#!/usr/bin/sh

pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Download git repo') {
            steps {
                echo 'Downloading git repo...'
                script {
                    if (isUnix()) {
                        sh 'git clone --depth=1 https://github.com/mshnschnko/test_webhook.git'
                        sh 'rm -rf test_webhook/.git*'
                        sh 'ls'
                    } else {
                        bat 'git clone --depth=1 https://github.com/mshnschnko/test_webhook.git'
                        bat 'rm -r -fo test_webhook\.git*'
                        bat 'ls'
                    }
                }
            }
        }
        stage('Getting env') {
            steps {
                echo 'Getting environment variables...'
                withCredentials([file(credentialsId: 'ENV', variable: 'ENV')]) {
                    script {
                        if (isUnix()) {
                            sh 'cp $ENV ./.env'
                            // sh 'docker build -t mshnschnko/test_hook .'
                            // sh 'docker run mshnschnko/test_hook'
                            // sh 'python main.py'
                        } else {
                            bat 'powershell Copy-Item %ENV% -Destination ./.env'
                            // bat 'docker build -t mshnschnko/test_hook .'
                            // bat 'docker exec -it mshnschnko/test_hook bash'
                            // bat 'docker run mshnschnko/test_hook'
                            // bat 'python main.py'
                        }
                    }
                }
            }
        }
    }
    post {
        success {
            script {
                if (isUnix()) {
                    // sh 'cp $ENV ./.env'
                    sh 'docker build -t mshnschnko/test_hook .'
                    sh 'docker run --name jenk_bot -d --rm mshnschnko/test_hook'
                    // sh 'python main.py'
                } else {
                    // bat 'powershell Copy-Item %ENV% -Destination ./.env'
                    bat 'docker build -t mshnschnko/test_hook .'
                    // bat 'docker exec -it mshnschnko/test_hook bash'
                    bat 'docker run --name jenk_bot -d --rm mshnschnko/test_hook'
                    // bat 'python main.py'
                }
            }
        }
    }
}