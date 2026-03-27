import sys
import os


def generate_invitations(template, attendees):
    if not template:
        print("Template is empty, ", file=sys.stderr, end='')
    elif not attendees:
        print("No data provided, ", file=sys.stderr, end='')
    elif not isinstance(template, str):
        print(f"template is {type(template)}, string expected, ", file=sys.stderr, end='')
    elif not isinstance(attendees, list):
        print(f"template is {type(attendees)}, a list of dictionnary expected, ", file=sys.stderr, end='')
    else:
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
        return
    print("no output files generated.", file=sys.stderr)
