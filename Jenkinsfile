pipeline {
  agent any
  
  stages {
    stage('Scan CloudFormation Template with cfn-lint') {
      steps {
        // Checkout the GitHub repository
        git url: 'https://github.com/atharva23/LintChecker'
        
        // Install cfn-lint
        sh 'pip3 install cfn-lint'
        
        // Scan the CloudFormation template using cfn-lint
        sh 'cfn-lint volume.yml'
      }
    }
    
  }
}
