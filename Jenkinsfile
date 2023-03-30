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
                sh 'pip install cfn-lint'
            }
        }

        stage('Scan CloudFormation template') {
            steps {
                sh 'cfn-lint volume.yaml'
            }
        }
    }
}
