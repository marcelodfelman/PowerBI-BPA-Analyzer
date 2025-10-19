from tmdl_analyzer import TMDLBestPracticesAgent

agent = TMDLBestPracticesAgent('BPARules.json')
result = agent.analyze_model('Sales Dashboard.SemanticModel/')

violations_by_rule = {}
for v in result['violations']:
    if v.rule_id not in violations_by_rule:
        violations_by_rule[v.rule_id] = []
    violations_by_rule[v.rule_id].append(v)

print(f'Total violations: {len(result["violations"])}')
print(f'Unique rules with violations: {len(violations_by_rule)}')
print('\nViolations by rule:')
for rule_id, viols in violations_by_rule.items():
    print(f'  {rule_id}: {len(viols)} violations')
    
print('\n\nAll 8 rules in BPARules.json:')
for i, rule in enumerate(agent.checker.rules):
    count = len(violations_by_rule.get(rule.id, []))
    status = f'{count} violations' if count > 0 else 'NO VIOLATIONS'
    print(f'{i+1}. {rule.id}: {status}')

