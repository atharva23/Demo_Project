pipeline {
    agent any
    environment {
        CFN_LINT_PATH = "~/.local/bin/cfn-lint"
        TEMP_FOLDER = "/tmp/cloudformation-templates"
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
                    
                    // Replace Ansible variable with a number in all files and copy them to a temporary folder
                    sh "mkdir -p ${TEMP_FOLDER}"
                    for (i in LINT_FILES) {
                        sh "sed 's/{{ my_ansible_var }}/123/g' ${i} > ${TEMP_FOLDER}/${i}"
                    }
                    
                    // List CloudFormation templates in temporary folder
                    def TEMP_LINT_FILES = sh(script: "find ${TEMP_FOLDER} -name '*.yml'", returnStdout: true).trim().split('\n')
                    echo "TEMP_LINT_FILES: ${TEMP_LINT_FILES}"
                    
                    // Scan CloudFormation templates using cfn-lint
                    def LINT_FAILED = 0
                    for (i in TEMP_LINT_FILES) {
                        def result = sh script: "${env.CFN_LINT_PATH} ${i}", returnStatus: true
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
