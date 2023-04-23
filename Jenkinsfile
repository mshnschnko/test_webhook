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
                        sh 'rm -rf test_webhook'
                        sh 'git clone --depth=1 https://github.com/mshnschnko/test_webhook.git'
                        sh 'rm -rf test_webhook/.git*'
                        sh 'ls'
                    } else {
                        bat 'rm -rf test_webhook'
                        bat 'git clone --depth=1 https://github.com/mshnschnko/test_webhook.git'
                        bat 'rm -rf test_webhook/.git*'
                        bat 'ls'
                    }
                }
            }
        }
        stage('Getting env and buackup') {
            steps {
                echo 'Getting environment variables and backuping data...'
                withCredentials([file(credentialsId: 'ENV', variable: 'ENV')]) {
                    script {
                        if (isUnix()) {
                            sh 'cp $ENV ./.env'
                            sh 'mkdir -p ./storage/temp'
                            sh 'mkdir -p ./storage/backup'
                            // sh 'python backup.py'
                        } else {
                            bat 'powershell Copy-Item %ENV% -Destination ./.env'
                            bat 'If Not Exist storage\\temp mkdir storage\\temp'
                            bat 'If Not Exist storage\\backup mkdir storage\\backup'
                            // bat 'python backup.py'
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