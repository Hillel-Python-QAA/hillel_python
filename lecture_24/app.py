from flask import Flask, jsonify, request

app = Flask(__name__)

# Зразок даних про користувачів
users = {
    "1": {"name": "Alice", "email": "alice@example.com"},
    "2": {"name": "Bob", "email": "bob@example.com"},
}


# Маршрут для отримання даних про користувача за його ідентифікатором
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


# Маршрут для створення нового користувача
@app.route("/users/create", methods=["POST"])
def create_user():
    data = request.json
    user_id = str(len(users) + 1)
    users[user_id] = {"name": data["name"], "email": data["email"]}
    return jsonify({"id": user_id}), 201


# Маршрут для видалення користувача за його ідентифікатором
@app.route("/users/delete/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return "", 204
    else:
        return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 7070
    app.run(host=host, port=port, debug=True)
