import re

emails = [
    "student1@university.edu",
    "student.two@uni.edu",
    "wrong-email.com",
    "@nouser.edu",
    "name@domain",
]

email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

for email in emails:
    if re.fullmatch(email_pattern, email):
        print(f"VALID   -> {email}")
    else:
        print(f"INVALID -> {email}")





