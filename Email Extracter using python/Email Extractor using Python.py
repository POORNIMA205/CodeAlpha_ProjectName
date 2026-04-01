import re

input_file = "input.txt"
output_file = "C:\\Users\\poornima\\Desktop\\emails.txt"

with open(input_file, "r") as file:
    content = file.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", content)

print("Extracted Emails:")
for email in emails:
    print(email)

with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("\nEmails saved successfully on Desktop!")