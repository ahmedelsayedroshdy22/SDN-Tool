pipeline {
    agent any

    stages {
        stage('Run API Call with curl') {
            steps {
                sh '''
                    # Credentials for Basic Auth
                    cred="Admin:Admin"
                    cred_encoded=$(echo -n "$cred" | base64)

                    # Call API and save to INI.txt
                    curl -s -X GET \
                        -H "Authorization: Basic $cred_encoded" \
                        http://192.168.128.128/api/v1/files/ini \
                        -o INI.txt
                '''
            }
        }

        stage('Archive File') {
            steps {
                archiveArtifacts artifacts: 'INI.txt', onlyIfSuccessful: true
            }
        }
    }
}
