pipeline {
    agent any
    environment {
        GIT_REPO = "https://github.com/atharva23/LintChecker.git"
       
    }
    stages {
        stage('Clone repository') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: "${env.GIT_REPO}"]]])
            }
        }
        stage('Scan CloudFormation templates') {
            steps {
                sh "pwd"
                sh "find . -name '*.yml' -o -name '*.json' | xargs ~/.local/bin/cfn-lint"
            }
        }
    }
}
