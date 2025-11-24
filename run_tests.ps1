# Run Pytest
Write-Host "Running Tests..."
pytest

# Generate Allure Report
Write-Host "Generating Allure Report..."
allure generate allure-results -o reports/allure-report --clean

# Combine into Single File
Write-Host "Combining report into single file..."
d:/Testing/.venv/Scripts/allure-combine.exe reports/allure-report

Write-Host "Test Run Completed."
Write-Host "Single-file report is saved as: reports/allure-report/complete.html"
Write-Host "You can open this file directly in any browser."
