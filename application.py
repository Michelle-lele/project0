from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
	username = "genadi"
	username = username.capitalize()
	return render_template("index.html", username=username)

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