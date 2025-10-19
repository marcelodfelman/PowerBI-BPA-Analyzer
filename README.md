# 📊 TMDL Best Practices Analyzer# TMDL Best Practices Analyzer Agent



A comprehensive tool for analyzing Power BI TMDL (Tabular Model Definition Language) files against Microsoft's Analysis Services best practice rules, with optional AI-enhanced recommendations.An AI-powered tool that analyzes Power BI TMDL (Tabular Model Definition Language) files against Microsoft's Analysis Services best practice rules.



## 🚀 Quick Start## Features



### Web Interface (Recommended)- 🔍 **Comprehensive Analysis**: Analyzes tables, measures, columns, and relationships in TMDL files

```bash- 📊 **Best Practices Validation**: Checks against Microsoft's official Analysis Services best practice rules

python run_web_interface.py- 🚨 **Detailed Reporting**: Generates detailed reports with violations, severity levels, and fix suggestions

```- 🌐 **Web Interface**: Easy-to-use web interface for uploading and analyzing models

Then open http://localhost:5000 in your browser.- 📄 **Export Reports**: Download analysis reports in Markdown format

- ⚡ **Fast Processing**: Efficiently parses and analyzes large TMDL models

### Command Line

```bash## Installation

python run_analyzer.py "path/to/YourModel.SemanticModel"

```1. **Clone or download this repository**

2. **Install Python dependencies**:

## 📁 Project Structure   ```bash

   pip install -r requirements.txt

```   ```

