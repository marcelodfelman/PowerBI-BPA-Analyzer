# TMDL Analyzer - Troubleshooting Guide

## Web Interface Upload Issues

### Problem: "No valid TMDL model found" Error

**What you need:**
1. A folder ending with `.SemanticModel` (e.g., "MyModel.SemanticModel")
2. Inside that folder, a `definition` subfolder
3. Inside `definition`, TMDL files like:
   - `model.tmdl`
   - `relationships.tmdl`
   - `tables/` folder with `.tmdl` files

**Expected Folder Structure:**
```
Your Model.SemanticModel/
├── definition/
│   ├── model.tmdl
│   ├── relationships.tmdl
│   ├── tables/
│   │   ├── Table1.tmdl
│   │   ├── Table2.tmdl
│   │   └── ...
│   └── cultures/
│       └── ...
├── diagramLayout.json
└── definition.pbism
```

### How to Upload Correctly

**Method 1: From Power BI Desktop**
1. In Power BI Desktop, go to File → Export → Export Model → TMDL
2. Choose a folder location
3. This creates a `.SemanticModel` folder
4. Upload this entire folder to the web interface

**Method 2: From Existing PBIP Project**
1. Look for a folder ending in `.SemanticModel`
2. Make sure it has a `definition` subfolder
3. Select this folder when uploading

**Method 3: Manual Check**
1. Open your folder in File Explorer
2. Verify you see: `YourModel.SemanticModel/definition/`
3. Inside `definition/` you should see TMDL files

### Common Issues

❌ **Wrong Folder Selected**
- Selected parent folder instead of `.SemanticModel` folder
- Selected `definition` folder directly

✅ **Correct Folder**
- Selected the `.SemanticModel` folder itself

❌ **Missing Files**
- Folder exists but no TMDL files inside
- Corrupted export from Power BI

✅ **Complete Structure**
- All TMDL files present in correct locations

### Browser-Specific Issues

**Chrome/Edge:**
- Click "Choose Directory" 
- Navigate to and select your `.SemanticModel` folder
- Browser will upload all files with correct paths

**Firefox:**
- May handle directory upload differently
- Try using Chrome/Edge if issues persist

### Command Line Testing

Test your folder structure before using web interface:

```bash
# Navigate to the folder containing your .SemanticModel directory
cd "C:\Path\To\Your\Folder"

# List contents - you should see YourModel.SemanticModel/
dir

# Test the analyzer
python tmdl_analyzer.py "YourModel.SemanticModel"
```

### Getting Your TMDL Files

**From Power BI Desktop (.pbix):**
1. Open your .pbix file
2. File → Export → Export Model → TMDL
3. Choose destination folder
4. Creates `ModelName.SemanticModel` folder

**From PBIP Project:**
1. Look for existing `.SemanticModel` folder
2. Should be alongside your `.Report` folder

**From Analysis Services:**
1. Use SQL Server Management Studio
2. Right-click database → Script Database as → TMDL

### Still Having Issues?

1. **Check File Permissions**: Make sure you can read the files
2. **Check File Encoding**: TMDL files should be UTF-8
3. **Check for Hidden Files**: Enable showing hidden files in Windows
4. **Try Command Line First**: Test with command line before web interface
5. **Check Browser Console**: Open Developer Tools to see JavaScript errors

### Debug Information

The analyzer will show you the uploaded structure if there's an error. Look for:
- 📁 Folder names ending with `/`
- 📄 Individual file names
- Missing `definition/` folder
- Missing TMDL files in `tables/` folder

Example good structure:
```
YourModel.SemanticModel/
├── 📁 definition/
│   ├── 📄 model.tmdl
│   ├── 📄 relationships.tmdl
│   └── 📁 tables/
│       ├── 📄 Table1.tmdl
│       └── 📄 Table2.tmdl
```

Example bad structure:
```
SomeFolder/
├── 📄 random_file.txt
└── 📁 other_folder/
    └── 📄 not_tmdl.file
```