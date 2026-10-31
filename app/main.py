from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "name": "Apprendre Docker", "done": False},
    {"id": 2, "name": "Apprendre Ansible", "done": True}
]

@app.route("/")
def home():
    return jsonify({
        "message": "TaskManager API",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
