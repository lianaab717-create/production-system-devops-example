from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# Simulated in-memory DB
DATA = {
    "items": [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"}
    ]
}

@app.route("/healthz", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(DATA["items"]), 200

@app.route("/items", methods=["POST"])
def add_item():
    new_item = request.json
    new_item["id"] = len(DATA["items"]) + 1
    DATA["items"].append(new_item)
    return jsonify(new_item), 201

if __name__ == "__main__":
    # Production-ready: set host=0.0.0.0 to bind container IP
    app.run(host="0.0.0.0", port=5000)
