#!/usr/bin/env python3
"""Quick test of AI-enhanced analyzer to verify AI enhancements are working"""

from ai_enhanced_analyzer import AIEnhancedTMDLAnalyzer
import sys

def test_ai_enhancements():
    """Test that AI enhancements are being applied"""
    
    print("="*70)
    print("Testing AI-Enhanced Analyzer")
    print("="*70)
    
    try:
        # Initialize the analyzer
        print("\n1. Initializing AI-Enhanced Analyzer...")
        analyzer = AIEnhancedTMDLAnalyzer('BPARules.json')
        
        if not analyzer.ai_enabled:
            print("❌ AI features are disabled. Cannot test enhancements.")
            return False
        
        print("✅ AI features enabled")
        
        # Run analysis on the sample model
        print("\n2. Running analysis on sample model...")
        model_path = r'C:\Users\marce\Downloads\PBIP File\Sales Dashboard.SemanticModel'
        
        results = analyzer.analyze_model(model_path)
        
        print(f"\n3. Analysis Results:")
        print(f"   - Total violations: {len(results['violations'])}")
        print(f"   - AI Enhanced: {results.get('ai_enhanced', False)}")
        
        # Check for AI enhancements
        ai_enhanced_count = 0
        has_ai_recommendations = bool(results.get('ai_recommendations'))
        
        for v in results['violations']:
            if hasattr(v, 'properties') and v.properties.get('ai_enhanced'):
                ai_enhanced_count += 1
        
        print(f"   - Violations with AI explanations: {ai_enhanced_count}")
        print(f"   - Has strategic recommendations: {has_ai_recommendations}")
        
        # Show first AI-enhanced violation
        if ai_enhanced_count > 0:
            print(f"\n4. Sample AI Enhancement:")
            for v in results['violations']:
                if hasattr(v, 'properties') and v.properties.get('ai_explanation'):
                    print(f"   Rule: {v.rule_name}")
                    print(f"   Object: {v.object_name}")
                    print(f"   AI Explanation (first 200 chars):")
                    print(f"   {v.properties['ai_explanation'][:200]}...")
                    break
        
        # Show recommendations
        if has_ai_recommendations:
            print(f"\n5. Strategic Recommendations (first 300 chars):")
            print(f"   {results['ai_recommendations'][:300]}...")
        
        # Verdict
        print("\n" + "="*70)
        if ai_enhanced_count > 0 or has_ai_recommendations:
            print("✅ SUCCESS: AI enhancements are working!")
            print(f"   - {ai_enhanced_count} violations enhanced with AI explanations")
            print(f"   - Strategic recommendations: {'Yes' if has_ai_recommendations else 'No'}")
        else:
            print("❌ FAILURE: No AI enhancements found in results")
            print("   - Violations have no AI explanations")
            print("   - No strategic recommendations")
        print("="*70)
        
        return ai_enhanced_count > 0 or has_ai_recommendations
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_ai_enhancements()
    sys.exit(0 if success else 1)
