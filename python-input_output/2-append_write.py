def write_file(filename="", text=""):
    with open(filename, "a") as file:
        file.write(text)
