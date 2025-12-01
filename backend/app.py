from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import sys
import os

app = Flask(__name__)
CORS(app)

RUNNER_PATH = os.path.dirname(os.path.abspath(__file__))

@app.route("/execute", methods=["POST"])
def execute():
    data = request.get_json()
    code = data.get("code", "")
    lang = data.get("lang", "python").lower()

    if lang == "python":
        runner_file = os.path.join(RUNNER_PATH, "runner.py")
        exe = sys.executable
    elif lang == "c":
        runner_file = os.path.join(RUNNER_PATH, "runner_c.py")
        exe = sys.executable
    elif lang == "javascript":
        runner_file = os.path.join(RUNNER_PATH, "runner_js.py")
        exe = sys.executable
    else:
        return jsonify({"result": f"Error: Runner for {lang} not found."})

    if not os.path.exists(runner_file):
        return jsonify({"result": f"Error: Runner for {lang} not found."})

    try:
        result = subprocess.run(
            [exe, runner_file, "-c", code],
            capture_output=True,
            text=True,
            timeout=5
        )
        output = result.stdout + result.stderr
    except Exception as e:
        output = str(e)

    return jsonify({"result": output})


if __name__ == "__main__":
    app.run(port=5000)
