from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort,send_file
import os
import main
import create_database
import display


app = Flask(__name__)
 


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def add():
    url=request.form['url']
    main.insert_url(url)
    res=display.show()
    print(res)
    return render_template("index.html",details=res)

@app.route("/create_database")
def create():
	create_database.create()
	return redirect(url_for("home"))


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(app.run(debug=True, port=os.getenv("PORT")))