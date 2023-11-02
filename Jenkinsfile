pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Hello master pipeline'
      }
    }

  }
  options {
    timeout(time: 1, unit: 'SECONDS')
  }
}