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
                        sh 'python main.py'
                    } else {
                        bat 'python main.py'
                    }
                }
            }
        }
    }
}