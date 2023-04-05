from cfnlint.rules import CloudFormationLintRule
from cfnlint.rules import RuleMatch

class ExcludeRule(CloudFormationLintRule):
    id = 'E0000'
    shortdesc = 'Exclude specific line'
    description = 'Exclude a specific line in the CloudFormation template'
    source_url = ''
    tags = []

    def match(self, cfn):
        matches = []

        for idx, line in enumerate(cfn.template.split('\n')):
            if 'MY-EXCLUDED-LINE' in line:
                # exclude this line
                return matches

        return matches
