import cfnlint.helpers
from cfnlint.rules import CloudFormationLintRule


class SkipLineRule(CloudFormationLintRule):
    id = 'W9901'
    shortdesc = 'Skip a specific line'
    description = 'This rule will skip a specific line in the CloudFormation template'
    source_url = ''
    tags = ['line-skipping']

    def match(self, cfn):
        matches = []
        for idx, line in enumerate(cfn.template.split('\n')):
            if line.strip() == '## SKIP THIS LINE':
                matches.append(cfnlint.Match(
                    idx + 1,
                    0,
                    self.id,
                    "This line is skipped"
                ))
        return matches
