import openpyxl
from config import Config

data = [
    ["Country"],
    ["India"],
    ["United States (USA)"],
    ["United Kingdom (UK)"],
    ["Canada"],
    ["Australia"],
    ["Germany"],
    ["France"],
    ["Italy"],
    ["Spain"],
    ["Japan"]
]

# Ensure directory exists
Config.DATA_DIR.mkdir(exist_ok=True)

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Countries"

for row in data:
    ws.append(row)

file_path = Config.DATA_DIR / "countries.xlsx"
wb.save(file_path)
print(f"Excel file created successfully at {file_path}")
