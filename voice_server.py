from flask import Flask, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.get("/")
def home():
    return jsonify({
        "app": "Free Calling",
        "status": "online"
    })

@socketio.on("join")
def join(data):
    user = data.get("user", "unknown")
    emit("user_joined", {"user": user}, broadcast=True)

@socketio.on("signal")
def signal(data):
    emit("signal", data, broadcast=True, include_self=False)

@socketio.on("disconnect")
def disconnect():
    emit("user_left", {}, broadcast=True)

socketio.run(app, host="0.0.0.0", port=5001)
