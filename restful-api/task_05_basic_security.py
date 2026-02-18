#!/usr/bin/python3
"""
Flask API with JWT Authentication and Basic Security.

This module implements a secure REST API with JWT authentication
and password hashing using werkzeug. It provides endpoints for user login,
protected resources, and admin-only access.

Key features:
- User authentication with hashed passwords
- JWT token generation and validation
- Role-based access control (admin vs regular users)
- Comprehensive error handling for JWT operations
"""

from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-super-secret"
jwt = JWTManager(app)

users = dict()


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle unauthorized access (missing or invalid token).

    Args:
        err: The error message from JWT manager.

    Returns:
        tuple: A JSON response with error message and 401 status code.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid token errors.

    Args:
        err: The error message from JWT manager.

    Returns:
        tuple: A JSON response with error message and 401 status code.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired token errors.

    Args:
        err: The error message from JWT manager.

    Returns:
        tuple: A JSON response with error message and 401 status code.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle revoked token errors.

    Args:
        err: The error message from JWT manager.

    Returns:
        tuple: A JSON response with error message and 401 status code.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle fresh token requirement errors.

    Args:
        err: The error message from JWT manager.

    Returns:
        tuple: A JSON response with error message and 401 status code.
    """
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/login", methods=["POST"])
def login():
    """
    Authenticate a user and return a JWT access token.

    Expects a JSON payload with:
    - username (str): The user's username
    - password (str): The user's password

    The password is verified against the stored hashed password using
    werkzeug's check_password_hash function.

    Returns:
        tuple: A JSON response containing the access token if successful,
               or an error message with 401 status code if authentication fail.

    Status Codes:
        200: Login successful, access token provided
        401: Invalid username or password
    """
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username not in users or not check_password_hash(
        users[username]["password"], password
    ):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Protected endpoint requiring valid JWT authentication.

    This endpoint can only be accessed with a valid JWT token in the
    Authorization header. The token is automatically validated by the
    @jwt_required() decorator.

    Returns:
        tuple: A JSON response with success message and 200 status code.

    Status Codes:
        200: Access granted (valid token)
        401: Missing or invalid token
    """
    return jsonify({"msg": "JWT Auth: Access Granted"}), 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Admin-only protected endpoint requiring JWT and admin privileges.

    This endpoint requires both a valid JWT token and admin privileges.
    The current user is identified from the JWT token, and their admin
    status is checked from the users database.

    Returns:
        tuple: A JSON response with success message and 200 status code
               if user is admin, or error message with 403 status code
               if user lacks admin privileges.

    Status Codes:
        200: Access granted (valid token + admin user)
        401: Missing or invalid token
        403: Valid token but user is not admin
    """
    current_user = get_jwt_identity()

    if users[current_user]["is_admin"]:
        return jsonify({"msg": "Admin Access: Granted"}), 200

    return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    users["test"] = {
        "username": "test",
        "password": generate_password_hash("test"),
        "is_admin": True,
    }
    users["test_non_admin"] = {
        "username": "test_non_admin",
        "password": generate_password_hash("test_pas_admin"),
        "is_admin": False,
    }
    app.run(host="0.0.0.0")
