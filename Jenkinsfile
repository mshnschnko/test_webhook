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
        stage('Run python script') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker build -t mshnschnko/test_hook .'
                        sh 'docker run -i -t mshnschnko/test_hook'
                        // sh 'python main.py'
                    } else {
                        // bat 'python main.py'
                        bat 'docker build -t mshnschnko/test_hook .'
                        bat 'docker run -i -t mshnschnko/test_hook'
                    }
                }
            }
        }
    }
}