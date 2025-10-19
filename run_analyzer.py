"""
TMDL Best Practices Analyzer - Command Line Interface

Run this script to analyze a Power BI TMDL model from the command line.

Usage:
    python run_analyzer.py <path_to_semantic_model> [--ai] [--output report.md]

Examples:
    python run_analyzer.py "Sales Dashboard.SemanticModel"
    python run_analyzer.py "Sales Dashboard.SemanticModel" --ai
    python run_analyzer.py "Sales Dashboard.SemanticModel" --output my_report.md
"""

import sys
import argparse
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_path))

from tmdl_analyzer import TMDLBestPracticesAgent

# Try to import AI analyzer
try:
    from ai_enhanced_analyzer import AIEnhancedTMDLAnalyzer
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False


def main():
    parser = argparse.ArgumentParser(
        description='Analyze Power BI TMDL files against best practices',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_analyzer.py "Sales Dashboard.SemanticModel"
  python run_analyzer.py "Sales Dashboard.SemanticModel" --ai
  python run_analyzer.py "Sales Dashboard.SemanticModel" --output reports/my_report.md
        """
    )
    
    parser.add_argument('model_path', help='Path to the .SemanticModel folder')
    parser.add_argument('--ai', action='store_true', help='Use AI-enhanced analysis (requires OpenAI API key)')
    parser.add_argument('--output', '-o', help='Output report file path (default: reports/analysis_report.md)')
    
    args = parser.parse_args()
    
    # Get rules file path
    project_root = Path(__file__).parent
    rules_file = str(project_root / 'data' / 'BPARules.json')
    
    if not Path(rules_file).exists():
        print(f"Error: BPARules.json not found at {rules_file}")
        return 1
    
    # Create analyzer
    if args.ai:
        if not AI_AVAILABLE:
            print("Error: AI-enhanced analyzer not available.")
            print("Please install required dependencies and configure OpenAI API key.")
            return 1
        print("Using AI-Enhanced Analyzer...")
        analyzer = AIEnhancedTMDLAnalyzer(rules_file)
    else:
        print("Using Regular Analyzer...")
        analyzer = TMDLBestPracticesAgent(rules_file)
    
    # Run analysis
    print(f"Analyzing model: {args.model_path}")
    try:
        result = analyzer.analyze_model(args.model_path)
    except Exception as e:
        print(f"Error analyzing model: {e}")
        return 1
    
    # Print summary
    print("\n" + "=" * 60)
    print("Analysis Complete!")
    print("=" * 60)
    print(f"Tables: {result['summary']['object_counts']['tables']}")
    print(f"Measures: {result['summary']['object_counts']['measures']}")
    print(f"Columns: {result['summary']['object_counts']['columns']}")
    print(f"Relationships: {result['summary']['object_counts']['relationships']}")
    print(f"\nTotal Violations: {result['summary']['violations']['total']}")
    print("\nBy Severity:")
    for severity, count in result['summary']['violations']['by_severity'].items():
        print(f"  {severity}: {count}")
    
    # Generate report
    output_path = args.output or str(project_root / 'reports' / 'analysis_report.md')
    print(f"\nGenerating report: {output_path}")
    
    try:
        analyzer.generate_report(
            result,
            output_path,
            include_summary=True,
            include_objects=True
        )
        print(f"✅ Report saved to: {output_path}")
    except Exception as e:
        print(f"Warning: Could not generate report: {e}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
