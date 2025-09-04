pipeline {
    agent any

    stages {
        stage('Run API Call with curl') {
            steps {
                script {
                    def status = sh(
                        script: '''
                            cred="Admin:Admin"
                            cred_encoded=$(echo -n "$cred" | base64)

                            # Call API and save response to file
                            curl -s -o INI3.txt -w "%{http_code}" \
                              -H "Authorization: Basic $cred_encoded" \
                              http://192.168.128.144/api/v1/files/in
                        ''',
                        returnStdout: true
                    ).trim()

                    echo "API returned status: ${status}"

                    if (status != "200") {
                        error("API test failed! Stopping pipeline.")
                    }
                }
            }
        }

        stage('Get the Configuration Package from the SBC1') {
            steps {
                sh '''
                    cred="Admin:Admin"
                    cred_encoded=$(echo -n "$cred" | base64)

                    curl -s -X GET \
                        -H "Authorization: Basic $cred_encoded" \
                        http://192.168.128.144/api/v1/files/configurationPackage.7z \
                        -o CFG-PCKG.7z
                '''
            }
        }

        stage('Archive Files') {
            steps {
                archiveArtifacts artifacts: 'INI3.txt', onlyIfSuccessful: true
                archiveArtifacts artifacts: 'CFG-PCKG.7z', onlyIfSuccessful: true
            }
        }
    }
}
