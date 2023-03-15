pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "nginx"
        DOCKERFILE_PATH = "./Dockerfile"

    stages {
        stage('Build Docker image') {
            steps {
                sh "docker build -t $DOCKER_IMAGE_NAME -f $DOCKERFILE_PATH ."
            }
        }


    }
}
