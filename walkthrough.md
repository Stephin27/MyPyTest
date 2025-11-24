# Automation Practice Walkthrough

I have successfully automated the interactions with the [Automation Practice](https://rahulshettyacademy.com/AutomationPractice/) website using a **Playwright Pytest Framework** implementing the **Page Object Model (POM)** and **Allure Reporting**.

## Framework Structure

The solution is organized as follows:

```text
d:/Testing/
├── pages/
│   ├── __init__.py
│   └── practice_page.py       # Page Object encapsulating page interactions (with Allure steps)
├── tests/
│   ├── __init__.py
│   ├── conftest.py            # Pytest fixtures (setup/teardown + Screenshot on Failure)
│   └── test_practice.py       # Test cases (with Allure titles/descriptions)
├── reports/                   # Generated HTML reports
│   └── allure-report/
│       └── complete.html      # Single-file standalone report (Open this!)
├── allure-results/            # Raw Allure results
├── run_tests.ps1              # Script to run tests and generate report
├── pytest.ini                 # Pytest configuration (includes Allure settings)
├── requirements.txt           # Dependencies
└── automate_practice.py       # (Original linear script)
```

## Features

-   **Page Object Model**: Clean separation of page logic and tests.
-   **Allure Reporting**: Rich HTML reports with steps, severity, and descriptions.
-   **Screenshots**:
    -   **On Failure**: Automatically captures a full-page screenshot if a test fails.
    -   **Explicit**: Can be added manually to any test step (example in `test_web_table`).
-   **Single-File Report**: Generates a portable `complete.html` file.

## Execution & Reporting

To run the tests and automatically generate a **standalone** Allure HTML report, use the provided PowerShell script:

```powershell
./run_tests.ps1
```

This script will:
1.  Run the tests using `pytest`.
2.  Generate the standard Allure report.
3.  **Combine** the report into a single file: `reports/allure-report/complete.html`.

## Viewing the Report

You can now open the report **directly** from your file system without any "Loading..." errors:

**Open File**: `reports/allure-report/complete.html`

## Manual Execution

1.  **Run Tests**:
    ```bash
    pytest
    ```
2.  **Generate Report**:
    ```bash
    allure generate allure-results -o reports/allure-report --clean
    ```
3.  **Combine (Optional)**:
    ```bash
    allure-combine reports/allure-report
    ```
