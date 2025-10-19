#!/usr/bin/env python3
"""Test script to verify column reference checking logic"""

from tmdl_analyzer import BestPracticesChecker, TMDLMeasure

def test_column_reference_checking():
    """Test the column reference checking logic"""
    
    # Initialize checker
    checker = BestPracticesChecker('BPARules.json')
    
    # Test 1: Expression with properly qualified column references (should NOT trigger violation)
    test_measure1 = TMDLMeasure(
        name='Title SalesPerson',
        object_type='Measure',
        expression='IF ( ISFILTERED( \'Dim_Agents\'[Name] ), "", "Sales Person" )',
        format_string="",
        is_hidden=False,
        display_folder=""
    )
    
    print("=== TEST 1: Qualified Column References ===")
    print(f"Expression: {test_measure1.expression}")
    has_unqualified1 = checker._check_column_references(test_measure1)
    print(f"Has unqualified references: {has_unqualified1}")
    print(f"Expected: False (this should NOT trigger violation)")
    print()
    
    # Test 2: Expression with unqualified column references (SHOULD trigger violation)
    test_measure2 = TMDLMeasure(
        name='Test Unqualified',
        object_type='Measure',
        expression='SUM([Amount]) + COUNT([CustomerID])',
        format_string="",
        is_hidden=False,
        display_folder=""
    )
    
    print("=== TEST 2: Unqualified Column References ===")
    print(f"Expression: {test_measure2.expression}")
    has_unqualified2 = checker._check_column_references(test_measure2)
    print(f"Has unqualified references: {has_unqualified2}")
    print(f"Expected: True (this SHOULD trigger violation)")
    print()
    
    # Test 3: Mixed qualified and unqualified (SHOULD trigger violation)
    test_measure3 = TMDLMeasure(
        name='Mixed References',
        object_type='Measure',
        expression='IF([Status] = "Active", \'Sales\'[Amount], 0)',
        format_string="",
        is_hidden=False,
        display_folder=""
    )
    
    print("=== TEST 3: Mixed References ===")
    print(f"Expression: {test_measure3.expression}")
    has_unqualified3 = checker._check_column_references(test_measure3)
    print(f"Has unqualified references: {has_unqualified3}")
    print(f"Expected: True (this SHOULD trigger violation due to [Status])")
    print()
    
    # Test 4: No column references (should NOT trigger violation)
    test_measure4 = TMDLMeasure(
        name='No Columns',
        object_type='Measure',
        expression='100 + 50',
        format_string="",
        is_hidden=False,
        display_folder=""
    )
    
    print("=== TEST 4: No Column References ===")
    print(f"Expression: {test_measure4.expression}")
    has_unqualified4 = checker._check_column_references(test_measure4)
    print(f"Has unqualified references: {has_unqualified4}")
    print(f"Expected: False (no column references)")
    print()
    
    # Summary
    print("=== SUMMARY ===")
    test_results = [
        ("Qualified references", not has_unqualified1, "PASS" if not has_unqualified1 else "FAIL"),
        ("Unqualified references", has_unqualified2, "PASS" if has_unqualified2 else "FAIL"),
        ("Mixed references", has_unqualified3, "PASS" if has_unqualified3 else "FAIL"),
        ("No column references", not has_unqualified4, "PASS" if not has_unqualified4 else "FAIL"),
    ]
    
    for test_name, passed, status in test_results:
        print(f"{test_name}: {status}")
    
    all_passed = all(result[1] for result in test_results)
    print(f"\nOverall: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    
    return all_passed

if __name__ == "__main__":
    test_column_reference_checking()