import os 

from flask import Flask, render_template, request, session
from database import db
from models import User

app = Flask(__name__)
app.config.from_envvar('APP_SETTINGS')

@app.route("/")
@app.route("/index.html")
def index():
	user_name = ""
	user_name = user_name.capitalize()
	return render_template("index.html", user_name=user_name)

@app.route("/signup.html", methods=["POST", "GET"])
def signup():
	if request.method == "POST":
		errorMessages= []
		#ensure required fields are submitted
		if not request.form.get("username"):
			errorMessages.append("Username is required!")
		
		if not request.form.get("password"):
			errorMessages.append("Password is required!")

		if not request.form.get("confirm-password"):
			errorMessages.append("Confirm Password is required!")

		if errorMessages != []:
			return render_template("signup.html", errorMessages=errorMessages)

		#ensure username has no spaces
		if ' ' in request.form.get("username"):
			errorMessages.append("Username should not contain spaces!")

		#ensure passwords match
		if request.form.get("password") != request.form.get("confirm-password"):
			errorMessages.append("Passwords don't match!")

		if errorMessages != []:
			return render_template("signup.html", errorMessages=errorMessages)

		#ensure password has minimum 8 characters, including characters & numbers
		if len(request.form.get("password")) < 8:
			errorMessages.append("Password should be at least 8 symbols!")
		if not request.form.get("password").isalnum():
			errorMessages.append("Password should contain at least 1 letter or digit!")

		if errorMessages != []:
			return render_template("signup.html", errorMessages=errorMessages)

		#ensure username doesn't exist
		username = db.query(User.username.label(request.form.get("username"))).all()
		#print(username, file=sys.stderr)
		if len(username) != 0:
			errorMessages.append("Username already exists!")
			return render_template("signup.html", errorMessages=errorMessages)

		#create new user
		newUser = User(username=request.form.get("username"), password=request.form.get("password"))
		db.commit()

	return render_template("signup.html")


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