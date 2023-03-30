pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/atharva23/LintChecker'
            }
        }

        stage('Install cfn-lint') {
            steps {
                sh 'pip3 install cfn-lint'
            }
        }

        stage('Scan CloudFormation template') {
            steps {
                sh 'cfn-lint --input-path volume.yaml'
            }
        }
    }
}
