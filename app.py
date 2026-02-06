from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students_data = []   # Temporary storage


# ---------- Home Page ----------
@app.route("/")
def index():
    return render_template("index.html")


# ---------- Register Student ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        course = request.form.get("course")

        students_data.append({
            "name": name,
            "email": email,
            "course": course
        })

        return redirect(url_for("students"))

    return render_template("register.html")


# ---------- Students List ----------
@app.route("/Students")
def students():
    return render_template("students.html", students=students_data)
