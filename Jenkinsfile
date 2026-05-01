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
                        echo 'Some tests failed. Continuing pipeline and publishing reports.'
                    }
                }
            }
        }
    }

    post {
        always {
            publishHTML([
                allowMissing: true,
                alwaysLinkToLastBuild: true,   // ✅ REQUIRED
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Playwright Automation Report'
            ])

            archiveArtifacts artifacts: 'test-results/**', allowEmptyArchive: true, fingerprint: true
        }
    }
}