PBIP/3. **Ensure you have the BPARules.json file** (automatically downloaded from Microsoft's repository)

├── run_web_interface.py      # Launch web interface

├── run_analyzer.py            # Command-line tool## OpenAI Integration (Optional)

├── requirements.txt           # Python dependencies

├── .gitignore                # Git ignore rulesThe analyzer works perfectly **without** OpenAI, but you can enhance it with AI-powered features:

├── config_template.py        # OpenAI configuration template

│### Setting Up OpenAI API Key

├── src/                      # Source code

│   ├── __init__.py**Option 1: Environment Variable (Recommended)**

│   ├── tmdl_analyzer.py      # Core analyzer```bash

│   ├── ai_enhanced_analyzer.py  # AI-enhanced analyzer# Windows PowerShell

│   ├── web_interface.py      # Flask web app$env:OPENAI_API_KEY = "sk-your-api-key-here"

│   └── config.py             # Configuration (create from template)

│# Linux/Mac

├── data/                     # Data filesexport OPENAI_API_KEY="sk-your-api-key-here"

│   └── BPARules.json         # Microsoft best practice rules```

│

├── tests/                    # Test files**Option 2: Configuration File**

│   ├── test_ai_analyzer.py1. Copy `config_template.py` to `config.py`

│   ├── test_ai_enhancements.py2. Add your API key: `OPENAI_API_KEY = "sk-your-api-key-here"`

│   ├── test_column_references.py

│   ├── test_rules.py**Get API Key**: Visit [OpenAI Platform](https://platform.openai.com/api-keys)

│   └── debug_column_refs.py

│### AI-Enhanced Features

├── examples/                 # Example scripts- 🤖 **Smart Explanations**: Context-aware violation explanations

│   ├── demo.py- 📊 **Strategic Recommendations**: High-level improvement strategies

│   ├── quick_start_ai.py- ⚡ **DAX Analysis**: Intelligent pattern detection

│   └── example_with_openai.py- 💡 **Custom Fixes**: Specific, actionable suggestions

│

├── docs/                     # DocumentationSee `OPENAI_SETUP.md` for detailed instructions.

│   ├── OPENAI_SETUP.md

│   ├── TROUBLESHOOTING.md## Usage

│   ├── AI_CONFIGURATION_FIXED.md

│   ├── AI_FIXES_COMPLETE.md### Option 1: Command Line Interface

│   ├── AI_PERFORMANCE_FIXES.md

│   ├── AI_RULE_TYPE_OPTIMIZATION.md```bash

│   ├── RULE_LEVEL_AI_ENHANCEMENT.mdpython tmdl_analyzer.py <model_path> [rules_file] [output_file]

│   └── ALL_RULES_VISIBILITY.md```

│

└── reports/                  # Generated reports**Examples:**

    ├── analysis_report.md```bash

    └── demo_analysis_report.md# Basic analysis

```python tmdl_analyzer.py "Sales Dashboard.SemanticModel"



## 📦 Installation# With custom rules file and output

python tmdl_analyzer.py "Sales Dashboard.SemanticModel" BPARules.json report.md

1. **Clone or download** this repository

# Analyze different model

2. **Install dependencies:**python tmdl_analyzer.py "C:\Models\MyModel.SemanticModel" BPARules.json analysis.md

   ```bash```

   pip install -r requirements.txt

   ```### Option 2: Web Interface



3. **(Optional) Configure OpenAI for AI-enhanced analysis:**1. **Start the web server**:

   ```bash   ```bash

   # Windows   python web_interface.py

   copy config_template.py src\\config.py   ```

   

   # Linux/Mac2. **Open your browser** and go to: `http://localhost:5000`

   cp config_template.py src/config.py

   3. **Upload your TMDL model directory** using the web interface

   # Edit src/config.py and add your OpenAI API key

   ```4. **View results** and download reports directly from the browser



## 🎯 Features## Best Practice Rules Checked



### Core AnalysisThe analyzer checks for violations in the following categories:

- ✅ Parses TMDL files from Power BI semantic models

- ✅ Checks 8+ best practice rules from Microsoft### Performance Rules

- ✅ Identifies violations with severity levels- ❌ Avoid floating point data types (Double)

- ✅ Provides fix suggestions where available- ⚡ Set IsAvailableInMdx to false on non-attribute columns

- ✅ Generates detailed markdown reports- 🔄 Avoid excessive bi-directional relationships

- ✅ Shows all rules checked (even those with 0 violations)- 📊 Model should have a date table

- 🎯 Hide foreign keys

### AI-Enhanced Analysis (Optional)- 📈 Reduce usage of calculated columns

- 🤖 Strategic recommendations for your model

- 🤖 Rule-level explanations (not per-violation to save costs)### DAX Expression Rules

- 🤖 Priority ranking and effort estimates- 📝 Column references should be fully qualified

- 🤖 Implementation strategies- 🎯 Measure references should be unqualified

- 🤖 90% cost reduction vs. individual enhancements- ➗ Use DIVIDE function instead of `/` operator

- 🚫 Avoid IFERROR function

### Web Interface- 🔍 Filter expressions optimization

- 🌐 Drag & drop file upload- 📋 No duplicate measures

- 🌐 Real-time analysis

- 🌐 Interactive results viewer### Formatting Rules

- 🌐 Expandable rule checklist- 🏷️ Provide format strings for measures

- 🌐 Download reports- 📊 Hide fact table columns used in measures

- 🌐 AI analyzer selector- 🔤 Object naming conventions

- 📅 Date and month column formatting

## 📖 Usage- 🔢 Numeric column summarization settings



### Method 1: Web Interface### Error Prevention Rules

- ✅ Data columns must have source columns

```bash- 📜 Expression-reliant objects must have expressions

python run_web_interface.py- 🔗 Relationship column data type consistency

```- 🚫 Avoid invalid characters in names



1. Open http://localhost:5000### Maintenance Rules

2. Choose analyzer type (Regular or AI-Enhanced)- 🧹 Remove unnecessary columns and measures

3. Upload your `.SemanticModel` folder- 🔗 Fix referential integrity violations

4. View results and download report- 📖 Add descriptions to objects

- 🎭 Remove unused perspectives and roles

### Method 2: Command Line

## Output

**Basic analysis:**

```bashThe analyzer generates comprehensive reports including:

python run_analyzer.py "Sales Dashboard.SemanticModel"

```- **Summary Statistics**: Count of tables, measures, columns, relationships

- **Violation Counts**: By severity (Error, Warning, Info) and category

**AI-enhanced analysis:**- **Detailed Violations**: Specific issues found with:

```bash  - Rule name and description

python run_analyzer.py "Sales Dashboard.SemanticModel" --ai  - Affected object and location

```  - Severity level

  - Fix suggestions (where available)

**Custom output:**

```bash### Sample Output

python run_analyzer.py "Sales Dashboard.SemanticModel" --output "reports/my_report.md"

``````

# TMDL Best Practices Analysis Report

### Method 3: Python API

Model: Sales Dashboard.SemanticModel

```pythonAnalysis Date: 2025-10-11 17:12:01

import sys

sys.path.insert(0, 'src')## Summary

- Tables: 9

from tmdl_analyzer import TMDLBestPracticesAgent- Measures: 56

- Columns: 106

# Create analyzer- Relationships: 6

agent = TMDLBestPracticesAgent('data/BPARules.json')- Total Violations: 166



# Analyze model### Violations by Severity

result = agent.analyze_model('Sales Dashboard.SemanticModel')- WARNING: 90

- ERROR: 76

# Generate report

agent.generate_report(result, 'reports/output.md')### Violations by Category

```- Performance: 63

- DAX Expressions: 43

**AI-enhanced:**- Formatting: 60

```python```

from ai_enhanced_analyzer import AIEnhancedTMDLAnalyzer

## File Structure

agent = AIEnhancedTMDLAnalyzer('data/BPARules.json')

result = agent.analyze_model('Sales Dashboard.SemanticModel')```

```PBIP/

├── tmdl_analyzer.py          # Main analyzer engine

## 🔧 Configuration├── web_interface.py          # Web interface

├── BPARules.json            # Microsoft's best practice rules

### OpenAI API Key (for AI features)├── requirements.txt         # Python dependencies

├── README.md               # This file

Create `src/config.py`:└── Sales Dashboard.SemanticModel/  # Sample TMDL model

```python    ├── definition/

# OpenAI Configuration    │   ├── model.tmdl

OPENAI_API_KEY = "sk-proj-your-api-key-here"    │   ├── relationships.tmdl

OPENAI_MODEL = "gpt-4"  # or "gpt-3.5-turbo" for faster/cheaper    │   └── tables/

MAX_TOKENS = 300    │       ├── Fact_Sales.tmdl

TEMPERATURE = 0.3    │       ├── Dim_Customers.tmdl

```    │       └── ...

    └── ...

Or set environment variable:```

```bash

# Windows## Technical Details

set OPENAI_API_KEY=sk-proj-your-key-here

### TMDL Parser

# Linux/Mac- Parses table definitions and extracts measures, columns, properties

export OPENAI_API_KEY=sk-proj-your-key-here- Handles multi-line DAX expressions with proper escaping

```- Extracts relationship definitions and cardinalities

- Supports complex TMDL syntax and annotations

## 📊 Analysis Results

### Rule Engine

### What Gets Checked- Implements Microsoft's Analysis Services best practice rules

- Supports rule expressions with pattern matching

The analyzer checks all 8 rules from Microsoft's BPARules.json:- Evaluates DAX code for common anti-patterns

- Provides contextual fix suggestions

1. **[Performance] Do not use floating point data types**

2. **[Performance] Set IsAvailableInMdx to false on non-attribute columns**### Web Interface

3. **[DAX Expressions] Column references should be fully qualified**- Flask-based web application

4. **[DAX Expressions] Measure references should be unqualified**- Drag-and-drop file upload with directory support

5. **[DAX Expressions] Use the DIVIDE function for division**- Real-time progress tracking

6. **[DAX Expressions] Avoid using the IFERROR function**- Interactive results visualization

7. **[Formatting] Provide format string for measures**- Downloadable reports

8. **[Formatting] Hide foreign keys**

## Supported TMDL Elements

### Results Include

- ✅ **Tables**: Data tables and calculated tables

- **Summary:** Object counts, violation totals by severity/category- ✅ **Measures**: DAX measures with expressions and formatting

- **Rules Checked:** All 8 rules showing passed ✅ or violations ❌- ✅ **Columns**: Data columns, calculated columns, and properties

- **Violations:** Detailed list with object info, descriptions, fix suggestions- ✅ **Relationships**: All relationship types and cardinalities

- **AI Recommendations:** (AI mode) Strategic guidance and implementation plan- ✅ **Partitions**: Data source and query information

- ✅ **Model Properties**: Model-level settings and annotations

## 📚 Documentation

## Best Practices Covered

- **[docs/OPENAI_SETUP.md](docs/OPENAI_SETUP.md)** - Configure AI features

- **[docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)** - Common issues and solutionsThe analyzer implements rules from Microsoft's official best practices guide:

- **[docs/RULE_LEVEL_AI_ENHANCEMENT.md](docs/RULE_LEVEL_AI_ENHANCEMENT.md)** - How AI analysis works- [Analysis Services Best Practice Rules](https://github.com/microsoft/Analysis-Services/tree/master/BestPracticeRules)

- **[docs/ALL_RULES_VISIBILITY.md](docs/ALL_RULES_VISIBILITY.md)** - Understanding the rules checklist- Performance optimization recommendations

- DAX coding standards

## 🧪 Testing- Data modeling best practices

- Security and maintenance guidelines

Run tests:

```bash## Contributing

# Navigate to tests directory

cd testsTo add new rules or improve existing ones:



# Run individual tests1. **Add rules to BPARules.json** following Microsoft's format

python test_rules.py2. **Implement rule logic** in the `BestPracticesChecker` class

python test_ai_analyzer.py3. **Add tests** for new functionality

```4. **Update documentation** with new rule descriptions



## 💡 Examples## Troubleshooting



Check the `examples/` folder for sample scripts:### Common Issues

- `demo.py` - Basic usage example

- `quick_start_ai.py` - AI-enhanced quick start**"Definition folder not found"**

- `example_with_openai.py` - Advanced AI integration- Ensure you're pointing to the `.SemanticModel` directory

- Check that the `definition` folder exists with TMDL files

## 🤝 Contributing

**"BPARules.json not found"**

1. Fork the repository- Ensure the rules file is in the same directory as the analyzer

2. Create a feature branch- Download from the Microsoft repository if missing

3. Make your changes

4. Test thoroughly**Web interface not starting**

5. Submit a pull request- Check that Flask is installed: `pip install flask`

- Ensure port 5000 is not in use

## 📄 License- Try running with different port: modify `app.run(port=5001)`



This project uses Microsoft's BPARules.json for best practice rules.## License



## 🆘 SupportThis tool is provided as-is for educational and analysis purposes. The best practice rules are from Microsoft's official Analysis Services repository.



- Check [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) for common issues## Version History

- Review example scripts in `examples/`

- Check documentation in `docs/`- **v1.0.0** - Initial release with core analysis functionality

- **v1.1.0** - Added web interface and improved reporting

## 🎯 Roadmap- **v1.2.0** - Enhanced TMDL parsing and additional rule support


- [ ] Add more Microsoft best practice rules
- [ ] Support for custom rules
- [ ] Export to different formats (JSON, CSV)
- [ ] Integration with Power BI pipelines
- [ ] Enhanced AI features

---

**Made with ❤️ for the Power BI community**
