pipeline {
    agent any
    options {
      timeout(time: 1, unit: 'SECONDS')
      }
    environment {
        registry_auth = "averbuh/auth"
        registry_main = "averbuh/main"
        registryCredential = 'dockerhub_id'
        image_auth = ''
        image_main = ''
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
                      label registry_main + ":$BUILD_NUMBER"
                      registryUrl registry_main
                      registryCredentialsId registryCredential
                    }
              }
          }
        stage("Cleaning up") {
            steps {
                sh "docker rmi $registry_auth:$BUILD_NUMBER"
                sh "docker rmi $registry_main:$BUILD_NUMBER"
              }
          }
      }
  }
