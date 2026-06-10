pipeline {

    agent any

    environment {
        IMAGE_NAME = "faceattendance:latest"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t faceattendance .'
            }
        }

        stage('Load Image into Minikube') {
            steps {
                bat 'minikube image load faceattendance'
            }
        }

        stage('Deploy Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/'
            }
        }

        stage('Check Deployment') {
            steps {
                bat 'kubectl get pods'
                bat 'kubectl get svc'
            }
        }
    }

    post {

        success {
            echo 'Deployment Successful!'
        }

        failure {
            echo 'Deployment Failed!'
        }
    }
}

