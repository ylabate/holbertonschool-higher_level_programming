#!/usr/bin/python3
from flask import Flask, request

app = Flask(__name__)
users = dict()


@app.route("/")
def home():
    """
    Home endpoint that returns a welcome message.

    Returns:
        str: A welcome message for the Flask API.
    """
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """
    Status endpoint that returns the API status.

    Returns:
        str: The status of the API ("OK").
    """
    return "OK"


@app.route("/data")
def data():
    """
    Data endpoint that returns a list of all usernames.

    Returns:
        list: A list of all usernames in the users dictionary.
    """
    return list(users.keys())


@app.route("/users/<username>")
def user(username):
    """
    Get a specific user by username.

    Args:
        username (str): The username of the user to retrieve.

    Returns:
        dict: The user data if found, or an error message with 404 status
        if not found.
    """
    if username in users:
        return users[username]
    else:
        return {"error": "User not found"}, 404


@app.post("/add_user")
def add_user():
    """
    Add a new user to the API.

    Expects a JSON payload with the following fields:
    - username (str): The unique username for the user.
    - name (str): The user's full name.
    - age (int): The user's age.
    - city (str): The user's city.

    Returns:
        tuple: A tuple containing:
            - dict: Response message with the added user data and status code.
            - int: HTTP status code (201 for success, 400 for invalid input,
            409 for duplicate username).
    """
    dictionnary = request.get_json()
    if not request.is_json or type(dictionnary) is not dict:
        return {"error": "Invalid JSON"}, 400

    if "username" not in dictionnary:
        return {"error": "Username is required"}, 400

    if (
        "name" not in dictionnary
        and "age" not in dictionnary
        and "city" not in dictionnary
    ):
        return {"error": "Invalid JSON"}, 400

    if dictionnary["username"] in users:
        return {"error": "Username already exists"}, 409
    users[dictionnary["username"]] = {
        "username": dictionnary["username"],
        "name": dictionnary["name"],
        "age": dictionnary["age"],
        "city": dictionnary["city"],
    }
    return {
        "message": "User added",
        "user": dictionnary,
    }, 201


if __name__ == "__main__":
    app.run(host="0.0.0.0")
