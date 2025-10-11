"""
Enhanced TMDL Analyzer with OpenAI integration for smarter recommendations

This extends the base analyzer with AI-powered explanations and suggestions.
"""

import os
from openai import OpenAI
from typing import List, Optional
from tmdl_analyzer import TMDLBestPracticesAgent, Violation
import json

# Try to import config file
try:
    import config
    DEFAULT_API_KEY = getattr(config, 'OPENAI_API_KEY', None)
    DEFAULT_MODEL = getattr(config, 'OPENAI_MODEL', 'gpt-4')
    DEFAULT_MAX_TOKENS = getattr(config, 'MAX_TOKENS', 300)
    DEFAULT_TEMPERATURE = getattr(config, 'TEMPERATURE', 0.3)
except ImportError:
    DEFAULT_API_KEY = None
    DEFAULT_MODEL = 'gpt-4'
    DEFAULT_MAX_TOKENS = 300
    DEFAULT_TEMPERATURE = 0.3

class AIEnhancedTMDLAnalyzer(TMDLBestPracticesAgent):
    """Enhanced analyzer with OpenAI integration"""
    
    def __init__(self, rules_file: str, openai_api_key: Optional[str] = None):
        super().__init__(rules_file)
        
        # Set up OpenAI API key - priority: parameter > config.py > environment variable
        api_key = None
        if openai_api_key:
            api_key = openai_api_key
        elif DEFAULT_API_KEY:
            api_key = DEFAULT_API_KEY
        else:
            # Try to get from environment variable
            api_key = os.getenv('OPENAI_API_KEY')
        
        if not api_key:
            self.logger.warning("OpenAI API key not provided. AI-enhanced features will be disabled.")
            self.ai_enabled = False
            self.client = None
        else:
            self.ai_enabled = True
            # Create client with timeout settings
            self.client = OpenAI(
                api_key=api_key,
                timeout=30.0,  # 30 second timeout
                max_retries=2
            )
            self.logger.info("OpenAI API key found. AI-enhanced features are enabled.")
        
        # Set model configuration
        self.model = DEFAULT_MODEL
        self.max_tokens = DEFAULT_MAX_TOKENS
        self.temperature = DEFAULT_TEMPERATURE
    
    def analyze_model(self, model_path: str):
        """Override to add AI enhancements to the analysis"""
        # First, run the standard analysis
        result = super().analyze_model(model_path)
        
        # If AI is not enabled, return standard result
        if not self.ai_enabled:
            self.logger.info("AI features disabled - returning standard analysis")
            return result
        
        self.logger.info("Enhancing analysis with AI-powered insights...")
        
        # Add AI enhancements to violations (limit to first 5 to avoid timeouts)
        enhanced_violations = []
        violations_to_enhance = min(5, len(result['violations']))
        
        self.logger.info(f"Enhancing {violations_to_enhance} violations with AI explanations...")
        
        for i, violation in enumerate(result['violations']):
            # Only enhance first few violations to avoid long wait times
            if i < violations_to_enhance:
                try:
                    # Find the original object to get DAX code if it's a measure
                    dax_code = ""
                    for measure in result['objects'].get('measures', []):
                        if measure.name == violation.object_name:
                            dax_code = getattr(measure, 'expression', '')
                            break
                    
                    # Get AI explanation
                    self.logger.info(f"  Enhancing {i+1}/{violations_to_enhance}: {violation.object_name}...")
                    ai_explanation = self.get_ai_explanation(violation, dax_code)
                    
                    # Create enhanced violation with AI explanation
                    # Store AI explanation in the violation object's properties
                    violation.properties = getattr(violation, 'properties', {})
                    violation.properties['ai_explanation'] = ai_explanation
                    violation.properties['ai_enhanced'] = True
                    
                except Exception as e:
                    self.logger.warning(f"Could not enhance violation {violation.object_name}: {e}")
                    violation.properties = getattr(violation, 'properties', {})
                    violation.properties['ai_enhanced'] = False
            else:
                # Don't enhance remaining violations to save time/cost
                violation.properties = getattr(violation, 'properties', {})
                violation.properties['ai_enhanced'] = False
            
            enhanced_violations.append(violation)
        
        # Replace violations with enhanced ones
        result['violations'] = enhanced_violations
        
        # Add strategic recommendations
        try:
            self.logger.info("Generating strategic recommendations...")
            recommendations = self.get_ai_recommendations(enhanced_violations[:10])  # Limit summary to 10 violations
            result['ai_recommendations'] = recommendations
            result['ai_enhanced'] = True
            self.logger.info("Strategic recommendations generated successfully!")
        except Exception as e:
            self.logger.error(f"Could not generate strategic recommendations: {e}")
            import traceback
            self.logger.error(traceback.format_exc())
            result['ai_recommendations'] = f"Unable to generate recommendations: {str(e)}"
            result['ai_enhanced'] = False
        
        self.logger.info("AI enhancement complete!")
        return result
    
    def get_ai_explanation(self, violation: Violation, dax_code: str = "") -> str:
        """Get AI-powered explanation for a violation"""
        if not self.ai_enabled:
            return violation.description
        
        try:
            prompt = f"""
            As a Power BI and DAX expert, explain this best practice violation in simple terms:
            
            Rule: {violation.rule_name}
            Object: {violation.object_name} ({violation.object_type})
            Category: {violation.category}
            Severity: {violation.severity.name}
            
            Original Description: {violation.description}
            
            {f"DAX Code: {dax_code}" if dax_code else ""}
            
            Please provide:
            1. Why this is a problem (in simple terms)
            2. What impact it has on performance/functionality
            3. A specific step-by-step fix recommendation
            4. Best practice alternative
            
            Keep it concise but actionable.
            """
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a Power BI and DAX expert who explains technical concepts clearly."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            self.logger.error(f"Error getting AI explanation: {e}")
            return violation.description
    
    def get_ai_recommendations(self, violations: List[Violation]) -> str:
        """Get AI-powered overall recommendations"""
        if not self.ai_enabled or not violations:
            return "No AI-powered recommendations available."
        
        try:
            # Summarize violations for AI
            violation_summary = {}
            for v in violations:
                category = v.category
                if category not in violation_summary:
                    violation_summary[category] = []
                violation_summary[category].append({
                    'rule': v.rule_name,
                    'severity': v.severity.name,
                    'object': v.object_name
                })
            
            prompt = f"""
            As a Power BI expert, analyze this model's violations and provide strategic recommendations:
            
            Violation Summary:
            {json.dumps(violation_summary, indent=2)}
            
            Total Violations: {len(violations)}
            
            Please provide:
            1. Top 3 priority areas to focus on
            2. Estimated impact of fixing these issues
            3. Recommended order of implementation
            4. Any patterns you notice that suggest architectural improvements
            
            Be specific and actionable.
            """
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a senior Power BI consultant providing strategic guidance."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=min(self.max_tokens + 100, 500),  # Allow slightly more tokens for recommendations
                temperature=self.temperature
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            self.logger.error(f"Error getting AI recommendations: {e}")
            return "Unable to generate AI recommendations at this time."
    
    def analyze_dax_pattern(self, dax_expression: str) -> str:
        """Analyze DAX expression for patterns and suggestions"""
        if not self.ai_enabled:
            return ""
        
        try:
            prompt = f"""
            Analyze this DAX expression for best practices and optimization opportunities:
            
            ```dax
            {dax_expression}
            ```
            
            Check for:
            1. Performance optimization opportunities
            2. Readability improvements
            3. Best practice violations
            4. Potential errors or edge cases
            
            Provide specific, actionable suggestions.
            """
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a DAX expert focused on performance and best practices."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            self.logger.error(f"Error analyzing DAX: {e}")
            return ""

