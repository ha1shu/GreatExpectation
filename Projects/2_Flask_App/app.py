from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Thank you , you are on the home page"

@app.route("/aboutt")
def about():
    return "Hey You clicked About!!"

@app.route("/contact")
def contact():
    return "Hey bro , Are you want to contact us"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)