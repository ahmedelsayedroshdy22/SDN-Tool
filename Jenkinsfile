pipeline {
    agent any

    stages {
        stage('Run PowerShell API Call') {
            steps {
                sh '''
                    pwsh -Command "
                        \$cred = 'Admin:Admin'
                        \$cred_encoded = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(\$cred))
                        \$headers = @{ Authorization = 'Basic ' + \$cred_encoded }
                        Invoke-RestMethod -Method GET -Uri 'http://192.168.128.128/api/v1/files/ini' -Headers \$headers -OutFile 'INI.txt'
                    "
                '''
            }
        }

        stage('Archive Output File') {
            steps {
                archiveArtifacts artifacts: 'INI.txt', onlyIfSuccessful: true
            }
        }
    }
}
