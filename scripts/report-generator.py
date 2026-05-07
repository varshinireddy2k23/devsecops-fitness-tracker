import os
import json
import pandas as pd

REPORTS = {
    "dependency-report.json": "DependencyScan",
    "trivy-report.json": "TrivyScan",
    "checkov-report.json": "CheckovScan"
}

output_file = "reports/security-report.xlsx"

writer = pd.ExcelWriter(output_file, engine="openpyxl")

for file_name, sheet_name in REPORTS.items():

    path = os.path.join("reports", file_name)

    if os.path.exists(path):

        try:
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)

            normalized = pd.json_normalize(data)

            if normalized.empty:
                normalized = pd.DataFrame(
                    [{"message": "No vulnerabilities found"}]
                )

            normalized.to_excel(
                writer,
                sheet_name=sheet_name,
                index=False
            )

            print(f"{file_name} converted successfully")

        except Exception as error:
            print(f"Error processing {file_name}")
            print(error)

writer.close()

print("Excel report generated successfully")