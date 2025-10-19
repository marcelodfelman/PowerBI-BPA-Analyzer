"""
Quick Start: AI-Enhanced TMDL Analysis

This script shows how to use the AI-enhanced analyzer with your API key.
"""

import os
from ai_enhanced_analyzer import AIEnhancedTMDLAnalyzer

def main():
    print("🚀 AI-Enhanced TMDL Analyzer - Quick Start")
    print("=" * 50)
    
    # Option 1: Use environment variable
    # $env:OPENAI_API_KEY = "sk-your-key-here"
    
    # Option 2: Use config file (config.py)
    # Copy config_template.py to config.py and add your key
    
    # Option 3: Set directly in code (not recommended for production)
    # api_key = "sk-your-key-here"
    # analyzer = AIEnhancedTMDLAnalyzer("BPARules.json", api_key)
    
    # Create analyzer (will auto-detect API key from environment or config)
    analyzer = AIEnhancedTMDLAnalyzer("BPARules.json")
    
    if not analyzer.ai_enabled:
        print("❌ AI features not available")
        print("💡 Set your OpenAI API key:")
        print("   $env:OPENAI_API_KEY = 'sk-your-key-here'")
        return
    
    print("✅ AI features enabled!")
    
    # Replace with your actual model path
    model_path = "YourModel.SemanticModel"
    
    # Check if model exists
    if not os.path.exists(model_path):
        print(f"⚠️  Model not found: {model_path}")
        print("💡 Update model_path with your actual .SemanticModel folder")
        return
    
    print(f"📂 Analyzing: {model_path}")
    
    # Run analysis
    result = analyzer.analyze_model(model_path)
    violations = result['violations']
    
    print(f"📊 Found {len(violations)} violations")
    
    if violations:
        print("\n🎯 AI STRATEGIC RECOMMENDATIONS")
        print("-" * 40)
        recommendations = analyzer.get_ai_recommendations(violations[:10])  # First 10
        print(recommendations)
        
        print("\n💡 AI-ENHANCED EXPLANATIONS")
        print("-" * 40)
        
        # Show AI explanations for first 3 unique violations
        unique_rules = set()
        for violation in violations:
            if violation.rule_name not in unique_rules and len(unique_rules) < 3:
                unique_rules.add(violation.rule_name)
                print(f"\n📋 {violation.rule_name}")
                print(f"Object: {violation.object_name}")
                explanation = analyzer.get_ai_explanation(violation)
                print(explanation)
                print("-" * 20)
    
    print("\n✨ AI-Enhanced analysis complete!")

if __name__ == "__main__":
    main()