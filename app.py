from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# LOGIN PAGE (First open)
@app.route('/')
def login():
    return render_template("login.html")


# After login → Dashboard
@app.route('/dashboard', methods=['POST'])
def dashboard():
    username = request.form.get("username")
    return render_template("dashboard.html", username=username)


# Create Project Page
@app.route('/create_project')
def create_project():
    return render_template("create_project.html")


# Project Members Page
@app.route('/project_members', methods=['POST'])
def project_members():
    project_name = request.form.get("project_name")
    print("DEBUG:", project_name) 
    return render_template("project_members.html", project_name=project_name)


if __name__ == "__main__":
    app.run(debug=True)
