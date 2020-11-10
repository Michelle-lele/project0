import os, sys

from flask import (
	g,
	Flask,
	redirect,
	render_template,
	request,
	session,
	url_for
	)
from flask_session import Session
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from database import db
from models import User
from datetime import timedelta

app = Flask(__name__)
app.config.from_envvar('APP_SETTINGS')

app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=10)
Session(app)

def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if user_id not in session:
			return redirect(url_for('login', next=request.url))
		return f(*args, **kwargs)
	return decorated_function

@login_required
@app.route("/")
@app.route("/index.html")
def index():
	return render_template("index.html")

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

	if 'user_id' in session:
		return redirect(url_for('index'))

	if request.method == "POST":
		if not request.form.get("email"):
			errorMessages.append("Username is required!")
		
		if not request.form.get("password"):
			errorMessages.append("Password is required!")

		if errorMessages != []:
			return render_template("login.html", errorMessages=errorMessages)

		user_count = db.query(User).filter(User.email == request.form.get("email")).count()
		user = db.query(User).filter(User.email == request.form.get("email"))
		
		if user_count != 1 or not check_password_hash(user[0].password, request.form.get("password")):
			errorMessages.append("Your username or password are not correct!")		
			return render_template("login.html", errorMessages=errorMessages)
		else:
			session['user_id'] = user[0].id
			#g.user = user[0]
			return redirect(url_for('index'))

	return render_template("login.html")

@app.route("/logout", methods = ['POST', 'GET'])
def logout():
	session.clear()
	#g.user = None
	return redirect(url_for("login"))

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