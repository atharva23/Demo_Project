pipeline {
    agent any
    environment {
        CFN_LINT_PATH = "~/.local/bin/cfn-lint"
        TEMP_FOLDER = "temp"
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
                    
                    // Replace Ansible variables in CloudFormation templates and copy to temporary folder
                    for (i in LINT_FILES) {
                        sh "mkdir -p ${TEMP_FOLDER}"
                        sh "sed 's/\\$[{]*[a-zA-Z0-9_]*[}]*/123/g' ${i} | awk '{print} /123/{print \"Ansible variable replaced with 123\"}' > ${TEMP_FOLDER}/${i}"
                    }
                    
                    // Scan CloudFormation templates using cfn-lint
                    def LINT_FAILED = 0
                    for (i in LINT_FILES) {
                        def result = sh script: "${env.CFN_LINT_PATH} ${TEMP_FOLDER}/${i}", returnStatus: true
                        if (result != 0 && result != 8) {
                            LINT_FAILED = 1
                        }
                    }
                    
                    // List templates in temporary folder
                    sh "ls -l ${TEMP_FOLDER}"
                    
                    // Fail the build if there were lint errors
                    if (LINT_FAILED == 1) {
                        error('CloudFormation templates failed linting')
                    }
                }
            }
        }
    }
}
