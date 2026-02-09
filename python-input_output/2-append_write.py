def append_write(filename="", text=""):
    with open(filename, "a") as file:
        file.write(text)
