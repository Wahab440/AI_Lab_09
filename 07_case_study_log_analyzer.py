import csv
from pathlib import Path

# Paths
base_path = Path(__file__).parent
input_csv = base_path / "students.csv"
report_file = base_path / "report.txt"

underperforming_students = []
invalid_email_students = []

# Read data
with open(input_csv, encoding="utf-8") as f:
    for row in csv.DictReader(f):
        name = row["name"].strip()
        marks = int(row["marks"])
        email = row["email"].strip()

        if marks < 12:
            underperforming_students.append((name, marks))

        # Simple email check: must contain '@' and a dot in the domain part.
        if "@" not in email or "." not in email.split("@")[-1]:
            invalid_email_students.append((name, email))

# Build report
report = [
    "Student Support Report",
    "=" * 22,
    "",
    "Rule 1: Underperforming = marks < 12",
    "",
    "Underperforming Students:",
]

if underperforming_students:
    for name, marks in underperforming_students:
        report.append(f"- {name}: {marks}")
else:
    report.append("- None")

report.extend(["", "Invalid Email Records:"])

if invalid_email_students:
    for name, email in invalid_email_students:
        report.append(f"- {name}: {email}")
else:
    report.append("- None")

# Write report
report_file.write_text("\n".join(report) + "\n", encoding="utf-8")

# Summary
print("Analysis completed successfully.\n")
print(f"Total underperforming students: {len(underperforming_students)}")
print(f"Total invalid emails: {len(invalid_email_students)}")
print(f"Report: {report_file.name}")