# Example usage function
def create_enhanced_analyzer(api_key: str = None) -> AIEnhancedTMDLAnalyzer:
    """Factory function to create enhanced analyzer"""
    rules_file = "BPARules.json"
    
    # Get API key from parameter, environment, or prompt user
    if not api_key:
        api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("OpenAI API key is required for enhanced features.")
        print("You can:")
        print("1. Set OPENAI_API_KEY environment variable")
        print("2. Pass api_key parameter to this function")
        print("3. The analyzer will work without AI features")
    
    return AIEnhancedTMDLAnalyzer(rules_file, api_key)

if __name__ == "__main__":
    # Example usage
    analyzer = create_enhanced_analyzer()
    
    model_path = "Sales Dashboard.SemanticModel"
    result = analyzer.analyze_model(model_path)
    
    print("🤖 AI-Enhanced Analysis Complete!")
    
    # Get AI recommendations
    if analyzer.ai_enabled:
        print("\n🎯 AI Strategic Recommendations:")
        print("-" * 40)
        recommendations = analyzer.get_ai_recommendations(result['violations'])
        print(recommendations)
        
        # Show AI explanation for first few violations
        print("\n💡 AI-Enhanced Explanations:")
        print("-" * 40)
        for violation in result['violations'][:3]:
            print(f"\n{violation.rule_name}:")
            explanation = analyzer.get_ai_explanation(violation)
            print(explanation)
    else:
        print("ℹ️ AI features disabled - no API key provided")