"""
Simple web interface for the TMDL Best Practices Analyzer Agent

This provides an easy-to-use web interface for analyzing Power BI TMDL files.
"""

from flask import Flask, render_template_string, request, jsonify, send_file
import os
import sys
import json
from pathlib import Path
import tempfile
import traceback
from werkzeug.utils import secure_filename

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent))

from tmdl_analyzer import TMDLBestPracticesAgent

# Try to import AI-enhanced analyzer (optional)
try:
    from ai_enhanced_analyzer import AIEnhancedTMDLAnalyzer
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# HTML template for the web interface - Modern UI Design
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TMDL Best Practices Analyzer</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --primary-light: #818cf8;
            --secondary: #10b981;
            --danger: #ef4444;
            --warning: #f59e0b;
            --info: #3b82f6;
            --success: #22c55e;
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --bg-tertiary: #334155;
            --text-primary: #f1f5f9;
            --text-secondary: #cbd5e1;
            --text-muted: #94a3b8;
            --border: #334155;
            --card-bg: #1e293b;
            --shadow: rgba(0, 0, 0, 0.3);
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: var(--text-primary);
            min-height: 100vh;
            padding: 20px;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            padding: 40px 20px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            border-radius: 20px;
            box-shadow: 0 20px 60px var(--shadow);
            animation: fadeInDown 0.6s ease;
        }
        
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .header h1 {
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 15px;
            background: linear-gradient(to right, #fff, #e0e7ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .header p {
            font-size: 1.1rem;
            color: var(--text-secondary);
            margin-bottom: 20px;
        }
        
        .header-links {
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        .header-link {
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }
        
        .header-link:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-2px);
        }
        
        .main-card {
            background: var(--card-bg);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px var(--shadow);
            border: 1px solid var(--border);
            animation: fadeInUp 0.6s ease;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .upload-area {
            border: 3px dashed var(--border);
            border-radius: 16px;
            padding: 60px 40px;
            text-align: center;
            margin-bottom: 30px;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.05) 0%, rgba(79, 70, 229, 0.05) 100%);
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .upload-area:hover {
            border-color: var(--primary);
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(79, 70, 229, 0.1) 100%);
            transform: translateY(-2px);
        }
        
        .upload-area.dragover {
            border-color: var(--primary-light);
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(79, 70, 229, 0.15) 100%);
            transform: scale(1.02);
        }
        
        .upload-icon {
            font-size: 4rem;
            margin-bottom: 20px;
            animation: bounce 2s infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        .upload-area h3 {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 10px;
            color: var(--text-primary);
        }
        
        .btn {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            color: white;
            padding: 14px 32px;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            margin: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        .btn:disabled {
            background: var(--bg-tertiary);
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }
        
        .btn-success {
            background: linear-gradient(135deg, var(--secondary) 0%, #059669 100%);
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
        }
        
        .btn-success:hover {
            box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
        }
        
        .analyzer-selection {
            margin: 30px 0;
            padding: 30px;
            background: var(--bg-primary);
            border-radius: 16px;
            border: 1px solid var(--border);
        }
        
        .analyzer-selection h3 {
            font-size: 1.3rem;
            margin-bottom: 20px;
            color: var(--text-primary);
        }
        
        .radio-group {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        
        .radio-option {
            display: flex;
            align-items: center;
            padding: 20px;
            background: var(--card-bg);
            border: 2px solid var(--border);
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .radio-option:hover {
            border-color: var(--primary);
            transform: translateX(5px);
        }
        
        .radio-option input[type="radio"] {
            width: 20px;
            height: 20px;
            margin-right: 15px;
            cursor: pointer;
            accent-color: var(--primary);
        }
        
        .radio-option label {
            cursor: pointer;
            flex: 1;
        }
        
        .radio-option strong {
            display: block;
            font-size: 1.1rem;
            margin-bottom: 5px;
            color: var(--text-primary);
        }
        
        .alert {
            padding: 16px 20px;
            border-radius: 12px;
            margin: 15px 0;
            border-left: 4px solid;
            animation: slideIn 0.3s ease;
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        .alert-warning {
            background: rgba(245, 158, 11, 0.1);
            border-color: var(--warning);
            color: #fbbf24;
        }
        
        .alert-info {
            background: rgba(59, 130, 246, 0.1);
            border-color: var(--info);
            color: #60a5fa;
        }
        
        .alert-success {
            background: rgba(34, 197, 94, 0.1);
            border-color: var(--success);
            color: #4ade80;
        }
        
        .alert-danger {
            background: rgba(239, 68, 68, 0.1);
            border-color: var(--danger);
            color: #f87171;
        }
        
        .progress {
            display: none;
            margin: 30px 0;
        }
        
        .progress-bar {
            width: 100%;
            height: 8px;
            background: var(--bg-primary);
            border-radius: 10px;
            overflow: hidden;
            box-shadow: inset 0 2px 4px var(--shadow);
        }
        
        .progress-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--primary), var(--primary-light));
            width: 0%;
            transition: width 0.3s ease;
            animation: shimmer 2s infinite;
        }
        
        @keyframes shimmer {
            0% { background-position: -100% 0; }
            100% { background-position: 100% 0; }
        }
        
        .progress-text {
            text-align: center;
            margin-top: 15px;
            color: var(--text-secondary);
            font-weight: 500;
        }
        
        .spinner {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-top-color: white;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        .results {
            display: none;
            margin-top: 40px;
        }
        
        .results h2 {
            font-size: 2rem;
            margin-bottom: 30px;
            color: var(--text-primary);
        }
        
        .summary-card {
            background: var(--bg-primary);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 30px;
            margin: 20px 0;
            box-shadow: 0 4px 15px var(--shadow);
            transition: all 0.3s ease;
        }
        
        .summary-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px var(--shadow);
        }
        
        .summary-card h3 {
            font-size: 1.4rem;
            margin-bottom: 20px;
            color: var(--text-primary);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }
        
        .stat-item {
            padding: 20px;
            background: var(--card-bg);
            border-radius: 12px;
            border: 1px solid var(--border);
            text-align: center;
            transition: all 0.3s ease;
        }
        
        .stat-item:hover {
            border-color: var(--primary);
            transform: translateY(-2px);
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--primary-light);
            display: block;
        }
        
        .stat-label {
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-top: 5px;
        }
        
        .severity-badge {
            display: inline-block;
            padding: 6px 12px;
            border-radius: 8px;
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin: 0 5px;
        }
        
        .severity-error {
            background: rgba(239, 68, 68, 0.2);
            color: #f87171;
            border: 1px solid rgba(239, 68, 68, 0.3);
        }
        
        .severity-warning {
            background: rgba(245, 158, 11, 0.2);
            color: #fbbf24;
            border: 1px solid rgba(245, 158, 11, 0.3);
        }
        
        .severity-info {
            background: rgba(59, 130, 246, 0.2);
            color: #60a5fa;
            border: 1px solid rgba(59, 130, 246, 0.3);
        }
        
        .violation-item {
            background: var(--card-bg);
            border-left: 4px solid var(--danger);
            padding: 25px;
            margin: 15px 0;
            border-radius: 0 12px 12px 0;
            box-shadow: 0 4px 15px var(--shadow);
            transition: all 0.3s ease;
        }
        
        .violation-item:hover {
            transform: translateX(5px);
            box-shadow: 0 6px 20px var(--shadow);
        }
        
        .violation-item.warning {
            border-left-color: var(--warning);
        }
        
        .violation-item.info {
            border-left-color: var(--info);
        }
        
        .violation-item h4 {
            color: var(--text-primary);
            margin-bottom: 15px;
            font-size: 1.2rem;
        }
        
        .object-info {
            font-size: 14px;
            color: var(--text-muted);
            margin: 8px 0;
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }
        
        .category-section {
            margin-bottom: 40px;
        }
        
        .category-header {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            color: white;
            padding: 20px 25px;
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
        }
        
        .category-header h3 {
            margin: 0;
            font-size: 1.5rem;
        }
        
        .error {
            color: var(--danger);
            margin: 20px 0;
            padding: 20px;
            background: rgba(239, 68, 68, 0.1);
            border-radius: 12px;
            border: 1px solid rgba(239, 68, 68, 0.3);
            display: none;
        }
        
        .error:not(:empty) {
            display: block;
        }
        
        .fix-suggestion {
            background: rgba(34, 197, 94, 0.1);
            border: 1px solid rgba(34, 197, 94, 0.3);
            color: #4ade80;
            padding: 15px;
            margin-top: 15px;
            border-radius: 12px;
        }
        
        .ai-explanation {
            background: rgba(99, 102, 241, 0.1);
            border-left: 4px solid var(--primary);
            padding: 20px;
            margin: 15px 0;
            border-radius: 12px;
            color: var(--text-secondary);
        }
        
        details {
            margin: 20px 0;
        }
        
        summary {
            cursor: pointer;
            font-weight: 600;
            padding: 15px;
            background: var(--card-bg);
            border-radius: 12px;
            border: 1px solid var(--border);
            transition: all 0.3s ease;
            user-select: none;
        }
        
        summary:hover {
            background: var(--bg-tertiary);
            border-color: var(--primary);
        }
        
        details[open] summary {
            margin-bottom: 15px;
            border-color: var(--primary);
        }
        
        .rules-list {
            max-height: 500px;
            overflow-y: auto;
            padding-right: 10px;
        }
        
        .rules-list::-webkit-scrollbar {
            width: 8px;
        }
        
        .rules-list::-webkit-scrollbar-track {
            background: var(--bg-primary);
            border-radius: 4px;
        }
        
        .rules-list::-webkit-scrollbar-thumb {
            background: var(--border);
            border-radius: 4px;
        }
        
        .rules-list::-webkit-scrollbar-thumb:hover {
            background: var(--bg-tertiary);
        }
        
        .rule-item {
            padding: 15px;
            margin: 8px 0;
            border-left: 3px solid;
            background: var(--card-bg);
            border-radius: 0 8px 8px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.3s ease;
        }
        
        .rule-item:hover {
            transform: translateX(5px);
        }
        
        .rule-item.passed {
            border-left-color: var(--success);
            background: rgba(34, 197, 94, 0.05);
        }
        
        .rule-item.failed {
            border-left-color: var(--danger);
            background: rgba(239, 68, 68, 0.05);
        }
        
        @media (max-width: 768px) {
            .header h1 {
                font-size: 2rem;
            }
            
            .main-card {
                padding: 20px;
            }
            
            .upload-area {
                padding: 40px 20px;
            }
            
            .stats-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Modern Header -->
        <div class="header">
            <h1>🔍 TMDL Analyzer</h1>
            <p>Advanced Power BI TMDL analysis powered by Microsoft's best practices</p>
            <div class="header-links">
                <a href="https://github.com/microsoft/Analysis-Services/blob/master/BestPracticeRules/README.md" target="_blank" class="header-link">
                    📋 Best Practices Guide
                </a>
                <a href="#" onclick="alert('📖 TROUBLESHOOTING\\n\\nCommon issues:\\n• Make sure to select the .SemanticModel folder (not its parent)\\n• Folder must contain definition/ subfolder\\n• Export TMDL from Power BI: File → Export → Model → TMDL')" class="header-link">
                    🆘 Help & Troubleshooting
                </a>
            </div>
        </div>
        
        <!-- Main Content Card -->
        <div class="main-card">
            <form id="uploadForm" enctype="multipart/form-data">
                <!-- Upload Area -->
                <div class="upload-area" id="uploadArea">
                    <div class="upload-icon">📁</div>
                    <h3>Upload TMDL Model Directory</h3>
                    <p style="color: var(--text-secondary); margin: 10px 0;">
                        Select your <strong>.SemanticModel</strong> folder
                    </p>
                    <p style="font-size: 14px; color: var(--text-muted); margin-bottom: 20px;">
                        Your folder should contain a "definition" subfolder with TMDL files
                    </p>
                    <input type="file" id="fileInput" name="files" multiple webkitdirectory directory style="display: none;">
                    <button type="button" class="btn" onclick="document.getElementById('fileInput').click();">
                        Choose Directory
                    </button>
                </div>
                
                <!-- Analyzer Type Selection -->
                <div class="analyzer-selection">
                    <h3>🤖 Analyzer Type</h3>
                    <div class="radio-group">
                        <div class="radio-option">
                            <input type="radio" name="analyzer_type" value="regular" id="regular" checked>
                            <label for="regular">
                                <strong>⚡ Regular Analyzer</strong>
                                <div style="color: var(--text-muted); font-size: 0.9rem; margin-top: 5px;">
                                    Fast, rule-based analysis using Microsoft's best practices
                                </div>
                            </label>
                        </div>
                        <div class="radio-option">
                            <input type="radio" name="analyzer_type" value="ai_enhanced" id="ai_enhanced">
                            <label for="ai_enhanced">
                                <strong>🤖 AI-Enhanced Analyzer</strong>
                                <div style="color: var(--text-muted); font-size: 0.9rem; margin-top: 5px;">
                                    Includes strategic recommendations and detailed explanations (requires OpenAI API key)
                                </div>
                            </label>
                        </div>
                    </div>
                    <div id="aiWarning" class="alert alert-warning" style="display: none; margin-top: 15px;">
                        <strong>⚠️ Note:</strong> AI-Enhanced analysis requires an OpenAI API key to be configured. 
                        <a href="#" onclick="alert('To use AI-Enhanced analysis:\\n\\n1. Create src/config.py\\n2. Add: OPENAI_API_KEY = \\\"your-key-here\\\"\\n3. See docs/OPENAI_SETUP.md for details')" style="color: #fbbf24; text-decoration: underline;">
                            How to configure?
                        </a>
                    </div>
                </div>
                
                <!-- Analyze Button -->
                <div style="text-align: center;">
                    <button type="submit" class="btn" id="analyzeBtn">
                        🚀 Analyze Model
                    </button>
                </div>
            </form>
            
            <!-- Progress Indicator -->
            <div class="progress" id="progress">
                <div class="progress-bar">
                    <div class="progress-bar-fill" id="progressFill"></div>
                </div>
                <p class="progress-text">
                    <span class="spinner"></span> Analyzing your model...
                </p>
            </div>
            
            <!-- Error Display -->
            <div class="error" id="errorMsg"></div>
            
            <!-- Results Section -->
            <div class="results" id="results">
                <h2>📊 Analysis Results</h2>
                <div id="summarySection"></div>
                <div id="violationsSection"></div>
                
                <div style="text-align: center; margin-top: 40px;">
                    <button class="btn btn-success" id="downloadBtn" onclick="downloadReport()">
                        📄 Download Full Report
                    </button>
                </div>
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
        
        // Analyzer type selection handling
        const analyzerRadios = document.querySelectorAll('input[name="analyzer_type"]');
        const aiWarning = document.getElementById('aiWarning');
        
        analyzerRadios.forEach(radio => {
            radio.addEventListener('change', function() {
                if (this.value === 'ai_enhanced') {
                    aiWarning.style.display = 'block';
                } else {
                    aiWarning.style.display = 'none';
                }
            });
        });
        
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
                let alertClass = "alert-success";
                
                if (!hasSemanticModel) {
                    statusIcon = "⚠️";
                    statusText = "Warning: No .SemanticModel folder detected";
                    alertClass = "alert-warning";
                } else if (!hasDefinition) {
                    statusIcon = "❌";
                    statusText = "Error: No definition folder found";
                    alertClass = "alert-danger";
                }
                
                // Get the root folder name
                const rootFolder = fileList[0].webkitRelativePath.split('/')[0];
                
                uploadArea.innerHTML = `
                    <div class="upload-icon">${statusIcon}</div>
                    <h3>Directory Selected</h3>
                    <p style="color: var(--text-secondary); margin: 15px 0;">
                        <strong>Folder:</strong> ${rootFolder}
                    </p>
                    <div class="alert ${alertClass}" style="display: inline-block; margin: 10px auto;">
                        ${statusText}
                    </div>
                    <p style="font-size: 14px; color: var(--text-muted); margin: 15px 0;">
                        ${files.length} files selected
                    </p>
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
            
            // Add analyzer type selection
            const selectedAnalyzer = document.querySelector('input[name="analyzer_type"]:checked').value;
            formData.append('analyzer_type', selectedAnalyzer);
            
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
            clearError();
            
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
            const errorElement = document.getElementById('errorMsg');
            errorElement.textContent = message;
            errorElement.style.display = message ? 'block' : 'none';
            document.getElementById('results').style.display = 'none';
        }
        
        function clearError() {
            const errorElement = document.getElementById('errorMsg');
            errorElement.textContent = '';
            errorElement.style.display = 'none';
        }
        
        function displayResults(results) {
            clearError();
            const summary = results.summary;
            const violations = results.violations;
            
            // Analyzer type info
            let analyzerInfo = '';
            const analyzerType = results.analyzer_type || 'regular';
            
            if (analyzerType === 'ai_enhanced') {
                analyzerInfo = '<div class="alert alert-success">🤖 <strong>AI-Enhanced Analysis</strong> - Results include strategic recommendations and detailed explanations</div>';
            } else if (results.ai_fallback_reason) {
                analyzerInfo = `<div class="alert alert-warning">⚠️ <strong>AI Analysis Failed</strong> - Fell back to regular analysis<br><small>Reason: ${results.ai_fallback_reason}</small></div>`;
            } else if (results.ai_unavailable_reason) {
                analyzerInfo = `<div class="alert alert-danger">❌ <strong>AI Analysis Unavailable</strong><br><small>${results.ai_unavailable_reason}</small></div>`;
            } else {
                analyzerInfo = '<div class="alert alert-info">⚡ <strong>Regular Analysis</strong> - Fast rule-based checking</div>';
            }
            
            // Display summary
            const summaryHtml = `
                ${analyzerInfo}
                <div class="summary-card">
                    <h3>📈 Model Overview</h3>
                    <div class="stats-grid">
                        <div class="stat-item">
                            <span class="stat-number">${summary.object_counts.tables}</span>
                            <span class="stat-label">Tables</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-number">${summary.object_counts.measures}</span>
                            <span class="stat-label">Measures</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-number">${summary.object_counts.columns}</span>
                            <span class="stat-label">Columns</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-number">${summary.object_counts.relationships}</span>
                            <span class="stat-label">Relationships</span>
                        </div>
                    </div>
                </div>
                
                <div class="summary-card">
                    <h3>⚠️ Violations Summary</h3>
                    <div style="margin-bottom: 20px;">
                        <div class="stat-item" style="display: inline-block; min-width: 200px;">
                            <span class="stat-number" style="font-size: 3rem;">${summary.violations.total}</span>
                            <span class="stat-label">Total Violations</span>
                        </div>
                    </div>
                    <div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center;">
                        ${Object.entries(summary.violations.by_severity).map(([severity, count]) => 
                            `<span class="severity-badge severity-${severity.toLowerCase()}">${severity}: ${count}</span>`
                        ).join('')}
                    </div>
                </div>
                
                <div class="summary-card">
                    <h3>✅ Rules Checked</h3>
                    <div class="stats-grid" style="margin-bottom: 20px;">
                        <div class="stat-item">
                            <span class="stat-number">${summary.rules_checked.total}</span>
                            <span class="stat-label">Total Rules</span>
                        </div>
                        <div class="stat-item" style="border-color: var(--danger);">
                            <span class="stat-number" style="color: #f87171;">${summary.rules_checked.rules_with_violations}</span>
                            <span class="stat-label">With Violations</span>
                        </div>
                        <div class="stat-item" style="border-color: var(--success);">
                            <span class="stat-number" style="color: #4ade80;">${summary.rules_checked.rules_without_violations}</span>
                            <span class="stat-label">Passed</span>
                        </div>
                    </div>
                    <details>
                        <summary>
                            📋 View All Rules Checked (${summary.rules_checked.total})
                        </summary>
                        <div class="rules-list" style="margin-top: 15px;">
                            ${summary.rules_checked.all_rules.map(rule => `
                                <div class="rule-item ${rule.has_violations ? 'failed' : 'passed'}">
                                    <div style="flex: 1;">
                                        <strong style="color: var(--text-primary);">${rule.name}</strong>
                                        <div style="margin-top: 5px;">
                                            <span class="severity-badge severity-${rule.severity.toLowerCase()}">${rule.severity}</span>
                                            <span style="color: var(--text-muted); margin-left: 10px; font-size: 0.9em;">${rule.category}</span>
                                        </div>
                                    </div>
                                    <div style="text-align: right;">
                                        ${rule.has_violations 
                                            ? `<span style="color: #f87171; font-weight: bold;">❌ ${rule.violation_count} violation${rule.violation_count > 1 ? 's' : ''}</span>` 
                                            : `<span style="color: #4ade80; font-weight: bold;">✅ Passed</span>`
                                        }
                                    </div>
                                </div>
                            `).join('')}
                        </div>
                    </details>
                </div>
            `;
            
            document.getElementById('summarySection').innerHTML = summaryHtml;
            
            // Display AI recommendations if available
            if (results.ai_recommendations && results.ai_enhanced) {
                const recommendationsHtml = `
                    <div class="summary-card" style="border: 2px solid var(--primary); background: rgba(99, 102, 241, 0.05);">
                        <h3>🤖 AI Strategic Recommendations</h3>
                        <div class="ai-explanation">
                            <div style="white-space: pre-wrap; line-height: 1.8;">${results.ai_recommendations}</div>
                        </div>
                    </div>
                `;
                document.getElementById('summarySection').innerHTML += recommendationsHtml;
            }
            
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
                            <h3>${category} <span style="opacity: 0.8; font-weight: normal;">(${categoryViolations.length} violations)</span></h3>
                        </div>
                `;
                
                categoryViolations.forEach(violation => {
                    violationsHtml += `
                        <div class="violation-item ${violation.severity.toLowerCase()}">
                            <h4>${violation.rule_name}</h4>
                            <div class="object-info">
                                <span><strong>Object:</strong> ${violation.object_name} (${violation.object_type})</span>
                                <span class="severity-badge severity-${violation.severity.toLowerCase()}">${violation.severity}</span>
                                ${violation.ai_enhanced ? '<span class="severity-badge" style="background: rgba(99, 102, 241, 0.2); color: #818cf8; border: 1px solid rgba(99, 102, 241, 0.3);">🤖 AI Enhanced</span>' : ''}
                            </div>
                            <div class="object-info"><strong>File:</strong> ${violation.file_path}</div>
                            <p style="color: var(--text-secondary); margin: 15px 0;">${violation.description}</p>
                            ${violation.ai_explanation ? `
                                <div class="ai-explanation">
                                    <strong style="color: var(--primary-light);">🤖 AI Expert Analysis:</strong>
                                    <div style="margin-top: 10px; white-space: pre-wrap; line-height: 1.8;">${violation.ai_explanation}</div>
                                </div>
                            ` : ''}
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
        analyzer_type = request.form.get('analyzer_type', 'regular')
        
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
            
            # Get rules file path - now in data folder
            project_root = Path(__file__).parent.parent
            rules_file = str(project_root / 'data' / 'BPARules.json')
            if not Path(rules_file).exists():
                return f"BPARules.json not found at {rules_file}", 500
            
            # Run analysis based on selected analyzer type
            if analyzer_type == 'ai_enhanced' and AI_AVAILABLE:
                try:
                    # Use AI-enhanced analyzer
                    agent = AIEnhancedTMDLAnalyzer(rules_file)
                    result = agent.analyze_model(model_path)
                    # Add metadata to indicate AI analysis was used
                    result['analyzer_type'] = 'ai_enhanced'
                except Exception as ai_error:
                    # Fall back to regular analyzer if AI fails
                    app.logger.warning(f"AI-enhanced analysis failed, falling back to regular: {ai_error}")
                    agent = TMDLBestPracticesAgent(rules_file)
                    result = agent.analyze_model(model_path)
                    result['analyzer_type'] = 'regular'
                    result['ai_fallback_reason'] = str(ai_error)
            else:
                # Use regular analyzer
                agent = TMDLBestPracticesAgent(rules_file)
                result = agent.analyze_model(model_path)
                result['analyzer_type'] = 'regular'
                if analyzer_type == 'ai_enhanced' and not AI_AVAILABLE:
                    result['ai_unavailable_reason'] = 'AI-enhanced analyzer not available. Please check ai_enhanced_analyzer.py and OpenAI configuration.'
            
            # Convert result to JSON serializable format
            serializable_result = {
                'summary': result['summary'],
                'analyzer_type': result.get('analyzer_type', 'regular'),
                'ai_fallback_reason': result.get('ai_fallback_reason'),
                'ai_unavailable_reason': result.get('ai_unavailable_reason'),
                'ai_enhanced': result.get('ai_enhanced', False),
                'ai_recommendations': result.get('ai_recommendations', ''),
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
                        'fix_suggestion': v.fix_suggestion,
                        'ai_explanation': getattr(v, 'properties', {}).get('ai_explanation', ''),
                        'ai_enhanced': getattr(v, 'properties', {}).get('ai_enhanced', False)
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
        project_root = Path(__file__).parent.parent
        rules_file = str(project_root / 'data' / 'BPARules.json')
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
    project_root = Path(__file__).parent.parent
    rules_file = project_root / 'data' / 'BPARules.json'
    if not rules_file.exists():
        print(f"Warning: BPARules.json not found at {rules_file}")
        print("Please ensure the data/BPARules.json file exists.")
    
    print("Starting TMDL Best Practices Analyzer Web Interface...")
    print("Open your browser and go to: http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)