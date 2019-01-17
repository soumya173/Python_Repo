from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/template/<username>")
def templates(username):
	return render_template("index.html", name=username)

@app.route("/")
def index():
	return "This is the first line"

@app.route("/admin")
def admin():
	return "This is ADMIN"

@app.route("/success/<name>")
def success(name):
	return "Welcome %s bro" %name

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST" :
		username = request.form["username"]
		return redirect(url_for("success", name=username))
	else:
		username = request.args.get("username")
		return redirect(url_for("success", name=username))

if __name__ == "__main__":
	app.run()