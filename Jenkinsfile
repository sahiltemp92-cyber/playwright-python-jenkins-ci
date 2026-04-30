pipeline {
    agent any

    stages {

        stage('Setup Environment') {
            steps {
                sh '''
                python -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                playwright install --with-deps
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest --html=reports/report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Playwright Automation Report'
            ])
        }
    }
}