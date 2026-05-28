import re

def extract_emails(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            content = f.read()

        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = re.findall(email_pattern, content)
        unique_emails = list(set(emails))

        if not unique_emails:
            print("No email addresses found.")
            return

        with open(output_file, "w") as f:
            for email in unique_emails:
                f.write(email + "\n")

        print(f"Found {len(unique_emails)} email(s). Saved to '{output_file}'.")
        for email in unique_emails:
            print(f"  - {email}")

    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")

# Usage: put some text with emails in 'input.txt', run the script
extract_emails("input.txt", "emails_found.txt")