pipeline {
    agent any
    stages {
        stage('Scan CloudFormation templates') {
            steps {
                script {
                    git url: 'https://github.com/atharva23/LintChecker.git', branch: 'main'
                    sh 'pip3 install cfn-lint'
                    sh 'cfn-lint --template **/*.yml'
                }
            }
        }
    }
}
