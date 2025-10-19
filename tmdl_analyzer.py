"""
TMDL Best Practices Analyzer Agent

This AI agent analyzes Power BI TMDL (Tabular Model Definition Language) files
and checks them against Microsoft's Analysis Services best practice rules.

The agent can:
1. Parse TMDL files from a Power BI data model
2. Load and apply best practice rules from BPARules.json
3. Generate detailed reports with violations and recommendations
4. Provide fixing suggestions where possible

Author: GitHub Copilot
Date: October 2025
"""

import os
import json
import re
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import logging


class Severity(Enum):
    """Rule severity levels"""
    INFO = 1
    WARNING = 2
    ERROR = 3


@dataclass
class BestPracticeRule:
    """Represents a single best practice rule"""
    id: str
    name: str
    category: str
    description: str
    severity: int
    scope: str
    expression: str
    fix_expression: Optional[str] = None
    compatibility_level: int = 1200
    
    @property
    def severity_level(self) -> Severity:
        """Convert numeric severity to enum"""
        return Severity(self.severity)


@dataclass
class TMDLObject:
    """Base class for TMDL objects"""
    name: str
    object_type: str
    properties: Dict[str, Any] = field(default_factory=dict)
    content: str = ""
    file_path: str = ""


@dataclass
class TMDLTable(TMDLObject):
    """Represents a TMDL table"""
    columns: List['TMDLColumn'] = field(default_factory=list)
    measures: List['TMDLMeasure'] = field(default_factory=list)
    partitions: List['TMDLPartition'] = field(default_factory=list)
    is_hidden: bool = False
    
    def __post_init__(self):
        self.object_type = "Table"


@dataclass
class TMDLColumn(TMDLObject):
    """Represents a TMDL column"""
    data_type: str = ""
    is_hidden: bool = False
    is_key: bool = False
    format_string: str = ""
    sort_by_column: Optional[str] = None
    source_column: str = ""
    
    def __post_init__(self):
        self.object_type = "Column"


@dataclass
class TMDLMeasure(TMDLObject):
    """Represents a TMDL measure"""
    expression: str = ""
    format_string: str = ""
    is_hidden: bool = False
    display_folder: str = ""
    
    def __post_init__(self):
        self.object_type = "Measure"


@dataclass
class TMDLRelationship(TMDLObject):
    """Represents a TMDL relationship"""
    from_table: str = ""
    from_column: str = ""
    to_table: str = ""
    to_column: str = ""
    is_active: bool = True
    cross_filter_direction: str = "OneDirection"
    from_cardinality: str = "Many"
    to_cardinality: str = "One"
    
    def __post_init__(self):
        self.object_type = "Relationship"


@dataclass
class TMDLPartition(TMDLObject):
    """Represents a TMDL partition"""
    source_type: str = ""
    query: str = ""
    
    def __post_init__(self):
        self.object_type = "Partition"


@dataclass
class Violation:
    """Represents a best practice rule violation"""
    rule_id: str
    rule_name: str
    category: str
    severity: Severity
    description: str
    object_name: str
    object_type: str
    file_path: str
    details: str = ""
    fix_suggestion: Optional[str] = None


