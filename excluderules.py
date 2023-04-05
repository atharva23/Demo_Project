import cfnlint

def excluderules(rule_id, rule_text, path, **kwargs):
    template = cfnlint.decode.decode(path)
    for idx, line in enumerate(template.split('\n')):
        if 'ExcludeThisLine: true' in line:
            return cfnlint.Issue(
                rule_id,
                rule_text.format(line),
                cfnlint.ParseError([cfnlint.Match(idx, 0, line)], path),
            )
    return None
