import sys
import os


def generate_invitations(template, attendees):
    errTxt = ", no output files generated."
    if not template or template == "":
        print(f"Template is empty{errTxt}", file=sys.stderr)
    elif not attendees or attendees == []:
        print(f"No data provided{errTxt}", file=sys.stderr)
    elif not isinstance(template, str):
        print(f"template is {type(template)}, string expected{errTxt}", file=sys.stderr)
    elif not isinstance(attendees, list):
        print(f"template is {type(attendees)}, a list of dictionnary expected{errTxt}", file=sys.stderr)
    else:
        for i, attendee in enumerate(attendees, 1):
            if not isinstance(attendee, dict):
                print(f"template is {type(attendee)}, a list of dictionnary expected{errTxt}", file=sys.stderr)
                return
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
