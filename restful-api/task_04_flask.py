#!/usr/bin/python3
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route("/")
def home():
    """Home route"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Return all usernames as a list"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return API status"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return user data by username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user"""
    try:
        new_user = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not new_user:
        return jsonify({"error": "Invalid JSON"}), 400

    username = new_user.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run(debug=True)
