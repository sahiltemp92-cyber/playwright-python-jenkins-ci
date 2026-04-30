Playwright Python Automation with Jenkins CI
A complete, CI‑ready test automation framework using Playwright (Python), Pytest, and Jenkins.
This repository demonstrates enterprise‑grade practices like non‑blocking test failures, HTML reporting, and automatic artifact capture (screenshots, videos, traces)—all triggered automatically on every commit to main.

🚀 Features

✅ Playwright test automation with Python
✅ Pytest + Pytest‑Playwright integration
✅ Jenkins CI pipeline (Pipeline as Code)
✅ Automatic trigger on every commit to main
✅ Continues pipeline execution even if tests fail
✅ HTML test report (pytest‑html)
✅ Screenshots, videos & traces only on failures
✅ Artifacts archived and accessible from Jenkins
✅ macOS & Linux CI compatible


📁 Project Structure
playwright-python-jenkins-ci/
├── Jenkinsfile
├── README.md
├── requirements.txt
├── pytest.ini
├── playwright.config.py
├── conftest.py
├── tests/
│   ├── test_example.py
│   └── ...
├── pages/
├── utils/
└── reports/            # Generated at runtime


🧰 Tech Stack

Python 3.9+
Playwright
Pytest
Pytest‑Playwright
Pytest‑HTML
Jenkins (Pipeline CI)


✅ Prerequisites
Local Machine

Python 3.9+
Git
(macOS) Homebrew recommended

Jenkins Machine

Jenkins (LTS)
Java 17
Python 3.9+
Git
HTML Publisher Plugin installed


⚙️ Installation (Local Setup)
Groovygit clone https://github.com/<your-username>/playwright-python-jenkins-ci.gitcd playwright-python-jenkins-cipython3 -m venv venvsource venv/bin/activatepip install --upgrade pippip install -r requirements.txtplaywright installShow more lines

▶️ Running Tests Locally
ShellpytestShow more lines
With HTML report and failure artifacts:
Shellpytest \  --html=reports/report.html \  --self-contained-html \  --screenshot=only-on-failure \  --video=retain-on-failure \  --tracing=retain-on-failureShow more lines

📊 Reports & Artifacts
HTML Report

Path: reports/report.html
Published automatically in Jenkins

Failure Artifacts (Auto‑generated)
Stored under test-results/:
test-results/
├── test_name/
│   ├── screenshot.png
│   ├── video.webm
│   └── trace.zip

Artifacts are archived and downloadable from Jenkins.

🧪 CI Behavior (Important)





























ScenarioResultAll tests pass✅ Build = SUCCESSSome tests fail⚠️ Build = UNSTABLETest crash⚠️ Build continuesHTML report✅ Always generatedScreenshots/videos✅ Only on failure

The pipeline never stops because of test failures.


🔁 Jenkins CI Setup
1. Jenkinsfile
The pipeline is defined in the Jenkinsfile at the repository root.
2. GitHub Credentials

Store GitHub PAT in Jenkins → Credentials
Use it in the Pipeline SCM configuration

3. Automatic Trigger on Commit

Jenkins: “GitHub hook trigger for GITScm polling”
GitHub: Webhook pointing to
http://<jenkins-host>:8080/github-webhook/



✅ Every push to main triggers the pipeline automatically.

🧩 Jenkinsfile Highlights

Uses python3 for compatibility
Captures pytest exit code without failing the pipeline
Marks build as UNSTABLE on test failures
Publishes HTML report every time
Archives Playwright artifacts


🔐 Best Practices Followed

No credentials committed to code
Non‑interactive CI (no password prompts)
Pipeline as Code
Failure diagnostics (screenshots, videos, traces)
Deterministic and reproducible builds


🛠️ Common Commands
Shell# Show Playwright trace locallyplaywright show-trace test-results/<test-name>/trace.zipShow more lines

🧭 Roadmap / Enhancements

Parallel test execution
Flaky test retries
Allure reporting
Dockerized Jenkins agents
PR validation pipelines (Multibranch)


🤝 Contributing

Fork the repository
Create a feature branch
Push changes
Open a Pull Request


📄 License
MIT License

✨ Final Notes
This repository demonstrates a real‑world, enterprise‑grade Playwright CI pipeline suitable for:

QA teams
Automation engineers
CI/CD learning
Production pipelines

If you have questions or want enhancements, feel free to contribute or raise issues.