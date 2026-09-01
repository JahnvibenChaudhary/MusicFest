from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>MusicFest</h1>
    <p>Music festival booking and management application.</p>
    <a href="/login">Customer Login</a>
    <br>
    <a href="/admin">Admin Dashboard</a>
    """


@app.route("/login")
def login():
    return """
    <h1>Customer Login</h1>
    <p>MusicFest customer login page.</p>
    <form>
        <input type="email" placeholder="Email Address">
        <br><br>
        <input type="password" placeholder="Password">
        <br><br>
        <button type="submit">Sign In</button>
    </form>
    """


@app.route("/admin")
def admin():
    return """
    <h1>Admin Dashboard</h1>
    <p>MusicFest administration area.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
