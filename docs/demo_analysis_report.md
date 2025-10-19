# TMDL Best Practices Analysis Report

Model: Sales Dashboard.SemanticModel
Analysis Date: 2025-10-11 17:16:58

## Summary
- Tables: 9
- Measures: 56
- Columns: 106
- Relationships: 6
- Total Violations: 166

### Violations by Severity
- WARNING: 90
- ERROR: 76

### Violations by Category
- Performance: 63
- DAX Expressions: 43
- Formatting: 60

## Detailed Violations

### Performance

#### [Performance] Do not use floating point data types
**Object:** Target_Sales (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Commission (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Credit (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Customers.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** QuarterNumOfYear (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** HalfOfYearNum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** HalfOfCalendarYearSum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** MonthNumberOfYear (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** DayOfMonth (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** DateInt (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** DayOFWeekNum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** YearMonthSum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** YearQuarterSum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** DaysInMonth (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** WeekInYear (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** YearMonthNumber (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Is Working Day (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Cost (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Products.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** amount (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\factBikesSales.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** AmountSales (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Dim_Products.Cost (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** % Profit (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Target_Sales (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Commission (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Credit (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Customers.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** QuarterNumOfYear (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** HalfOfYearNum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** HalfOfCalendarYearSum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** MonthNumberOfYear (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** DayOfMonth (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** DateInt (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** DayOFWeekNum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** YearMonthSum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** YearQuarterSum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** DaysInMonth (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** WeekInYear (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** YearMonthNumber (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Is Working Day (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Cost (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Products.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** amount (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\factBikesSales.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** AmountSales (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Dim_Products.Cost (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** % Profit (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Target_Sales (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Commission (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Credit (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Customers.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** QuarterNumOfYear (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** HalfOfYearNum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** HalfOfCalendarYearSum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** MonthNumberOfYear (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** DayOfMonth (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** DateInt (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** DayOFWeekNum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** YearMonthSum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** YearQuarterSum (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** DaysInMonth (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** WeekInYear (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** YearMonthNumber (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Is Working Day (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Cost (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Products.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** amount (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\factBikesSales.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** AmountSales (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** Dim_Products.Cost (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

#### [Performance] Do not use floating point data types
**Object:** % Profit (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** The "Double" floating point data type should be avoided, as it can result in unpredictable roundoff errors and decreased performance in certain scenarios. Use "Int64" or "Decimal" where appropriate (but note that "Decimal" is limited to 4 digits after the decimal sign).
**Fix Suggestion:** DataType = DataType.Decimal

### DAX Expressions

#### [DAX Expressions] Column references should be fully qualified
**Object:** Title SalesPerson (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Background Color SalesPerson DarkBlue (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Background Color SalesPerson Black (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Left to Target (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Total Target (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** % Left to target (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Background Color Customer DarkBlue (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Customers.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Title Customers (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Customers.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Background Color Customer Black (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Customers.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** MaxDate (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** MinDate (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Selected Year (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Title Product (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Products.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Background Color Product (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Products.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Background Color Product Black (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Products.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Top Product Sold (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Products.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Total Bike Sales (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\factBikesSales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Total Bike Sales PY (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\factBikesSales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Diff Bike Sales vs PY (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\factBikesSales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Total Sales (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Total Profit (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** % - Profit (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Total Cost (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Sales MTD (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Total Sales LY (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Sales LM (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** % Change Sales from LY (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Sales Full LM (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** % Change Sales CM from Full LM (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Sales Full LY (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Total Sales LY samedate (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Monthly Sales % Change vs LY (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Monthly Sales % Change vs LM (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** # Yearly Sales (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Sales YTD (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Total Quantity (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** # Distinct Customers (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Top Sale Type (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** SelectedMeasure (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Parameter_SalesAndProfit.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Title for Products (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Parameter_SalesAndProfit.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Title for Customers (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Parameter_SalesAndProfit.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** MaxY (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\tbl_Measures.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

#### [DAX Expressions] Column references should be fully qualified
**Object:** Dummy Line (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\tbl_Measures.tmdl
**Description:** Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets.
Reference: https://www.elegantbi.com/post/top10bestpractices

### Formatting

#### [Formatting] Provide format string for measures
**Object:** Title SalesPerson (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Background Color SalesPerson DarkBlue (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Background Color SalesPerson Black (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Left to Target (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Total Target (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Agents.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Background Color Customer DarkBlue (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Customers.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Title Customers (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Customers.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Background Color Customer Black (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Customers.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Selected Year (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Dates.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Title Product (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Products.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Background Color Product (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Products.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Background Color Product Black (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Products.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Top Product Sold (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Products.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Total Bike Sales (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\factBikesSales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Total Bike Sales PY (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\factBikesSales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Yearly Sales (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Sales Full LM (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Monthly Sales (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Monthly Sales LY (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Sales Full LY (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Total Sales LY samedate (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Monthly Sales LM (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** # Yearly Sales (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Sales YTD (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Tooltip information about bars (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** % from ly as target (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Top Sale Type (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Total Sales LQ (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** SelectedMeasure (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Parameter_SalesAndProfit.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Title for Products (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Parameter_SalesAndProfit.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Title for Customers (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\Parameter_SalesAndProfit.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** MaxY (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\tbl_Measures.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Provide format string for measures
**Object:** Dummy Line (Measure)
**Severity:** ERROR
**File:** Sales Dashboard.SemanticModel\definition\tables\tbl_Measures.tmdl
**Description:** Visible measures should have their format string property assigned

#### [Formatting] Hide foreign keys
**Object:** item_name (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\DimBikeProducts.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** Customer_Number (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Customers.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** SKU (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Products.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** sale_date (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\factBikesSales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** item_name (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\factBikesSales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** SaleDate (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** Customer_Number (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** SKU (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** SalesPerson (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** item_name (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\DimBikeProducts.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** Customer_Number (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Customers.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** SKU (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Products.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** sale_date (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\factBikesSales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** item_name (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\factBikesSales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** SaleDate (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** Customer_Number (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** SKU (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** SalesPerson (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** item_name (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\DimBikeProducts.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** Customer_Number (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Customers.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** SKU (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Dim_Products.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** sale_date (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\factBikesSales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** item_name (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\factBikesSales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** SaleDate (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** Customer_Number (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** SKU (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true

#### [Formatting] Hide foreign keys
**Object:** SalesPerson (Column)
**Severity:** WARNING
**File:** Sales Dashboard.SemanticModel\definition\tables\Fact_Sales.tmdl
**Description:** Foreign keys should always be hidden.
**Fix Suggestion:** IsHidden = true