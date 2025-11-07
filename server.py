from flask import Flask, send_from_directory, request
import subprocess
import os

app = Flask(__name__)

SCRIPT_PATH = os.path.abspath('./pipeline2.sh')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/run-script')
def run_script():
    if request.args.get('token') != 'airi_rob_2025':
       return {"error": "Unauthorized"}, 403
    try:
        subprocess.Popen([SCRIPT_PATH])
        return {"status": "ok"}, 200
    except Exception as e:
        print(f"Ошибка: {e}")
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
