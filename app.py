from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == "customer@musicfest.com" and password == "123456":
            return redirect(url_for("home"))

        error = "Invalid email or password."

    return render_template("login.html", error=error)


@app.route("/festival")
def festival():
    return render_template("festival.html")


@app.route("/tickets")
def tickets():
    return render_template("tickets.html")


@app.route("/payment", methods=["GET", "POST"])
def payment():
    if request.method == "POST":
        return redirect(url_for("confirmation"))

    return render_template("payment.html")


@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True)
