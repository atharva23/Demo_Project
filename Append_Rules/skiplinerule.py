from cfnlint.rules import CloudFormationLintRule


class SkipLineRule(CloudFormationLintRule):
    id = 'E9999'
    shortdesc = 'Skip specific lines in CloudFormation templates'
    description = 'Skip specific lines in CloudFormation templates'
    source_url = ''
    tags = ['experimental']

    def match(self, cfn):
        filename = cfn.get_filename()
        if filename.endswith('.yml'):
            with open(filename, 'r') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if 'SKIP THIS LINE' in line:
                        return False
        return True
