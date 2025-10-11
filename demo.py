"""
Demo script showing how to use the TMDL Best Practices Analyzer Agent

This script demonstrates various ways to use the analyzer:
1. Basic analysis with default settings
2. Analyzing specific rule categories
3. Filtering results by severity
4. Generating custom reports
"""

from tmdl_analyzer import TMDLBestPracticesAgent, Severity
import os

def main():
    print("🔍 TMDL Best Practices Analyzer - Demo")
    print("=" * 50)
    
    # Configuration
    model_path = "Sales Dashboard.SemanticModel"
    rules_file = "BPARules.json"
    
    # Check if files exist
    if not os.path.exists(model_path):
        print(f"❌ Model not found: {model_path}")
        return
    
    if not os.path.exists(rules_file):
        print(f"❌ Rules file not found: {rules_file}")
        return
    
    print(f"📂 Analyzing model: {model_path}")
    print(f"📋 Using rules from: {rules_file}")
    print()
    
    # Create the analyzer agent
    agent = TMDLBestPracticesAgent(rules_file)
    
    # Run the analysis
    print("🚀 Running analysis...")
    result = agent.analyze_model(model_path)
    
    # Display summary
    print("\n📊 Analysis Summary")
    print("-" * 30)
    summary = result['summary']
    print(f"Tables: {summary['object_counts']['tables']}")
    print(f"Measures: {summary['object_counts']['measures']}")
    print(f"Columns: {summary['object_counts']['columns']}")
    print(f"Relationships: {summary['object_counts']['relationships']}")
    print(f"Total Violations: {summary['violations']['total']}")
    
    # Display violations by severity
    print("\n⚠️ Violations by Severity")
    print("-" * 30)
    for severity, count in summary['violations']['by_severity'].items():
        emoji = "🚨" if severity == "ERROR" else "⚠️" if severity == "WARNING" else "ℹ️"
        print(f"{emoji} {severity}: {count}")
    
    # Display violations by category
    print("\n📋 Violations by Category")
    print("-" * 30)
    for category, count in summary['violations']['by_category'].items():
        print(f"• {category}: {count}")
    
    # Show top 5 most common violations
    print("\n🔝 Top 5 Most Common Violations")
    print("-" * 30)
    violation_counts = {}
    for violation in result['violations']:
        rule_name = violation.rule_name
        violation_counts[rule_name] = violation_counts.get(rule_name, 0) + 1
    
    top_violations = sorted(violation_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    for i, (rule_name, count) in enumerate(top_violations, 1):
        print(f"{i}. {rule_name}: {count} occurrences")
    
    # Show critical errors (severity = ERROR)
    critical_violations = [v for v in result['violations'] if v.severity == Severity.ERROR]
    if critical_violations:
        print(f"\n🚨 Critical Issues ({len(critical_violations)} errors)")
        print("-" * 30)
        for violation in critical_violations[:3]:  # Show first 3
            print(f"• {violation.object_name} ({violation.object_type})")
            print(f"  Rule: {violation.rule_name}")
            print(f"  File: {violation.file_path}")
            if violation.fix_suggestion:
                print(f"  Fix: {violation.fix_suggestion}")
            print()
    
    # Performance-related violations
    performance_violations = [v for v in result['violations'] if v.category == 'Performance']
    if performance_violations:
        print(f"\n⚡ Performance Issues ({len(performance_violations)} violations)")
        print("-" * 30)
        perf_rules = {}
        for violation in performance_violations:
            rule = violation.rule_name
            perf_rules[rule] = perf_rules.get(rule, 0) + 1
        
        for rule, count in sorted(perf_rules.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"• {rule}: {count} occurrences")
    
    # DAX-related violations
    dax_violations = [v for v in result['violations'] if v.category == 'DAX Expressions']
    if dax_violations:
        print(f"\n📝 DAX Expression Issues ({len(dax_violations)} violations)")
        print("-" * 30)
        
        # Show measures with DAX issues
        measures_with_issues = set()
        for violation in dax_violations:
            if violation.object_type == 'Measure':
                measures_with_issues.add(violation.object_name)
        
        print(f"Measures with DAX issues: {len(measures_with_issues)}")
        if measures_with_issues:
            print("Examples:")
            for measure in list(measures_with_issues)[:3]:
                print(f"  • {measure}")
    
    # Generate and save detailed report
    print(f"\n📄 Generating detailed report...")
    report_file = "demo_analysis_report.md"
    report_content = agent.generate_report(result, report_file)
    print(f"✅ Report saved to: {report_file}")
    
    # Show sample violations with fix suggestions
    violations_with_fixes = [v for v in result['violations'] if v.fix_suggestion]
    if violations_with_fixes:
        print(f"\n💡 Sample Fix Suggestions")
        print("-" * 30)
        for violation in violations_with_fixes[:3]:
            print(f"Issue: {violation.rule_name}")
            print(f"Object: {violation.object_name}")
            print(f"Fix: {violation.fix_suggestion}")
            print()
    
    # Summary and recommendations
    print("\n🎯 Recommendations")
    print("-" * 30)
    
    total_violations = len(result['violations'])
    if total_violations == 0:
        print("🎉 Excellent! No violations found. Your model follows best practices.")
    elif total_violations < 10:
        print("✅ Good! Only a few minor issues found. Quick fixes recommended.")
    elif total_violations < 50:
        print("⚠️ Several issues found. Focus on critical errors first.")
    else:
        print("🚨 Many issues found. Consider systematic refactoring.")
    
    # Priority recommendations
    error_count = len([v for v in result['violations'] if v.severity == Severity.ERROR])
    warning_count = len([v for v in result['violations'] if v.severity == Severity.WARNING])
    
    print("\nPriority order:")
    if error_count > 0:
        print(f"1. Fix {error_count} critical errors first")
    if warning_count > 0:
        print(f"2. Address {warning_count} warning-level issues")
    
    # Common quick wins
    quick_wins = [
        "Add format strings to measures",
        "Hide foreign key columns", 
        "Use DIVIDE instead of / operator",
        "Replace floating point data types"
    ]
    
    print("\nQuick wins to start with:")
    for i, win in enumerate(quick_wins, 1):
        print(f"{i}. {win}")
    
    print(f"\n✨ Analysis complete! Check {report_file} for full details.")

if __name__ == "__main__":
    main()