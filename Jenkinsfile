pipeline {
    agent any

    stages {

        stage('Verify') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Docker Version') {
            steps {
                sh 'docker --version'
            }
        }
    }
}
