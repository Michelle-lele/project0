from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
	user_name = "genadi"
	user_name = user_name.capitalize()
	return render_template("index.html", user_name=user_name)

@app.route("/signup.html", methods=["POST", "GET"])
def signup():
	user_email = request.form.get("email")
	return render_template("signup.html", user_email=user_email)


@app.route("/template-leia.html")
def template_leia():
	return render_template("template-leia.html")

@app.route("/template-shrek.html")
def template_shrek():
	return render_template("template-shrek.html")

@app.route("/template-jbond.html")
def template_jbond():
	return render_template("template-jbond.html")

if __name__ == '__main__':
    app.run(debug=True, port=8080)