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
                script {
                    def recentCommit = sh(script: "git log -n 1 --pretty=format:'%H'", returnStdout: true).trim()
                    def prevCommit = sh(script: "git log -n 2 --skip=1 --pretty=format:'%H'", returnStdout: true).trim()
                    if (recentCommit == prevCommit) {
                        echo "No new commit"
                    } else {
                        
                        
                        sh "git diff --name-only HEAD HEAD~1 | grep -E '.*.yml' | xargs ${env.CFN_LINT_PATH}"
                    }
                }
            }
        }        
    }
}
