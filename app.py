from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/create_project')
def create_project():
    return render_template("create_project.html")

if __name__ == "__main__":
    app.run(debug=True)
