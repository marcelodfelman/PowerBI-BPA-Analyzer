# OpenAI API Configuration Guide

## Where to Put Your OpenAI API Key

The TMDL Analyzer currently works **without** OpenAI, but you can enhance it with AI features. Here's how to add your OpenAI API key:

### Option 1: Environment Variable (Recommended)

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY = "your-api-key-here"
```

**Windows (Command Prompt):**
```cmd
setx OPENAI_API_KEY "your-api-key-here"
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### Option 2: Configuration File

1. Copy `config_template.py` to `config.py`
2. Edit the line: `OPENAI_API_KEY = "your-openai-api-key-here"`
3. Replace with your actual API key

### Option 3: Direct in Code

```python
from ai_enhanced_analyzer import AIEnhancedTMDLAnalyzer

analyzer = AIEnhancedTMDLAnalyzer(
    rules_file="BPARules.json",
    openai_api_key="your-api-key-here"
)
```

### Getting an OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)
5. Keep it secure - don't share it!

## How to Use AI-Enhanced Features

Once you have your API key set up, follow these steps:

### Step 1: Verify Your Setup

```bash
# Quick test to see if AI is working
python quick_start_ai.py
```

You should see: `✅ AI features enabled!`

### Step 2: Choose Your Method

**Method A: Use the Example Script**
```bash
python example_with_openai.py
```

**Method B: Command Line with Standard Analyzer**
```bash
# Standard analyzer (no AI)
python tmdl_analyzer.py "YourModel.SemanticModel"

# For AI features, use the enhanced version
python quick_start_ai.py
```

**Method C: Import in Your Own Code**
```python
from ai_enhanced_analyzer import AIEnhancedTMDLAnalyzer

# Create enhanced analyzer
analyzer = AIEnhancedTMDLAnalyzer("BPARules.json")

# Check if AI is enabled
if analyzer.ai_enabled:
    print("🤖 AI features available!")
    
    # Run analysis
    result = analyzer.analyze_model("YourModel.SemanticModel")
    
    # Get AI recommendations
    recommendations = analyzer.get_ai_recommendations(result['violations'])
    print(recommendations)
    
    # Get enhanced explanations
    for violation in result['violations'][:3]:
        explanation = analyzer.get_ai_explanation(violation)
        print(f"💡 {violation.rule_name}: {explanation}")
else:
    print("❌ AI features not available - check your API key")
```

### Step 3: What You Get

When AI is enabled, you'll receive:

1. **🎯 Strategic Recommendations**
   - High-level improvement strategies
   - Priority areas to focus on
   - Implementation roadmap

2. **💡 Enhanced Explanations**
   - Context-aware violation explanations
   - Why each issue matters
   - Step-by-step fix instructions

3. **⚡ DAX Analysis**
   - Intelligent pattern detection
   - Performance optimization tips
   - Code quality improvements

### Troubleshooting AI Setup

**Problem: "AI features not available"**
- Check API key is set: `echo $env:OPENAI_API_KEY`
- Verify key starts with `sk-`
- Check internet connection
- Verify OpenAI account has credits

**Problem: "API key not found"**
```powershell
# Set the key in current session
$env:OPENAI_API_KEY = "sk-your-key-here"

# Or set permanently
setx OPENAI_API_KEY "sk-your-key-here"
```

**Problem: API errors**
- Check your OpenAI account has sufficient credits
- Verify the API key is active
- Try again in a few minutes (rate limiting)

### Cost Considerations

- GPT-4: ~$0.03 per 1K tokens (more accurate)
- GPT-3.5-turbo: ~$0.002 per 1K tokens (cheaper)
- Typical analysis: $0.10 - $0.50 depending on model size

### AI Features Available

When you add an API key, you get:

🤖 **Enhanced Explanations**: Detailed, context-aware violation explanations
📊 **Strategic Recommendations**: High-level improvement strategies  
⚡ **DAX Analysis**: Smart pattern detection in DAX expressions
💡 **Custom Fixes**: Specific, actionable fix suggestions

### Current Status

✅ **Working Now**: Rule-based analysis (no API key needed)
🔄 **Optional**: AI-enhanced features (requires API key)

The analyzer is fully functional without OpenAI - the AI features are just bonus enhancements!