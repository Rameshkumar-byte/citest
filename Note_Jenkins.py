pipeline {
    agent any

    stages {
        stage('Example Stage') {
            steps {
                script {
                    try {
                        bat 'E:\\Note.bat'
                    } catch (Exception e) {
                        echo "Error executing batch file: ${e.message}"
                        currentBuild.result = 'FAILURE'
                        error("Error executing batch file")
                    }
                }
            }
        }
    }
}
