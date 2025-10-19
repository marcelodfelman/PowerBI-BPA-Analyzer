#!/usr/bin/env python3
"""Debug the column reference checking logic"""

from tmdl_analyzer import BestPracticesChecker, TMDLMeasure
import re

def debug_column_reference_logic():
    """Debug the column reference checking with detailed output"""
    
    # Test expressions
    expressions = [
        "IF ( ISFILTERED( 'Dim_Agents'[Name] ), \"\", \"Sales Person\" )",  # Should be False (qualified)
        "SUM([Amount]) + COUNT([CustomerID])",  # Should be True (unqualified)
        "IF([Status] = \"Active\", 'Sales'[Amount], 0)",  # Should be True (mixed)
        "100 + 50"  # Should be False (no columns)
    ]
    
    for i, expression in enumerate(expressions, 1):
        print(f"=== TEST {i} ===")
        print(f"Expression: {expression}")
        
        # Pattern from the current implementation
        unqualified_pattern = r"(?<!')\b(?<!\w)\[[^\]]+\]"
        
        # Find all bracket references
        all_brackets = re.findall(r'\[[^\]]+\]', expression)
        print(f"All brackets found: {all_brackets}")
        
        # Find potential unqualified matches
        unqualified_matches = re.findall(unqualified_pattern, expression)
        print(f"Unqualified pattern matches: {unqualified_matches}")
        
        # Test the actual logic
        actual_unqualified = []
        for match in unqualified_matches:
            match_pos = expression.find(match)
            if match_pos >= 0:
                # Get text before the match
                before = expression[:match_pos].rstrip()
                print(f"  Match: {match}, Position: {match_pos}, Before: '{before}'")
                
                # Check if it's truly unqualified
                if (before == "" or 
                    before[-1] in ",()+*/=<>!& \t\n" or
                    before.endswith(" AND ") or 
                    before.endswith(" OR ") or
                    before.endswith("IF ") or
                    before.endswith("ISFILTERED ")):
                    actual_unqualified.append(match)
                    print(f"    -> UNQUALIFIED")
                else:
                    print(f"    -> qualified (before text: '{before}')")
        
        print(f"Final unqualified: {actual_unqualified}")
        print(f"Result: {len(actual_unqualified) > 0}")
        print()

if __name__ == "__main__":
    debug_column_reference_logic()