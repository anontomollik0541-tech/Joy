from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "status": "online",
        "message": "Joy API is working"
    })

@app.get("/hello")
def hello():
    return jsonify({
        "message": "Hello from Joy API"
    })

app.run(host="0.0.0.0", port=5000)
