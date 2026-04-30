pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'mkdir -p reports'

                    def testStatus = sh(
                        script: '''
                        . venv/bin/activate
                        pytest \
                          --html=reports/report.html \
                          --self-contained-html \
                          --screenshot=only-on-failure \
                          --video=retain-on-failure \
                          --tracing=retain-on-failure
                        ''',
                        returnStatus: true
                    )

                    if (testStatus != 0) {
                        currentBuild.result = 'UNSTABLE'
                        echo 'Tests failed — screenshots, videos, and traces collected.'
                    }
                }
            }
        }
    }

    post {
        always {
            publishHTML([
                allowMissing: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Playwright Automation Report'
            ])

            archiveArtifacts artifacts: 'test-results/**', fingerprint: true
        }
    }
}