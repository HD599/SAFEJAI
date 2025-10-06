from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# ไม่ต้องมี app.run() ถ้าใช้ Gunicorn
