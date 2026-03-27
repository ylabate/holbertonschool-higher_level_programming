#!/usr/bin/python3
import sys


def generate_invitations(template, attendees):
    errTxt = ", no output files generated."
    if not template or template == "":
        print(f"Template is empty{errTxt}", file=sys.stderr)
    elif not attendees or attendees == []:
        print(f"No data provided{errTxt}", file=sys.stderr)
    elif not isinstance(template, str):
        print(f"template is the wrong type{errTxt}", file=sys.stderr)
    elif not isinstance(attendees, list):
        print(f"attendees is the wrong type{errTxt}", file=sys.stderr)
    else:
        for i, attendee in enumerate(attendees, 1):
            if not isinstance(attendee, dict):
                print(f"template is the wrong type{errTxt}", file=sys.stderr)
                return
            buffer = template
            for key, value in attendee.items():
                try:
                    buffer = buffer.replace(key, value)
                except Exception:
                    buffer = buffer.replace(key, key + ":N/A")
            with open(f"output_{i}.txt", mode="w") as file:
                file.write(buffer)
        return
