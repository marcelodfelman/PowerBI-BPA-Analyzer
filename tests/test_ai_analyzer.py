#!/usr/bin/env python3
"""Test script to verify AI-enhanced analyzer configuration"""

from ai_enhanced_analyzer import AIEnhancedTMDLAnalyzer
import sys

def test_ai_configuration():
    """Test if AI-enhanced analyzer is properly configured"""
    
    print("="*60)
    print("AI-Enhanced Analyzer Configuration Test")
    print("="*60)
    
    try:
        # Initialize the analyzer
        print("\n1. Initializing AI-Enhanced Analyzer...")
        analyzer = AIEnhancedTMDLAnalyzer('BPARules.json')
        
        # Check if AI is enabled
        print(f"\n2. AI Features Status: {'✅ ENABLED' if analyzer.ai_enabled else '❌ DISABLED'}")
        
        if analyzer.ai_enabled:
            print(f"   - Model: {analyzer.model}")
            print(f"   - Max Tokens: {analyzer.max_tokens}")
            print(f"   - Temperature: {analyzer.temperature}")
            print("\n✅ Configuration loaded successfully from config.py")
        else:
            print("\n❌ AI features are disabled. Check your configuration:")
            print("   1. Ensure config.py exists")
            print("   2. Verify OPENAI_API_KEY is set in config.py")
            print("   3. Or set OPENAI_API_KEY environment variable")
            return False
        
        # Test with a small model (optional - comment out to avoid API calls)
        print("\n3. Testing AI API connection...")
        print("   (Skipping actual API call to avoid charges)")
        print("   To test API connection, uncomment the code in test_ai_analyzer.py")
        
        # Uncomment below to test actual API call:
        # from tmdl_analyzer import Violation, Severity
        # test_violation = Violation(
        #     rule_id="TEST",
        #     rule_name="Test Rule",
        #     category="Performance",
        #     severity=Severity.WARNING,
        #     description="Test description",
        #     object_name="TestObject",
        #     object_type="Measure",
        #     file_path="test.tmdl",
        #     fix_suggestion="Test fix"
        # )
        # explanation = analyzer.get_ai_explanation(test_violation)
        # print(f"\n   AI Response: {explanation[:100]}...")
        
        print("\n" + "="*60)
        print("✅ All tests passed! AI-enhanced analyzer is ready to use.")
        print("="*60)
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_ai_configuration()
    sys.exit(0 if success else 1)
