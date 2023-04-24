pipeline {
    agent any
    environment {
        CFN_LINT_PATH = "~/.local/bin/cfn-lint"
        TEMP_FOLDER = "./temp_templates"
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
                        // Create temporary folder structure
                        
                        // Create temporary folder structure
                        def dir_path = i.substring(0, i.lastIndexOf('/'))
                        
                        //This line gets the directory path of the current file by removing the file name from the full path.                        
                        def temp_dir_path = "${TEMP_FOLDER}/${dir_path}"
                        
                        // This line constructs the temporary folder path using the TEMP_FOLDER environment variable and the dir_name variable.                        
                        sh "mkdir -p ${temp_dir_path}"
                     
                    
                        // Replace Ansible variable and copy to temporary folder
                        
                        // Copy the original file to the temporary folder
                        sh "cp ${i} ${temp_dir_path}/${i.substring(i.lastIndexOf('/') + 1)}"

                        // Replace Ansible variables in the copied file
                        sh "sed -i 's/{{ \\([^}]*\\) }}/abc/g' ${temp_dir_path}/${i.substring(i.lastIndexOf('/') + 1)}" 
                        
                        
                        sh "cat ${i}"
                        sh "cat ${temp_dir_path}/${i.substring(i.lastIndexOf('/') + 1)}"


                        // Scan the modified template using cfn-lint
                        
                        def result = sh script: "${env.CFN_LINT_PATH} ${temp_dir_path}/${i.substring(i.lastIndexOf('/') + 1)} --ignore-checks E3031", returnStatus: true

                        if (result != 0 && result != 8) {
                            LINT_FAILED = 1
                        }
                    }          
                    
                    sh "rm -rf ${TEMP_FOLDER}"
                    
                    // Fail the build if there were lint errors
                    if (LINT_FAILED == 1) {
                        error('CloudFormation templates failed linting')
                    }
                }
            }
        }
    }
}
