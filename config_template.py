# Configuration file for TMDL Analyzer
# Copy this to config.py and add your API keys

# OpenAI Configuration (Optional - for AI-enhanced features)
# Get your API key from: https://platform.openai.com/api-keys
OPENAI_API_KEY = "your-openai-api-key-here"

# Alternative: Set as environment variable
# On Windows: setx OPENAI_API_KEY "your-api-key-here"
# On Linux/Mac: export OPENAI_API_KEY="your-api-key-here"

# Model Configuration
OPENAI_MODEL = "gpt-4"  # or "gpt-3.5-turbo" for lower cost
MAX_TOKENS = 300
TEMPERATURE = 0.3

# Analysis Settings
ENABLE_AI_EXPLANATIONS = True
ENABLE_AI_RECOMMENDATIONS = True
ENABLE_DAX_ANALYSIS = True

# File Paths
RULES_FILE = "BPARules.json"
DEFAULT_OUTPUT_DIR = "reports"