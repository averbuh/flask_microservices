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
                script {
                    image_auth = docker.build registry_auth + ":$BUILD_NUMBER"
                    image_main = docker.build registry_main  + ":$BUILD_NUMBER"
                  }
              }
          }
        stage("Push to Registry") {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                      image_auth.push()
                      image_main.push()
                      }
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
