import os, sys

from flask import Flask, render_template, request, session, redirect, url_for
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from database import db
from models import User

app = Flask(__name__)
app.config.from_envvar('APP_SETTINGS')

#def login_required(f):


@app.route("/")
@app.route("/index.html")
def index():
	user_name = ""
	user_name = user_name.capitalize()
	return render_template("index.html", user_name=user_name)

@app.route("/signup", methods=["POST", "GET"])
def signup():
	if request.method == "POST":
		errorMessages = []
		successMessages = []
		#ensure required fields are submitted
		if not request.form.get("username"):
			errorMessages.append("Username is required!")

		if not request.form.get("email"):
			errorMessages.append("Email is required!")
		
		if not request.form.get("password"):
			errorMessages.append("Password is required!")

		if not request.form.get("confirm-password"):
			errorMessages.append("Confirm Password is required!")

		if errorMessages != []:
			return render_template("signup.html", errorMessages=errorMessages)

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

		#ensure email doesn't exist
		emails = db.query(User).filter(User.email==request.form.get("email")).count()
		
		if emails != 0:
			errorMessages.append("Email address already exists!")
			return render_template("signup.html", errorMessages=errorMessages)

		#create new user
		newUser = User(username=request.form.get("username"), email=request.form.get("email"), password=generate_password_hash(request.form.get("password")))
		db.add(newUser)
		db.commit()
		successMessages.append(f"You have registered successfully!")
		return render_template("signup.html", successMessages=successMessages)

	return render_template("signup.html")

@app.route("/login", methods=["POST", "GET"])
def login():
	errorMessages = []

	if request.method == "POST":
		if not request.form.get("email"):
			errorMessages.append("Username is required!")
		
		if not request.form.get("password"):
			errorMessages.append("Password is required!")

		if errorMessages != []:
			return render_template("login.html", errorMessages=errorMessages)

		user = db.query(User).filter(User.email == request.form.get("email")).count()
		#WIP check hash
		password = db.query(User).filter(User.password == request.form.get("password")).count()
		print(user, file=sys.stderr)
		print(password, file=sys.stderr)
		
		if user == 1 or password == 1:
			errorMessages.append("Your username or password are not correct!")		
			return render_template("login.html", errorMessages=errorMessages)
		else:
			return redirect(url_for('index'))

	return render_template("login.html")

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