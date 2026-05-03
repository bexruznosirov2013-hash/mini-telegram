from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

messages = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    msg = data.get("message")
    if msg:
        messages.append(msg)
    return jsonify({"ok": True})

@app.route("/messages")
def get_messages():
    return jsonify(messages)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)