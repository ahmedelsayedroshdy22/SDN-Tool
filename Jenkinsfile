pipeline {
    agent any

    stages {
        stage('Say Hello') {
            steps {
                echo 'Hello from Jenkins Pipeline!'
            }
        }

        stage('Run a Command') {
            steps {
                sh 'echo "This is running inside the Jenkins container on Linux"'
            }
        }
    }
}
