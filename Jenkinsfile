pipeline {
    agent any
    
    environment {
        GIT_REPO = "https://github.com/atharva23/LintChecker.git"
        CFN_LINT_PATH = "~/.local/bin/cfn-lint"
    }

    stages {
        stage('Clone repository') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: "${env.GIT_REPO}"]]])
            }
        }

        stage('Scan CloudFormation templates') {
            steps {
               
                sh "find . -name '*.yml' -o -name '*.json' | xargs ${env.CFN_LINT_PATH}"
            }
        }
    }
}
