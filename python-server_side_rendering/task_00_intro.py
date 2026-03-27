import sys
import os


def generate_invitations(template: str, attendees: [{}]):
    if not template:
        print("Template is empty, no output files generated.", file=sys.stderr)
        return
    if not attendees:
        print("No data provided, no output files generated.", file=sys.stderr)

    for i, attendee in enumerate(attendees, 1):
        buffer = template
        for key, value in attendee.items():
            try:
                buffer = buffer.replace('{' + key + '}', value)
            except Exception:
                buffer = buffer.replace('{' + key + '}', f"{key}:N/A")

        if not os.path.exists(f"output_{i}.txt"):
            with open(f"output_{i}.txt", mode="w") as file:
                file.write(buffer)
