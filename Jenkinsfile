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
                        -o INI3.txt
                '''
            }
        }
        stage('Get the Configuration Package from the SBC1'){

            steps {
                sh '''
                    # Credentials for Basic Auth
                    cred="Admin:Admin"
                    cred_encoded=$(echo -n "$cred" | base64)

                    # Call API and save CFG PCKG
                    curl -s -X GET \
                        -H "Authorization: Basic $cred_encoded" \
                        http://192.168.128.128/api/v1/files/configurationPackage.7z \
                        -o CFG-PCKG.7z
                '''

                
            }
        }

        stage('Archive File') {
            steps {
                archiveArtifacts artifacts: 'INI3.txt', onlyIfSuccessful: true
                archiveArtifacts artifacts: 'CFG-PCKG.7z', onlyIfSuccessful: true
            
            }
        }
    }
}
