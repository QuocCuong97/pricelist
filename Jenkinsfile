pipeline{
    agent any
    stages {
        stage('Clone repository') {
            steps {
                checkout master
            }
        }
        stage('Clear old version') {
            steps {
                echo "Running source code in a fully containerized environment..."
                sh '/usr/local/bin/docker-compose down -v'
            }
        }
        stage('Deploy Source Code') {
            steps {
                echo "Running source code in a fully containerized environment..."    
                sh '/usr/local/bin/docker-compose up -d --build'
            }
        }
    }
}