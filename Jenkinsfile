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
                    def changedFiles = sh(
                        script: "git diff --name-only HEAD HEAD~1 | grep -E '\\.yaml\$'",
                        returnStdout: true
                    ).trim()
                    if (!changedFiles) {
                        echo "No CloudFormation templates were changed in the last commit."
                    } else {
                        sh "echo \"Scanning the following files: ${changedFiles}\""
                        sh "echo \"\""
                        sh "echo ${changedFiles} | xargs ${env.CFN_LINT_PATH}"
                    }
                }
            }
        }
    }
}
