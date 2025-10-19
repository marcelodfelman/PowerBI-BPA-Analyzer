"""
Enhanced TMDL Analyzer with OpenAI integration for smarter recommendations

This extends the base analyzer with AI-powered explanations and suggestions.
"""

import os
import sys
from pathlib import Path
from openai import OpenAI
from typing import List, Optional
import json

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent))

from tmdl_analyzer import TMDLBestPracticesAgent, Violation

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
        
        # Group violations by rule ID
        violations_by_rule = {}
        for violation in result['violations']:
            rule_id = violation.rule_id
            if rule_id not in violations_by_rule:
                violations_by_rule[rule_id] = []
            violations_by_rule[rule_id].append(violation)
        
        self.logger.info(f"Found {len(violations_by_rule)} unique violation types across {len(result['violations'])} total violations")
        
        # Get AI explanation for each rule type (not each violation)
        rule_explanations = {}
        rules_to_enhance = list(violations_by_rule.keys())
        
        self.logger.info(f"Enhancing {len(rules_to_enhance)} violation types with AI strategic guidance...")
        
        for i, rule_id in enumerate(rules_to_enhance):
            try:
                # Get sample violation for this rule
                sample_violation = violations_by_rule[rule_id][0]
                violation_count = len(violations_by_rule[rule_id])
                
                # Get example objects for this rule
                example_objects = [v.object_name for v in violations_by_rule[rule_id][:3]]
                
                # Find DAX code if applicable
                dax_examples = []
                for v in violations_by_rule[rule_id][:2]:  # Get 2 DAX examples max
                    for measure in result['objects'].get('measures', []):
                        if measure.name == v.object_name:
                            dax_examples.append(getattr(measure, 'expression', ''))
                            break
                
                # Get AI explanation for this rule type
                self.logger.info(f"  Enhancing rule {i+1}/{len(rules_to_enhance)}: {sample_violation.rule_name} ({violation_count} violations)...")
                ai_explanation = self.get_rule_explanation(
                    sample_violation, 
                    violation_count,
                    example_objects,
                    dax_examples
                )
                
                rule_explanations[rule_id] = ai_explanation
                
            except Exception as e:
                self.logger.warning(f"Could not enhance rule {rule_id}: {e}")
                rule_explanations[rule_id] = None
        
        # Apply AI explanations to all violations of each rule type
        enhanced_violations = []
        for violation in result['violations']:
            violation.properties = getattr(violation, 'properties', {})
            if violation.rule_id in rule_explanations and rule_explanations[violation.rule_id]:
                violation.properties['ai_explanation'] = rule_explanations[violation.rule_id]
                violation.properties['ai_enhanced'] = True
            else:
                violation.properties['ai_enhanced'] = False
            enhanced_violations.append(violation)
        
        # Replace violations with enhanced ones
        result['violations'] = enhanced_violations
        
        # Add strategic recommendations based on violation types
        try:
            self.logger.info("Generating strategic recommendations...")
            recommendations = self.get_ai_recommendations(violations_by_rule)
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
    
    
    def get_rule_explanation(self, violation: Violation, violation_count: int, 
                            example_objects: List[str], dax_examples: List[str] = None) -> str:
        """Get AI-powered explanation for a violation rule type"""
        if not self.ai_enabled:
            return violation.description
        
        try:
            # Build context about the violations
            examples_text = f"\n\nExample objects affected:\n" + "\n".join(f"- {obj}" for obj in example_objects)
            
            dax_text = ""
            if dax_examples and len(dax_examples) > 0:
                dax_text = f"\n\nExample DAX code:\n```dax\n{dax_examples[0][:500]}\n```"
            
            prompt = f"""
            As a Power BI and DAX expert, explain this best practice rule that has {violation_count} violations:
            
            Rule: {violation.rule_name}
            Category: {violation.category}
            Severity: {violation.severity.name}
            
            Standard Description: {violation.description}
            {examples_text}
            {dax_text}
            
            Please provide a comprehensive explanation for ALL {violation_count} violations of this rule:
            
            1. **Why This Matters**: Explain the core issue and why this rule exists
            2. **Impact**: What are the performance/functionality/maintenance impacts
            3. **How to Fix**: Step-by-step approach to fix ALL violations of this type
            4. **Best Practice**: What's the recommended pattern to follow going forward
            5. **Priority**: Given {violation_count} violations, how urgent is this fix
            
            Make it actionable and specific to fixing all violations at once, not just one.
            """
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a Power BI and DAX expert who explains technical concepts clearly and provides strategic guidance."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=min(self.max_tokens + 200, 600),  # Allow more tokens for rule-level explanations
                temperature=self.temperature
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            self.logger.error(f"Error getting AI rule explanation: {e}")
            return violation.description
    
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
    
    
    def get_ai_recommendations(self, violations_by_rule: dict) -> str:
        """Get AI-powered overall recommendations based on violation types"""
        if not self.ai_enabled or not violations_by_rule:
            return "No AI-powered recommendations available."
        
        try:
            # Summarize violation types (not individual violations)
            violation_summary = []
            total_violations = 0
            
            for rule_id, violations in violations_by_rule.items():
                sample = violations[0]
                count = len(violations)
                total_violations += count
                
                violation_summary.append({
                    'rule_id': rule_id,
                    'rule_name': sample.rule_name,
                    'category': sample.category,
                    'severity': sample.severity.name,
                    'count': count,
                    'example_objects': [v.object_name for v in violations[:3]]
                })
            
            # Sort by count (most violations first) and severity
            violation_summary.sort(key=lambda x: (-x['count'], x['severity']))
            
            prompt = f"""
            As a Power BI expert consultant, analyze this model's best practice violations and provide strategic recommendations.
            
            Model has {total_violations} total violations across {len(violations_by_rule)} rule types:
            
            {json.dumps(violation_summary, indent=2)}
            
            Please provide:
            
            1. **Top 3 Priority Areas**: Which violation types should be fixed first and why?
               - Consider severity, count, and impact
               - Be specific about which rules to tackle
            
            2. **Implementation Strategy**: What's the best order to fix these?
               - Group related fixes together
               - Identify quick wins vs. larger refactoring
            
            3. **Expected Impact**: What benefits will fixing each area bring?
               - Performance improvements
               - Maintainability gains
               - Risk reduction
            
            4. **Effort Estimation**: Rough time estimates for fixing each violation type
               - Which are bulk operations?
               - Which require careful analysis?
            
            5. **Root Cause Patterns**: Do you see any systemic issues?
               - Are there modeling patterns that should change?
               - Architectural improvements to consider?
            
            Be specific, actionable, and reference actual rule names and counts.
            """
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a senior Power BI consultant providing strategic guidance on model optimization."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800,  # Longer response for strategic recommendations
                temperature=self.temperature
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            self.logger.error(f"Error getting AI recommendations: {e}")
            return "Unable to generate AI recommendations at this time."
    
    def get_ai_explanation_old(self, violations: List[Violation]) -> str:
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
    print(f"Found {len(result['violations'])} total violations")
    
    # Show AI recommendations
    if analyzer.ai_enabled and 'ai_recommendations' in result:
        print("\n🎯 AI Strategic Recommendations:")
        print("-" * 80)
        print(result['ai_recommendations'])
        
        # Show enhanced violations by rule type
        print("\n💡 AI-Enhanced Rule Explanations:")
        print("-" * 80)
        
        # Group violations by rule to show AI explanations
        violations_by_rule = {}
        for v in result['violations']:
            if v.rule_id not in violations_by_rule:
                violations_by_rule[v.rule_id] = []
            violations_by_rule[v.rule_id].append(v)
        
        for rule_id, violations in violations_by_rule.items():
            sample = violations[0]
            if sample.properties.get('ai_enhanced'):
                print(f"\n📋 {sample.rule_name} ({len(violations)} violations)")
                print(sample.properties.get('ai_explanation', 'No explanation available'))
                print()
    else:
        print("ℹ️ AI features disabled - no API key provided")