class TMDLParser:
    """Parser for TMDL files"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def parse_model_directory(self, model_path: str) -> Dict[str, List[TMDLObject]]:
        """Parse all TMDL files in a model directory"""
        result = {
            'tables': [],
            'relationships': [],
            'measures': [],
            'columns': []
        }
        
        self.logger.info(f"Looking for definition folder in: {model_path}")
        
        definition_path = os.path.join(model_path, 'definition')
        if not os.path.exists(definition_path):
            # Try to find definition folder in subdirectories (for uploaded files)
            found_definition = False
            for root, dirs, files in os.walk(model_path):
                if 'definition' in dirs:
                    definition_path = os.path.join(root, 'definition')
                    self.logger.info(f"Found definition folder at: {definition_path}")
                    found_definition = True
                    break
            
            if not found_definition:
                # List directory contents for debugging
                contents = []
                try:
                    for item in os.listdir(model_path):
                        item_path = os.path.join(model_path, item)
                        if os.path.isdir(item_path):
                            contents.append(f"📁 {item}/")
                        else:
                            contents.append(f"📄 {item}")
                except Exception as e:
                    contents = [f"Error listing directory: {e}"]
                
                contents_str = '\n'.join(contents)
                raise FileNotFoundError(
                    f"Definition folder not found in: {model_path}\n"
                    f"Directory contents:\n{contents_str}\n\n"
                    f"Expected: A .SemanticModel folder with a 'definition' subfolder containing TMDL files."
                )
        
        self.logger.info(f"Using definition path: {definition_path}")
        
        # Parse tables
        tables_path = os.path.join(definition_path, 'tables')
        if os.path.exists(tables_path):
            for file_name in os.listdir(tables_path):
                if file_name.endswith('.tmdl'):
                    file_path = os.path.join(tables_path, file_name)
                    table = self.parse_table_file(file_path)
                    if table:
                        result['tables'].append(table)
                        result['measures'].extend(table.measures)
                        result['columns'].extend(table.columns)
        
        # Parse relationships
        relationships_file = os.path.join(definition_path, 'relationships.tmdl')
        if os.path.exists(relationships_file):
            relationships = self.parse_relationships_file(relationships_file)
            result['relationships'].extend(relationships)
        
        return result
    
    def parse_table_file(self, file_path: str) -> Optional[TMDLTable]:
        """Parse a single table TMDL file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract table name
            table_match = re.search(r'table\s+([^\s\r\n]+)', content)
            if not table_match:
                return None
            
            table_name = table_match.group(1)
            table = TMDLTable(name=table_name, object_type="Table", content=content, file_path=file_path)
            
            # Parse measures
            table.measures = self._parse_measures(content, table_name, file_path)
            
            # Parse columns
            table.columns = self._parse_columns(content, table_name, file_path)
            
            # Parse table properties
            table.is_hidden = 'isHidden: true' in content
            
            return table
            
        except Exception as e:
            self.logger.error(f"Error parsing table file {file_path}: {e}")
            return None
    
    def _parse_measures(self, content: str, table_name: str, file_path: str) -> List[TMDLMeasure]:
        """Parse measures from table content"""
        measures = []
        
        # Find all measure definitions
        measure_pattern = r'measure\s+([\'"]?)([^\'"\r\n]+)\1\s*=\s*(.*?)(?=\n\s*(?:measure|column|partition|annotation|\Z))'
        
        for match in re.finditer(measure_pattern, content, re.DOTALL | re.MULTILINE):
            measure_name = match.group(2).strip()
            measure_content = match.group(3).strip()
            
            measure = TMDLMeasure(
                name=measure_name,
                object_type="Measure",
                content=measure_content,
                file_path=file_path
            )
            
            # Extract expression (DAX code)
            expr_match = re.search(r'```(.*?)```', measure_content, re.DOTALL)
            if expr_match:
                measure.expression = expr_match.group(1).strip()
            else:
                # Single line expression
                lines = measure_content.split('\n')
                if lines:
                    measure.expression = lines[0].strip()
            
            # Extract format string
            format_match = re.search(r'formatString:\s*([^\r\n]+)', measure_content)
            if format_match:
                measure.format_string = format_match.group(1).strip()
            
            # Extract display folder
            folder_match = re.search(r'displayFolder:\s*([^\r\n]+)', measure_content)
            if folder_match:
                measure.display_folder = folder_match.group(1).strip()
            
            measures.append(measure)
        
        return measures
    
    def _parse_columns(self, content: str, table_name: str, file_path: str) -> List[TMDLColumn]:
        """Parse columns from table content"""
        columns = []
        
        # Find all column definitions
        column_pattern = r'column\s+([\'"]?)([^\'"\r\n]+)\1\s*(.*?)(?=\n\s*(?:measure|column|partition|annotation|\Z))'
        
        for match in re.finditer(column_pattern, content, re.DOTALL | re.MULTILINE):
            column_name = match.group(2).strip()
            column_content = match.group(3).strip()
            
            column = TMDLColumn(
                name=column_name,
                object_type="Column",
                content=column_content,
                file_path=file_path
            )
            
            # Extract data type
            datatype_match = re.search(r'dataType:\s*([^\r\n]+)', column_content)
            if datatype_match:
                column.data_type = datatype_match.group(1).strip()
            
            # Extract format string
            format_match = re.search(r'formatString:\s*([^\r\n]+)', column_content)
            if format_match:
                column.format_string = format_match.group(1).strip()
            
            # Extract source column
            source_match = re.search(r'sourceColumn:\s*([^\r\n]+)', column_content)
            if source_match:
                column.source_column = source_match.group(1).strip()
            
            # Check if hidden
            column.is_hidden = 'isHidden: true' in column_content
            
            # Check if key
            column.is_key = 'isKey: true' in column_content
            
            columns.append(column)
        
        return columns
    
    def parse_relationships_file(self, file_path: str) -> List[TMDLRelationship]:
        """Parse relationships from relationships.tmdl file"""
        relationships = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all relationship definitions
            rel_pattern = r'relationship\s+([^\r\n]+)\s*(.*?)(?=\n\s*relationship|\Z)'
            
            for match in re.finditer(rel_pattern, content, re.DOTALL | re.MULTILINE):
                rel_name = match.group(1).strip()
                rel_content = match.group(2).strip()
                
                relationship = TMDLRelationship(
                    name=rel_name,
                    object_type="Relationship",
                    content=rel_content,
                    file_path=file_path
                )
                
                # Extract from column
                from_match = re.search(r'fromColumn:\s*([^\r\n]+)', rel_content)
                if from_match:
                    from_parts = from_match.group(1).strip().split('.')
                    if len(from_parts) == 2:
                        relationship.from_table = from_parts[0]
                        relationship.from_column = from_parts[1]
                
                # Extract to column
                to_match = re.search(r'toColumn:\s*([^\r\n]+)', rel_content)
                if to_match:
                    to_parts = to_match.group(1).strip().split('.')
                    if len(to_parts) == 2:
                        relationship.to_table = to_parts[0]
                        relationship.to_column = to_parts[1]
                
                relationships.append(relationship)
                
        except Exception as e:
            self.logger.error(f"Error parsing relationships file {file_path}: {e}")
        
        return relationships


