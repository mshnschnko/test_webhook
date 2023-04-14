#!/usr/bin/env groovy

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
                sh 'python.exe main.py'
            }
        }
    }
}