pipeline {
    agent any
    environment {
        CFN_LINT_PATH = "~/.local/bin/cfn-lint"
    }
    stages {
        stage('Scan CloudFormation templates') {
            steps {
                script {
                    // Clone the Git repository
                    git branch: 'main', url: 'https://github.com/atharva23/LintChecker.git'
                    
                    // Install cfn-lint
                    sh 'pip3 install cfn-lint'
                    
                    // List all CloudFormation templates
                    def LINT_FILES = sh(script: "find . -name '*.yml'", returnStdout: true).trim().split('\n')
                    echo "LINT_FILES: ${LINT_FILES}"
                    
                    // Scan CloudFormation templates using cfn-lint
                    def LINT_FAILED = 0
                    for (i in LINT_FILES) {
                        def result = sh script: "${env.CFN_LINT_PATH}  ${i}", returnStatus: true
                        if (result != 0 && result != 8) {
                            LINT_FAILED = 1
                        }
                    }
                    
                    // Fail the build if there were lint errors
                    if (LINT_FAILED == 1) {
                        error('CloudFormation templates failed linting')
                    }
                }
            }
        }
    }
}
