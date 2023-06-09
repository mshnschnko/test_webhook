#!/usr/bin/sh

pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Stop old container') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker stop jenk_bot || true'
                    } else {
                        bat 'docker stop jenk_bot || true'
                    }
                }
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
            withCredentials([string(credentialsId: 'DB_URL', variable: 'DB_URL')]) {
                script {
                    if (isUnix()) {
                        // sh 'cp $ENV ./.env'
                        // sh 'docker stop jenk_bot'
                        sh 'docker build -t mshnschnko/test_hook .'
                        sh 'docker run --name jenk_bot -d --rm mshnschnko/test_hook'
                        sh 'touch storage/dump.sql'
                        sh 'docker exec jenk_bot bash -c "pg_dump --dbname=$DB_URL -f storage/dump.sql"'
                        sh 'docker exec -d jenk_bot bash -c "python backup.py"'
                        // sh 'python main.py'
                    } else {
                        // bat 'powershell Copy-Item %ENV% -Destination ./.env'
                        // bat 'docker stop jenk_bot'
                        bat 'docker build -t mshnschnko/test_hook .'
                        bat 'docker run --name jenk_bot -d --rm mshnschnko/test_hook'
                        bat 'If Not Exist storage/dump.sql powershell New-Item storage/dump.sql'
                        bat 'docker exec jenk_bot bash -c "pg_dump --dbname=%DB_URL% -f storage/dump.sql"'
                        bat 'docker exec -d jenk_bot bash -c "python backup.py"'
                        // bat 'python3 -m venv .venv'
                        // bat '.\\.venv\\Scripts\\activate'
                        // bat 'pip install dotenv yadisk'
                        // bat 'python backup.py'
                        // bat 'docker exec -it mshnschnko/test_hook bash'
                        // bat 'python main.py'
                    }
                }
            }
        }
    }
}