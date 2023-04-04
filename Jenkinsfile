pipeline {
    agent any
    environment {      
        CFN_LINT_PATH = "~/.local/bin/cfn-lint"
       
    }    
    stages {
        stage('Scan CloudFormation templates') {
            steps {
                script {
                    git url: 'https://github.com/atharva23/LintChecker.git', branch: 'main'
                    sh 'pip3 install cfn-lint'
                    sh '${env.CFN_LINT_PATH} --template **/*.yml --append-rules cfn-lint-rules.json'
                   
                }
            }
        }
    }
}
