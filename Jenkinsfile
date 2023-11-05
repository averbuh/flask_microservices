pipeline {
    agent any
    options {
      timeout(time: 1, unit: 'SECONDS')
      }
    environment {
        registry_auth = "averbuh/auth"
        registry_main = "averbuh/main"
        registryCredential = 'dockerhub_id'
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
                    env.image_auth = docker.build("registry_auth:${env.BUILD_ID}")
                    env.image_main = docker.build("registry_main:${env.BUILD_ID}")
                  }
              }
            
          }
        stage("Push to registry") {
            steps {
                script {
                    docker.withRegistry('https://hub.docker.com/', registryCredential) {
                      image_auth.push()
                      image_main.push()
                      }  
                  }
              }
          }
          
        stage("Cleaning up") {
            steps {
                sh "docker rmi $registry_auth:$BUILD_ID"
                sh "docker rmi $registry_main:$BUILD_ID"
              }
          }
      }
  }
