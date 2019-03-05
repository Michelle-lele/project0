from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/template-leia")
def template_leia():
	return render_template("template-leia.html")

@app.route("/template-shrek")
def template_shrek():
	return render_template("template-shrek.html")

@app.route("/template-jbond")
def template_jbond():
	return render_template("template-jbond.html")

if __name__ == '__main__':
    app.run(debug=True, port=8080)