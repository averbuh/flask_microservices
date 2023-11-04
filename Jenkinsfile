pipeline {
    agent any
    options {
      timeout(time: 1, unit: 'SECONDS')
      }
    stages {
        stage("Check") {
            steps {
                echo 'Hello dev pipeline'
              }
          }
        
        stage("Build Image") {
            steps {
                dockerfile {
                    filename 'Dockerfile'
                    dir 'app-main'
                    label 'main'
                  }
                dockerfile {
                    filename 'Dokcerfile'
                    dir 'app-auth'
                    label 'auth'
                  }
              }
          }
        stage("Push to Registry") {
            steps {
                echo 'Pushed'
              }
          }
      }
  }
