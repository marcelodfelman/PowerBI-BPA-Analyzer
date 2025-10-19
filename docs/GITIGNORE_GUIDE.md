# .gitignore Configuration

## Updated for New Project Structure ✅

The `.gitignore` file has been updated to work with the new organized folder structure.

## What's Ignored

### 🔒 Sensitive Files
- `src/config.py` - Contains OpenAI API key
- `config.py` - Fallback config location
- `.env` / `.env.local` - Environment variables

### 🐍 Python Files
- `__pycache__/` - Python cache folders (all locations)
- `*.pyc`, `*.pyo`, `*.pyd` - Compiled Python files
- `.venv/`, `venv/`, `env/` - Virtual environments
- `*.egg-info/` - Package metadata
- `.pytest_cache/` - Pytest cache
- `.mypy_cache/` - MyPy type checker cache

### 📊 Generated Reports
- `reports/*.md` - All generated report files
- Generated reports are ignored but the folder structure is preserved

### 🧪 Test Outputs
- `tests/output/` - Test output files
- `tests/*.log` - Test log files

### 💻 IDE/Editor Files
- `.vscode/` - VS Code settings
- `.idea/` - PyCharm/IntelliJ settings
- `*.swp`, `*.swo` - Vim swap files

### 🖥️ OS Files
- `.DS_Store` - macOS
- `Thumbs.db` - Windows
- `desktop.ini` - Windows

### 📦 Distribution
- `build/`, `dist/` - Build outputs
- `*.egg`, `*.egg-info/` - Package files

### 📓 Jupyter
- `.ipynb_checkpoints` - Jupyter notebook checkpoints

### 📝 Logs
- `*.log` - All log files
- `logs/` - Log directory

### ⚡ Power BI Specific
- `**/.pbi/localSettings.json` - Local Power BI settings
- `**/.pbi/cache.abf` - Power BI cache

## What's Tracked

### ✅ Essential Files
- Source code in `src/`
- Tests in `tests/`
- Examples in `examples/`
- Documentation in `docs/`
- Data files in `data/` (BPARules.json)
- `requirements.txt`
- `README.md`
- `run_web_interface.py`
- `run_analyzer.py`
- `config_template.py` (template only, not actual config)

### ✅ Folder Structure
- Empty folders are preserved with `.gitkeep` files
- `reports/.gitkeep` ensures reports folder exists

## Setup for New Users

When someone clones the repository:

1. **Create virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create config file (for AI features):**
   ```bash
   copy config_template.py src\config.py  # Windows
   cp config_template.py src/config.py    # Linux/Mac
   
   # Edit src/config.py and add OpenAI API key
   ```

4. **Run the tool:**
   ```bash
   python run_web_interface.py
   ```

## Why These Patterns?

### `src/config.py` is Ignored
- Contains sensitive OpenAI API key
- Each user creates their own from `config_template.py`
- Never commit API keys to git!

### Reports are Ignored
- Generated files, not source code
- Can be recreated by running analysis
- Keeps repository clean
- Users generate their own reports

### Virtual Environments are Ignored
- Large folder (~100MB+)
- Each user creates their own
- Dependencies tracked in `requirements.txt`

### Cache Folders are Ignored
- Temporary Python compilation
- Regenerated automatically
- Different on each machine

## Committing Changes

### Safe to Commit ✅
- Source code changes in `src/`
- New tests in `tests/`
- Documentation updates in `docs/`
- New examples in `examples/`
- Updates to `requirements.txt`
- Updates to `BPARules.json`

### Never Commit ❌
- `src/config.py` with API keys
- Virtual environment folders
- Generated reports
- Cache folders
- IDE settings (unless shared)
- Personal configurations

## Checking What's Ignored

View ignored files:
```bash
git status --ignored
```

Check if a file is ignored:
```bash
git check-ignore -v filename
```

List all tracked files:
```bash
git ls-files
```

## Best Practices

1. **Before committing:**
   ```bash
   # Check status
   git status
   
   # Make sure config.py is not staged
   git status | grep config.py
   ```

2. **If you accidentally staged config.py:**
   ```bash
   git reset HEAD src/config.py
   ```

3. **To remove config.py if already committed:**
   ```bash
   git rm --cached src/config.py
   git commit -m "Remove config.py from tracking"
   ```

## Summary

✅ `.gitignore` updated for new structure  
✅ Sensitive files protected (config.py)  
✅ Generated files ignored (reports)  
✅ Development files ignored (cache, .venv)  
✅ Folder structure preserved (.gitkeep)  
✅ Clean repository  

Your repository is now properly configured for collaborative development! 🎉
