pipeline {
    agent any

    environment {
        APP_NAME = "flask-app"
        IMAGE_NAME = "flask-app:v1"
        SERVICE_NAME = "flask-service"
    }

    stages {

        stage('Clone') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Vivekkulkarni521/myflaskapp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t ${IMAGE_NAME} .
                '''
            }
        }

        stage('Remove Old Image (Optional)') {
            steps {
                sh '''
                docker image prune -f
                '''
            }
        }

        stage('Deploy to Docker Swarm') {
            steps {
                sh '''
                if docker service ls | grep -q ${SERVICE_NAME}
                then
                    echo "Service already exists. Updating..."
                    docker service update --image ${IMAGE_NAME} ${SERVICE_NAME}
                else
                    echo "Creating new service..."
                    docker service create \
                      --name ${SERVICE_NAME} \
                      --replicas 3 \
                      -p 5000:5000 \
                      ${IMAGE_NAME}
                fi
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                docker service ls
                docker service ps ${SERVICE_NAME}
                '''
            }
        }
    }

    post {
        success {
            echo "Docker Swarm deployment completed successfully."
        }

        failure {
            echo "Deployment failed."
        }
    }
}
