"""
Simple web interface for the TMDL Best Practices Analyzer Agent

This provides an easy-to-use web interface for analyzing Power BI TMDL files.
"""

from flask import Flask, render_template_string, request, jsonify, send_file
import os
import json
from tmdl_analyzer import TMDLBestPracticesAgent
import tempfile
import traceback
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TMDL Best Practices Analyzer</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        .upload-area {
            border: 2px dashed #ddd;
            border-radius: 10px;
            padding: 40px;
            text-align: center;
            margin-bottom: 20px;
            background-color: #fafafa;
        }
        .upload-area.dragover {
            border-color: #007acc;
            background-color: #f0f8ff;
        }
        .btn {
            background-color: #007acc;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin: 10px;
        }
        .btn:hover {
            background-color: #005a9e;
        }
        .btn:disabled {
            background-color: #ccc;
            cursor: not-allowed;
        }
        .progress {
            display: none;
            margin: 20px 0;
        }
        .progress-bar {
            width: 100%;
            height: 20px;
            background-color: #f0f0f0;
            border-radius: 10px;
            overflow: hidden;
        }
        .progress-bar-fill {
            height: 100%;
            background-color: #007acc;
            width: 0%;
            transition: width 0.3s ease;
        }
        .results {
            display: none;
            margin-top: 30px;
        }
        .summary-card {
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 20px;
            margin: 15px 0;
        }
        .violation-item {
            background-color: #fff;
            border-left: 4px solid #dc3545;
            padding: 15px;
            margin: 10px 0;
            border-radius: 0 5px 5px 0;
        }
        .violation-item.warning {
            border-left-color: #ffc107;
        }
        .violation-item.info {
            border-left-color: #17a2b8;
        }
        .severity-badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
            text-transform: uppercase;
        }
        .severity-error {
            background-color: #dc3545;
            color: white;
        }
        .severity-warning {
            background-color: #ffc107;
            color: #212529;
        }
        .severity-info {
            background-color: #17a2b8;
            color: white;
        }
        .category-section {
            margin-bottom: 30px;
        }
        .category-header {
            background-color: #007acc;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            margin-bottom: 15px;
        }
        .error {
            color: #dc3545;
            margin: 10px 0;
        }
        .object-info {
            font-size: 14px;
            color: #666;
            margin: 5px 0;
        }
        .fix-suggestion {
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            color: #155724;
            padding: 10px;
            margin-top: 10px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 TMDL Best Practices Analyzer</h1>
        <p style="text-align: center; color: #666; margin-bottom: 20px;">
            Analyze your Power BI TMDL files against Microsoft's Analysis Services best practices
        </p>
        <div style="text-align: center; margin-bottom: 20px;">
            <a href="#" onclick="window.open('https://github.com/microsoft/Analysis-Services/blob/master/BestPracticeRules/README.md', '_blank')" style="color: #007acc; text-decoration: none; margin-right: 20px;">📋 Best Practices Guide</a>
            <span style="color: #ccc;">|</span>
            <a href="#" onclick="alert('📖 TROUBLESHOOTING.md\\n\\nCommon issues:\\n• Make sure to select the .SemanticModel folder (not its parent)\\n• Folder must contain definition/ subfolder\\n• Export TMDL from Power BI: File → Export → Model → TMDL')" style="color: #007acc; text-decoration: none; margin-left: 20px;">🆘 Help & Troubleshooting</a>
        </div>
        
        <form id="uploadForm" enctype="multipart/form-data">
            <div class="upload-area" id="uploadArea">
                <h3>Upload TMDL Model Directory</h3>
                <p><strong>Select your .SemanticModel folder</strong></p>
                <p style="font-size: 14px; color: #666;">
                    📁 Your folder should be named like "MyModel.SemanticModel" and contain a "definition" subfolder with TMDL files.
                </p>
                <input type="file" id="fileInput" name="files" multiple webkitdirectory directory style="display: none;">
                <button type="button" class="btn" onclick="document.getElementById('fileInput').click();">
                    📂 Choose .SemanticModel Directory
                </button>
                <div style="margin-top: 15px; font-size: 12px; color: #888;">
                    💡 Tip: Click "Choose Directory" and select your .SemanticModel folder (e.g., "Sales Dashboard.SemanticModel")
                </div>
            </div>
            
            <div style="text-align: center;">
                <button type="submit" class="btn" id="analyzeBtn">
                    🚀 Analyze Model
                </button>
            </div>
        </form>
        
        <div class="progress" id="progress">
            <div class="progress-bar">
                <div class="progress-bar-fill" id="progressFill"></div>
            </div>
            <p style="text-align: center; margin-top: 10px;">Analyzing model...</p>
        </div>
        
        <div class="error" id="errorMsg"></div>
        
        <div class="results" id="results">
            <h2>📊 Analysis Results</h2>
            <div id="summarySection"></div>
            <div id="violationsSection"></div>
            
            <div style="text-align: center; margin-top: 30px;">
                <button class="btn" id="downloadBtn" onclick="downloadReport()">
                    📄 Download Full Report
                </button>
            </div>
        </div>
    </div>

    <script>
        let analysisResults = null;
        
        // File upload handling
        const uploadArea = document.getElementById('uploadArea');
        const fileInput = document.getElementById('fileInput');
        
        uploadArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadArea.classList.add('dragover');
        });
        
        uploadArea.addEventListener('dragleave', () => {
            uploadArea.classList.remove('dragover');
        });
        
        uploadArea.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadArea.classList.remove('dragover');
            fileInput.files = e.dataTransfer.files;
            updateFileDisplay();
        });
        
        fileInput.addEventListener('change', updateFileDisplay);
        
        function updateFileDisplay() {
            const files = fileInput.files;
            if (files.length > 0) {
                // Check if we have a .SemanticModel structure
                const fileList = Array.from(files);
                const hasSemanticModel = fileList.some(file => 
                    file.webkitRelativePath.includes('.SemanticModel')
                );
                const hasDefinition = fileList.some(file => 
                    file.webkitRelativePath.includes('definition/')
                );
                
                let statusIcon = "✅";
                let statusText = "Files ready for analysis";
                let statusColor = "#28a745";
                
                if (!hasSemanticModel) {
                    statusIcon = "⚠️";
                    statusText = "Warning: No .SemanticModel folder detected";
                    statusColor = "#ffc107";
                } else if (!hasDefinition) {
                    statusIcon = "❌";
                    statusText = "Error: No definition folder found";
                    statusColor = "#dc3545";
                }
                
                // Get the root folder name
                const rootFolder = fileList[0].webkitRelativePath.split('/')[0];
                
                uploadArea.innerHTML = `
                    <h3>${statusIcon} Directory Selected</h3>
                    <p><strong>Folder:</strong> ${rootFolder}</p>
                    <p style="color: ${statusColor};">${statusText}</p>
                    <p style="font-size: 14px; color: #666;">${files.length} files selected</p>
                    <button type="button" class="btn" onclick="document.getElementById('fileInput').click();">
                        📂 Choose Different Directory
                    </button>
                `;
            }
        }
        
        // Form submission
        document.getElementById('uploadForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const files = fileInput.files;
            if (files.length === 0) {
                showError('Please select a directory first');
                return;
            }
            
            showProgress();
            
            const formData = new FormData();
            for (let file of files) {
                formData.append('files', file);
            }
            
            try {
                const response = await fetch('/analyze', {
                    method: 'POST',
                    body: formData
                });
                
                if (!response.ok) {
                    throw new Error(await response.text());
                }
                
                analysisResults = await response.json();
                displayResults(analysisResults);
                
            } catch (error) {
                showError('Analysis failed: ' + error.message);
            } finally {
                hideProgress();
            }
        });
        
        function showProgress() {
            document.getElementById('progress').style.display = 'block';
            document.getElementById('analyzeBtn').disabled = true;
            document.getElementById('results').style.display = 'none';
            document.getElementById('errorMsg').textContent = '';
            
            // Simulate progress
            let progress = 0;
            const interval = setInterval(() => {
                progress += Math.random() * 15;
                if (progress > 90) progress = 90;
                document.getElementById('progressFill').style.width = progress + '%';
            }, 200);
            
            // Store interval for cleanup
            window.progressInterval = interval;
        }
        
        function hideProgress() {
            document.getElementById('progress').style.display = 'none';
            document.getElementById('analyzeBtn').disabled = false;
            document.getElementById('progressFill').style.width = '100%';
            
            if (window.progressInterval) {
                clearInterval(window.progressInterval);
            }
        }
        
        function showError(message) {
            document.getElementById('errorMsg').textContent = message;
            document.getElementById('results').style.display = 'none';
        }
        
        function displayResults(results) {
            const summary = results.summary;
            const violations = results.violations;
            
            // Display summary
            const summaryHtml = `
                <div class="summary-card">
                    <h3>📈 Model Overview</h3>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 15px;">
                        <div><strong>Tables:</strong> ${summary.object_counts.tables}</div>
                        <div><strong>Measures:</strong> ${summary.object_counts.measures}</div>
                        <div><strong>Columns:</strong> ${summary.object_counts.columns}</div>
                        <div><strong>Relationships:</strong> ${summary.object_counts.relationships}</div>
                    </div>
                </div>
                
                <div class="summary-card">
                    <h3>⚠️ Violations Summary</h3>
                    <div><strong>Total Violations:</strong> ${summary.violations.total}</div>
                    <div style="margin-top: 10px;">
                        ${Object.entries(summary.violations.by_severity).map(([severity, count]) => 
                            `<span class="severity-badge severity-${severity.toLowerCase()}">${severity}: ${count}</span>`
                        ).join(' ')}
                    </div>
                </div>
            `;
            
            document.getElementById('summarySection').innerHTML = summaryHtml;
            
            // Display violations by category
            const violationsByCategory = {};
            violations.forEach(violation => {
                if (!violationsByCategory[violation.category]) {
                    violationsByCategory[violation.category] = [];
                }
                violationsByCategory[violation.category].push(violation);
            });
            
            let violationsHtml = '';
            Object.entries(violationsByCategory).forEach(([category, categoryViolations]) => {
                violationsHtml += `
                    <div class="category-section">
                        <div class="category-header">
                            <h3>${category} (${categoryViolations.length} violations)</h3>
                        </div>
                `;
                
                categoryViolations.forEach(violation => {
                    violationsHtml += `
                        <div class="violation-item ${violation.severity.toLowerCase()}">
                            <h4>${violation.rule_name}</h4>
                            <div class="object-info">
                                <strong>Object:</strong> ${violation.object_name} (${violation.object_type})
                                <span class="severity-badge severity-${violation.severity.toLowerCase()}">${violation.severity}</span>
                            </div>
                            <div class="object-info"><strong>File:</strong> ${violation.file_path}</div>
                            <p>${violation.description}</p>
                            ${violation.fix_suggestion ? `
                                <div class="fix-suggestion">
                                    <strong>💡 Fix Suggestion:</strong> ${violation.fix_suggestion}
                                </div>
                            ` : ''}
                        </div>
                    `;
                });
                
                violationsHtml += '</div>';
            });
            
            document.getElementById('violationsSection').innerHTML = violationsHtml;
            document.getElementById('results').style.display = 'block';
        }
        
        async function downloadReport() {
            if (!analysisResults) return;
            
            try {
                const response = await fetch('/generate_report', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(analysisResults)
                });
                
                if (!response.ok) {
                    throw new Error('Failed to generate report');
                }
                
                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'TMDL_Analysis_Report.md';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
                document.body.removeChild(a);
                
            } catch (error) {
                showError('Failed to download report: ' + error.message);
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Serve the main web interface"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze uploaded TMDL files"""
    try:
        files = request.files.getlist('files')
        if not files:
            return "No files uploaded", 400
        
        # Create temporary directory for uploaded files
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save uploaded files maintaining directory structure
            for file in files:
                if file.filename:
                    # Get the original file path (browsers send the relative path)
                    original_path = file.filename.replace('\\', '/')  # Normalize path separators
                    
                    # Create the full file path in temp directory
                    file_path = os.path.join(temp_dir, original_path)
                    
                    # Create directories if needed
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    file.save(file_path)
            
            # Find the model directory (look for .SemanticModel folder with definition subfolder)
            model_path = None
            
            # First, look for any .SemanticModel directory
            for root, dirs, files_list in os.walk(temp_dir):
                for dir_name in dirs:
                    if dir_name.endswith('.SemanticModel'):
                        potential_model_path = os.path.join(root, dir_name)
                        definition_path = os.path.join(potential_model_path, 'definition')
                        if os.path.exists(definition_path):
                            model_path = potential_model_path
                            break
                if model_path:
                    break
            
            # If not found, look for any directory with 'definition' folder
            if not model_path:
                for root, dirs, files_list in os.walk(temp_dir):
                    if 'definition' in dirs:
                        model_path = root
                        break
            
            if not model_path:
                # Debug: List the uploaded structure
                debug_info = []
                for root, dirs, files_list in os.walk(temp_dir):
                    level = root.replace(temp_dir, '').count(os.sep)
                    indent = ' ' * 2 * level
                    debug_info.append(f"{indent}{os.path.basename(root)}/")
                    subindent = ' ' * 2 * (level + 1)
                    for file in files_list:
                        debug_info.append(f"{subindent}{file}")
                
                debug_structure = '\n'.join(debug_info)
                return f"No valid TMDL model found. Please ensure you upload a directory ending with '.SemanticModel' that contains a 'definition' folder.\n\nUploaded structure:\n{debug_structure}\n\n📖 See TROUBLESHOOTING.md for detailed help with folder structure and upload issues.", 400
            
            # Get rules file path
            rules_file = os.path.join(os.path.dirname(__file__), 'BPARules.json')
            if not os.path.exists(rules_file):
                return "BPARules.json not found", 500
            
            # Run analysis
            agent = TMDLBestPracticesAgent(rules_file)
            result = agent.analyze_model(model_path)
            
            # Convert result to JSON serializable format
            serializable_result = {
                'summary': result['summary'],
                'violations': [
                    {
                        'rule_id': v.rule_id,
                        'rule_name': v.rule_name,
                        'category': v.category,
                        'severity': v.severity.name,
                        'description': v.description,
                        'object_name': v.object_name,
                        'object_type': v.object_type,
                        'file_path': v.file_path,
                        'fix_suggestion': v.fix_suggestion
                    }
                    for v in result['violations']
                ],
                'model_path': result['model_path']
            }
            
            return jsonify(serializable_result)
            
    except Exception as e:
        app.logger.error(f"Analysis error: {traceback.format_exc()}")
        return f"Analysis failed: {str(e)}", 500

@app.route('/generate_report', methods=['POST'])
def generate_report():
    """Generate and download a detailed report"""
    try:
        data = request.get_json()
        
        # Create a temporary TMDLBestPracticesAgent to use its report generation
        rules_file = os.path.join(os.path.dirname(__file__), 'BPARules.json')
        agent = TMDLBestPracticesAgent(rules_file)
        
        # Reconstruct violations objects for report generation
        from tmdl_analyzer import Violation, Severity
        violations = []
        for v_data in data['violations']:
            violation = Violation(
                rule_id=v_data['rule_id'],
                rule_name=v_data['rule_name'],
                category=v_data['category'],
                severity=Severity[v_data['severity']],
                description=v_data['description'],
                object_name=v_data['object_name'],
                object_type=v_data['object_type'],
                file_path=v_data['file_path'],
                fix_suggestion=v_data.get('fix_suggestion')
            )
            violations.append(violation)
        
        # Reconstruct result object
        result = {
            'summary': data['summary'],
            'violations': violations,
            'model_path': data['model_path']
        }
        
        # Generate report
        report_content = agent.generate_report(result)
        
        # Return as downloadable file
        return app.response_class(
            report_content,
            mimetype='text/markdown',
            headers={"Content-disposition": "attachment; filename=TMDL_Analysis_Report.md"}
        )
        
    except Exception as e:
        app.logger.error(f"Report generation error: {traceback.format_exc()}")
        return f"Report generation failed: {str(e)}", 500

if __name__ == '__main__':
    # Check if BPARules.json exists
    rules_file = os.path.join(os.path.dirname(__file__), 'BPARules.json')
    if not os.path.exists(rules_file):
        print("Warning: BPARules.json not found. Please ensure it's in the same directory as this script.")
    
    print("Starting TMDL Best Practices Analyzer Web Interface...")
    print("Open your browser and go to: http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)