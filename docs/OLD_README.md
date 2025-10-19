# TMDL Best Practices Analyzer Agent

An AI-powered tool that analyzes Power BI TMDL (Tabular Model Definition Language) files against Microsoft's Analysis Services best practice rules.

## Features

- 🔍 **Comprehensive Analysis**: Analyzes tables, measures, columns, and relationships in TMDL files
- 📊 **Best Practices Validation**: Checks against Microsoft's official Analysis Services best practice rules
- 🚨 **Detailed Reporting**: Generates detailed reports with violations, severity levels, and fix suggestions
- 🌐 **Web Interface**: Easy-to-use web interface for uploading and analyzing models
- 📄 **Export Reports**: Download analysis reports in Markdown format
- ⚡ **Fast Processing**: Efficiently parses and analyzes large TMDL models

## Installation

1. **Clone or download this repository**
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Ensure you have the BPARules.json file** (automatically downloaded from Microsoft's repository)

## OpenAI Integration (Optional)

The analyzer works perfectly **without** OpenAI, but you can enhance it with AI-powered features:

### Setting Up OpenAI API Key

**Option 1: Environment Variable (Recommended)**
```bash
# Windows PowerShell
$env:OPENAI_API_KEY = "sk-your-api-key-here"

# Linux/Mac
export OPENAI_API_KEY="sk-your-api-key-here"
```

**Option 2: Configuration File**
1. Copy `config_template.py` to `config.py`
2. Add your API key: `OPENAI_API_KEY = "sk-your-api-key-here"`

**Get API Key**: Visit [OpenAI Platform](https://platform.openai.com/api-keys)

### AI-Enhanced Features
- 🤖 **Smart Explanations**: Context-aware violation explanations
- 📊 **Strategic Recommendations**: High-level improvement strategies
- ⚡ **DAX Analysis**: Intelligent pattern detection
- 💡 **Custom Fixes**: Specific, actionable suggestions

See `OPENAI_SETUP.md` for detailed instructions.

## Usage

### Option 1: Command Line Interface

```bash
python tmdl_analyzer.py <model_path> [rules_file] [output_file]
```

**Examples:**
```bash
# Basic analysis
python tmdl_analyzer.py "Sales Dashboard.SemanticModel"

# With custom rules file and output
python tmdl_analyzer.py "Sales Dashboard.SemanticModel" BPARules.json report.md

# Analyze different model
python tmdl_analyzer.py "C:\Models\MyModel.SemanticModel" BPARules.json analysis.md
```

### Option 2: Web Interface

1. **Start the web server**:
   ```bash
   python web_interface.py
   ```

2. **Open your browser** and go to: `http://localhost:5000`

3. **Upload your TMDL model directory** using the web interface

4. **View results** and download reports directly from the browser

## Best Practice Rules Checked

The analyzer checks for violations in the following categories:

### Performance Rules
- ❌ Avoid floating point data types (Double)
- ⚡ Set IsAvailableInMdx to false on non-attribute columns
- 🔄 Avoid excessive bi-directional relationships
- 📊 Model should have a date table
- 🎯 Hide foreign keys
- 📈 Reduce usage of calculated columns

### DAX Expression Rules
- 📝 Column references should be fully qualified
- 🎯 Measure references should be unqualified
- ➗ Use DIVIDE function instead of `/` operator
- 🚫 Avoid IFERROR function
- 🔍 Filter expressions optimization
- 📋 No duplicate measures

### Formatting Rules
- 🏷️ Provide format strings for measures
- 📊 Hide fact table columns used in measures
- 🔤 Object naming conventions
- 📅 Date and month column formatting
- 🔢 Numeric column summarization settings

### Error Prevention Rules
- ✅ Data columns must have source columns
- 📜 Expression-reliant objects must have expressions
- 🔗 Relationship column data type consistency
- 🚫 Avoid invalid characters in names

### Maintenance Rules
- 🧹 Remove unnecessary columns and measures
- 🔗 Fix referential integrity violations
- 📖 Add descriptions to objects
- 🎭 Remove unused perspectives and roles

## Output

The analyzer generates comprehensive reports including:

- **Summary Statistics**: Count of tables, measures, columns, relationships
- **Violation Counts**: By severity (Error, Warning, Info) and category
- **Detailed Violations**: Specific issues found with:
  - Rule name and description
  - Affected object and location
  - Severity level
  - Fix suggestions (where available)

### Sample Output

```
# TMDL Best Practices Analysis Report

Model: Sales Dashboard.SemanticModel
Analysis Date: 2025-10-11 17:12:01

## Summary
- Tables: 9
- Measures: 56
- Columns: 106
- Relationships: 6
- Total Violations: 166

### Violations by Severity
- WARNING: 90
- ERROR: 76

### Violations by Category
- Performance: 63
- DAX Expressions: 43
- Formatting: 60
```

## File Structure

```
PBIP/
├── tmdl_analyzer.py          # Main analyzer engine
├── web_interface.py          # Web interface
├── BPARules.json            # Microsoft's best practice rules
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── Sales Dashboard.SemanticModel/  # Sample TMDL model
    ├── definition/
    │   ├── model.tmdl
    │   ├── relationships.tmdl
    │   └── tables/
    │       ├── Fact_Sales.tmdl
    │       ├── Dim_Customers.tmdl
    │       └── ...
    └── ...
```

## Technical Details

### TMDL Parser
- Parses table definitions and extracts measures, columns, properties
- Handles multi-line DAX expressions with proper escaping
- Extracts relationship definitions and cardinalities
- Supports complex TMDL syntax and annotations

### Rule Engine
- Implements Microsoft's Analysis Services best practice rules
- Supports rule expressions with pattern matching
- Evaluates DAX code for common anti-patterns
- Provides contextual fix suggestions

### Web Interface
- Flask-based web application
- Drag-and-drop file upload with directory support
- Real-time progress tracking
- Interactive results visualization
- Downloadable reports

## Supported TMDL Elements

- ✅ **Tables**: Data tables and calculated tables
- ✅ **Measures**: DAX measures with expressions and formatting
- ✅ **Columns**: Data columns, calculated columns, and properties
- ✅ **Relationships**: All relationship types and cardinalities
- ✅ **Partitions**: Data source and query information
- ✅ **Model Properties**: Model-level settings and annotations

## Best Practices Covered

The analyzer implements rules from Microsoft's official best practices guide:
- [Analysis Services Best Practice Rules](https://github.com/microsoft/Analysis-Services/tree/master/BestPracticeRules)
- Performance optimization recommendations
- DAX coding standards
- Data modeling best practices
- Security and maintenance guidelines

## Contributing

To add new rules or improve existing ones:

1. **Add rules to BPARules.json** following Microsoft's format
2. **Implement rule logic** in the `BestPracticesChecker` class
3. **Add tests** for new functionality
4. **Update documentation** with new rule descriptions

## Troubleshooting

### Common Issues

**"Definition folder not found"**
- Ensure you're pointing to the `.SemanticModel` directory
- Check that the `definition` folder exists with TMDL files

**"BPARules.json not found"**
- Ensure the rules file is in the same directory as the analyzer
- Download from the Microsoft repository if missing

**Web interface not starting**
- Check that Flask is installed: `pip install flask`
- Ensure port 5000 is not in use
- Try running with different port: modify `app.run(port=5001)`

## License

This tool is provided as-is for educational and analysis purposes. The best practice rules are from Microsoft's official Analysis Services repository.

## Version History

- **v1.0.0** - Initial release with core analysis functionality
- **v1.1.0** - Added web interface and improved reporting
- **v1.2.0** - Enhanced TMDL parsing and additional rule support
