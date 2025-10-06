from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# ห้ามมี app.run() ถ้าใช้ gunicorn