class BestPracticesChecker:
    """Checks TMDL objects against best practice rules"""
    
    def __init__(self, rules_file: str):
        self.rules = self._load_rules(rules_file)
        self.logger = logging.getLogger(__name__)
    
    def _load_rules(self, rules_file: str) -> List[BestPracticeRule]:
        """Load best practice rules from JSON file"""
        try:
            with open(rules_file, 'r', encoding='utf-8') as f:
                rules_data = json.load(f)
            
            rules = []
            for rule_data in rules_data:
                rule = BestPracticeRule(
                    id=rule_data['ID'],
                    name=rule_data['Name'],
                    category=rule_data['Category'],
                    description=rule_data['Description'],
                    severity=rule_data['Severity'],
                    scope=rule_data['Scope'],
                    expression=rule_data['Expression'],
                    fix_expression=rule_data.get('FixExpression'),
                    compatibility_level=rule_data.get('CompatibilityLevel', 1200)
                )
                rules.append(rule)
            
            return rules
            
        except Exception as e:
            self.logger.error(f"Error loading rules from {rules_file}: {e}")
            return []
    
    def check_objects(self, objects: Dict[str, List[TMDLObject]]) -> List[Violation]:
        """Check all objects against best practice rules"""
        violations = []
        
        for rule in self.rules:
            rule_violations = self._check_rule(rule, objects)
            violations.extend(rule_violations)
        
        return violations
    
    def _check_rule(self, rule: BestPracticeRule, objects: Dict[str, List[TMDLObject]]) -> List[Violation]:
        """Check a specific rule against objects"""
        violations = []
        
        # Determine which objects to check based on rule scope
        target_objects = self._get_objects_by_scope(rule.scope, objects)
        
        for obj in target_objects:
            if self._evaluate_rule_expression(rule, obj, objects):
                violation = Violation(
                    rule_id=rule.id,
                    rule_name=rule.name,
                    category=rule.category,
                    severity=rule.severity_level,
                    description=rule.description,
                    object_name=obj.name,
                    object_type=obj.object_type,
                    file_path=obj.file_path,
                    fix_suggestion=rule.fix_expression
                )
                violations.append(violation)
        
        return violations
    
    def _get_objects_by_scope(self, scope: str, objects: Dict[str, List[TMDLObject]]) -> List[TMDLObject]:
        """Get objects that match the rule scope"""
        target_objects = []
        
        scope_parts = [s.strip() for s in scope.split(',')]
        
        for scope_part in scope_parts:
            if 'Measure' in scope_part:
                target_objects.extend(objects['measures'])
            if 'Column' in scope_part or 'DataColumn' in scope_part or 'CalculatedColumn' in scope_part:
                target_objects.extend(objects['columns'])
            if 'Table' in scope_part:
                target_objects.extend(objects['tables'])
            if 'Relationship' in scope_part:
                target_objects.extend(objects['relationships'])
        
        # Remove duplicates by converting to set and back to list
        # Use object id to ensure uniqueness since TMDLObject might not be hashable
        seen = set()
        unique_objects = []
        for obj in target_objects:
            obj_key = (obj.name, obj.object_type, obj.file_path)
            if obj_key not in seen:
                seen.add(obj_key)
                unique_objects.append(obj)
        
        return unique_objects
    
    def _evaluate_rule_expression(self, rule: BestPracticeRule, obj: TMDLObject, all_objects: Dict[str, List[TMDLObject]]) -> bool:
        """Evaluate if an object violates a rule"""
        try:
            # Simplified rule evaluation - implement specific checks for common rules
            expression = rule.expression.lower()
            
            # Check for specific rule patterns
            if rule.id == "PROVIDE_FORMAT_STRING_FOR_MEASURES":
                return self._check_measure_format_string(obj)
            elif rule.id == "USE_THE_DIVIDE_FUNCTION_FOR_DIVISION":
                return self._check_divide_function(obj)
            elif rule.id == "AVOID_USING_THE_IFERROR_FUNCTION":
                return self._check_iferror_function(obj)
            elif rule.id == "HIDE_FOREIGN_KEYS":
                return self._check_foreign_key_hidden(obj, all_objects)
            elif rule.id == "DAX_COLUMNS_FULLY_QUALIFIED":
                return self._check_column_references(obj)
            elif rule.id == "AVOID_FLOATING_POINT_DATA_TYPES":
                return self._check_floating_point_datatype(obj)
            
            return False
            
        except Exception as e:
            self.logger.error(f"Error evaluating rule {rule.id} for object {obj.name}: {e}")
            return False
    
    def _check_measure_format_string(self, obj: TMDLObject) -> bool:
        """Check if measure has format string"""
        if isinstance(obj, TMDLMeasure) and not obj.is_hidden:
            return not obj.format_string or obj.format_string.strip() == ""
        return False
    
    def _check_divide_function(self, obj: TMDLObject) -> bool:
        """Check if measure uses / instead of DIVIDE function"""
        if isinstance(obj, TMDLMeasure):
            # Look for division operators
            pattern = r'\]\s*/(?!//)(?!/\*)'
            return bool(re.search(pattern, obj.expression))
        return False
    
    def _check_iferror_function(self, obj: TMDLObject) -> bool:
        """Check if measure uses IFERROR function"""
        if isinstance(obj, TMDLMeasure):
            return bool(re.search(r'IFERROR\s*\(', obj.expression, re.IGNORECASE))
        return False
    
    def _check_foreign_key_hidden(self, obj: TMDLObject, all_objects: Dict[str, List[TMDLObject]]) -> bool:
        """Check if foreign key column is hidden"""
        if isinstance(obj, TMDLColumn):
            # Check if column is used in relationships as foreign key and not hidden
            for rel in all_objects['relationships']:
                if isinstance(rel, TMDLRelationship):
                    if rel.from_column == obj.name and not obj.is_hidden:
                        return True
        return False
    
    def _check_column_references(self, obj: TMDLObject) -> bool:
        """Check if DAX expression uses fully qualified column references"""
        if isinstance(obj, TMDLMeasure):
            # Check for unqualified column references
            # Qualified: 'TableName'[ColumnName] or TableName[ColumnName] 
            # Unqualified: [ColumnName] (standalone, not preceded by table name)
            
            expression = obj.expression
            
            # Pattern to find unqualified column references:
            # [ColumnName] that is NOT preceded by a table name
            # Negative lookbehind to ensure it's not: 'TableName'[Column] or TableName[Column]
            
            # This regex looks for [something] that is not preceded by:
            # - 'quoted text' (quoted table name)
            # - word characters (unquoted table name)
            unqualified_pattern = r"(?<!')\b(?<!\w)\[[^\]]+\]"
            
            unqualified_matches = re.findall(unqualified_pattern, expression)
            
            # Additional check: remove false positives by checking context
            actual_unqualified = []
            for match in unqualified_matches:
                match_pos = expression.find(match)
                if match_pos >= 0:
                    # Get text before the match
                    before = expression[:match_pos].rstrip()
                    
                    # Check if it's truly unqualified (not part of a table reference)
                    if (before == "" or 
                        before[-1] in ",()+*/=<>!& \t\n" or
                        before.endswith(" AND ") or 
                        before.endswith(" OR ") or
                        before.endswith("IF ") or
                        before.endswith("ISFILTERED ")):
                        actual_unqualified.append(match)
            
            return len(actual_unqualified) > 0
        return False
    
    def _check_floating_point_datatype(self, obj: TMDLObject) -> bool:
        """Check if column uses floating point data type"""
        if isinstance(obj, TMDLColumn):
            return obj.data_type.lower() == "double"
        return False


