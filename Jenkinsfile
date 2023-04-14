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
                bat 'python main.py'
            }
        }
    }
}