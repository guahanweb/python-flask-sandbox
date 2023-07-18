from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.get("/")
def home():
    return render_template('home.html', title="Home")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
