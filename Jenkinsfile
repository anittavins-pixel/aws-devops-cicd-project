pipeline {
    agent any

    environment {
        ECR_REPO = "128974585758.dkr.ecr.us-east-2.amazonaws.com/flask-app"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/anittavins-pixel/aws-devops-cicd-project.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Push To ECR') {
            steps {
                sh '''
                aws ecr get-login-password --region us-east-2 | \
                docker login --username AWS \
                --password-stdin 128974585758.dkr.ecr.us-east-2.amazonaws.com

                docker tag flask-app:latest $ECR_REPO:latest

                docker push $ECR_REPO:latest
                '''
            }
        }
    }
}