class TMDLBestPracticesAgent:
    """Main agent class for analyzing TMDL files"""
    
    def __init__(self, rules_file: str):
        self.parser = TMDLParser()
        self.checker = BestPracticesChecker(rules_file)
        self.logger = logging.getLogger(__name__)
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    def analyze_model(self, model_path: str) -> Dict[str, Any]:
        """Analyze a TMDL model and return findings"""
        self.logger.info(f"Starting analysis of model: {model_path}")
        
        try:
            # Parse TMDL files
            objects = self.parser.parse_model_directory(model_path)
            
            self.logger.info(f"Parsed {len(objects['tables'])} tables, {len(objects['measures'])} measures, "
                           f"{len(objects['columns'])} columns, {len(objects['relationships'])} relationships")
            
            # Check best practices
            violations = self.checker.check_objects(objects)
            
            # Generate summary
            summary = self._generate_summary(objects, violations)
            
            self.logger.info(f"Analysis complete. Found {len(violations)} violations.")
            
            return {
                'summary': summary,
                'objects': objects,
                'violations': violations,
                'model_path': model_path
            }
            
        except Exception as e:
            self.logger.error(f"Error analyzing model: {e}")
            raise
    
    def _generate_summary(self, objects: Dict[str, List[TMDLObject]], violations: List[Violation]) -> Dict[str, Any]:
        """Generate analysis summary"""
        summary = {
            'object_counts': {
                'tables': len(objects['tables']),
                'measures': len(objects['measures']),
                'columns': len(objects['columns']),
                'relationships': len(objects['relationships'])
            },
            'violations': {
                'total': len(violations),
                'by_severity': {},
                'by_category': {},
                'by_rule': {}
            },
            'rules_checked': {
                'total': len(self.checker.rules),
                'rules_with_violations': 0,
                'rules_without_violations': 0,
                'all_rules': []
            }
        }
        
        # Count violations by severity
        for violation in violations:
            severity = violation.severity.name
            summary['violations']['by_severity'][severity] = summary['violations']['by_severity'].get(severity, 0) + 1
        
        # Count violations by category
        for violation in violations:
            category = violation.category
            summary['violations']['by_category'][category] = summary['violations']['by_category'].get(category, 0) + 1
        
        # Count violations by rule
        for violation in violations:
            rule_id = violation.rule_id
            if rule_id not in summary['violations']['by_rule']:
                summary['violations']['by_rule'][rule_id] = {
                    'count': 0,
                    'name': violation.rule_name,
                    'category': violation.category,
                    'severity': violation.severity.name
                }
            summary['violations']['by_rule'][rule_id]['count'] += 1
        
        # Add information about all rules checked
        for rule in self.checker.rules:
            rule_info = {
                'id': rule.id,
                'name': rule.name,
                'category': rule.category,
                'severity': rule.severity_level.name,
                'violation_count': summary['violations']['by_rule'].get(rule.id, {}).get('count', 0),
                'has_violations': rule.id in summary['violations']['by_rule']
            }
            summary['rules_checked']['all_rules'].append(rule_info)
            
            if rule_info['has_violations']:
                summary['rules_checked']['rules_with_violations'] += 1
            else:
                summary['rules_checked']['rules_without_violations'] += 1
        
        return summary
    
    def generate_report(self, analysis_result: Dict[str, Any], output_file: Optional[str] = None) -> str:
        """Generate a detailed analysis report"""
        violations = analysis_result['violations']
        summary = analysis_result['summary']
        
        report_lines = []
        report_lines.append("# TMDL Best Practices Analysis Report")
        report_lines.append(f"\nModel: {analysis_result['model_path']}")
        report_lines.append(f"Analysis Date: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Summary section
        report_lines.append("\n## Summary")
        report_lines.append(f"- Tables: {summary['object_counts']['tables']}")
        report_lines.append(f"- Measures: {summary['object_counts']['measures']}")
        report_lines.append(f"- Columns: {summary['object_counts']['columns']}")
        report_lines.append(f"- Relationships: {summary['object_counts']['relationships']}")
        report_lines.append(f"- Total Violations: {summary['violations']['total']}")
        
        # Violations by severity
        report_lines.append("\n### Violations by Severity")
        for severity, count in summary['violations']['by_severity'].items():
            report_lines.append(f"- {severity}: {count}")
        
        # Violations by category
        report_lines.append("\n### Violations by Category")
        for category, count in summary['violations']['by_category'].items():
            report_lines.append(f"- {category}: {count}")
        
        # Detailed violations
        if violations:
            report_lines.append("\n## Detailed Violations")
            
            # Group by category
            violations_by_category = {}
            for violation in violations:
                category = violation.category
                if category not in violations_by_category:
                    violations_by_category[category] = []
                violations_by_category[category].append(violation)
            
            for category, category_violations in violations_by_category.items():
                report_lines.append(f"\n### {category}")
                
                for violation in category_violations:
                    report_lines.append(f"\n#### {violation.rule_name}")
                    report_lines.append(f"**Object:** {violation.object_name} ({violation.object_type})")
                    report_lines.append(f"**Severity:** {violation.severity.name}")
                    report_lines.append(f"**File:** {violation.file_path}")
                    report_lines.append(f"**Description:** {violation.description}")
                    
                    if violation.fix_suggestion:
                        report_lines.append(f"**Fix Suggestion:** {violation.fix_suggestion}")
        
        report_content = "\n".join(report_lines)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report_content)
        
        return report_content


if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python tmdl_analyzer.py <model_path> [rules_file] [output_file]")
        sys.exit(1)
    
    model_path = sys.argv[1]
    rules_file = sys.argv[2] if len(sys.argv) > 2 else "BPARules.json"
    output_file = sys.argv[3] if len(sys.argv) > 3 else None
    
    # Create and run the agent
    agent = TMDLBestPracticesAgent(rules_file)
    
    try:
        result = agent.analyze_model(model_path)
        report = agent.generate_report(result, output_file)
        
        if output_file:
            print(f"Report saved to: {output_file}")
        else:
            print(report)
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)