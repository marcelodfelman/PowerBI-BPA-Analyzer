"""
Example: Using TMDL Analyzer with OpenAI Integration

This example shows how to use the enhanced analyzer with OpenAI features.
"""

import os
from ai_enhanced_analyzer import AIEnhancedTMDLAnalyzer

def main():
    print("🤖 TMDL Analyzer with OpenAI Integration")
    print("=" * 50)
    
    # Check if API key is available
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("ℹ️  No OpenAI API key found.")
        print("   The analyzer will work with standard features.")
        print("   To enable AI features:")
        print("   1. Get API key from: https://platform.openai.com/api-keys")
        print("   2. Set environment variable: OPENAI_API_KEY=your-key")
        print("   3. Or pass it directly to the analyzer")
        print()
        
        # Option to enter API key manually for demo
        user_key = input("Enter your OpenAI API key (or press Enter to continue without AI): ").strip()
        if user_key:
            api_key = user_key
    
    # Create enhanced analyzer
    print("🔧 Creating enhanced analyzer...")
    analyzer = AIEnhancedTMDLAnalyzer("BPARules.json", api_key)
    
    if analyzer.ai_enabled:
        print("✅ AI features enabled!")
    else:
        print("⚠️  AI features disabled - using standard analysis")
    
    # Run analysis
    model_path = "Sales Dashboard.SemanticModel"
    print(f"\n📂 Analyzing model: {model_path}")
    
    result = analyzer.analyze_model(model_path)
    violations = result['violations']
    
    print(f"\n📊 Found {len(violations)} violations")
    
    if analyzer.ai_enabled and violations:
        print("\n🤖 Getting AI-powered insights...")
        
        # Get strategic recommendations
        print("\n" + "="*50)
        print("🎯 AI STRATEGIC RECOMMENDATIONS")
        print("="*50)
        recommendations = analyzer.get_ai_recommendations(violations)
        print(recommendations)
        
        # Show AI explanations for top violations
        print("\n" + "="*50)
        print("💡 AI-ENHANCED EXPLANATIONS")
        print("="*50)
        
        # Group violations by rule to avoid duplicates
        unique_violations = {}
        for v in violations:
            if v.rule_name not in unique_violations:
                unique_violations[v.rule_name] = v
        
        # Show top 3 most common violations with AI explanations
        for i, (rule_name, violation) in enumerate(list(unique_violations.items())[:3], 1):
            print(f"\n{i}. {violation.rule_name}")
            print("-" * 40)
            
            # Get enhanced explanation
            explanation = analyzer.get_ai_explanation(violation)
            print(explanation)
        
        # Analyze DAX patterns for measures with violations
        print("\n" + "="*50)
        print("⚡ DAX PATTERN ANALYSIS")
        print("="*50)
        
        measure_violations = [v for v in violations if v.object_type == 'Measure']
        if measure_violations:
            sample_violation = measure_violations[0]
            
            # Try to find the actual DAX code (simplified)
            # In a real implementation, you'd extract this from the parsed TMDL
            sample_dax = "SUM(Table[Column]) / SUM(Table[OtherColumn])"
            
            print(f"Analyzing DAX for: {sample_violation.object_name}")
            dax_analysis = analyzer.analyze_dax_pattern(sample_dax)
            print(dax_analysis)
        
    else:
        print("\n📋 Standard Analysis Complete")
        print("💡 For AI-enhanced insights, add your OpenAI API key")
    
    print(f"\n✨ Analysis complete!")
    print(f"📄 Full report available in generated files")

if __name__ == "__main__":
    main()