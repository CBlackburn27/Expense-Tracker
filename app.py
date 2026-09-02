from flask import Flask, render_template  # type: ignore        #imports flask library
from flask_sqlalchemy import SQLAlchemy
from datetime import date


app = Flask(__name__)   # creates an instance of the Flask class


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"  # sets the database URI for SQLAlchemy to use a SQLite database named "data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # disables SQLAlchemy event system to save resources
db = SQLAlchemy(app)  # creates an instance of the SQLAlchemy class and associates it with the Flask app

with app.app_context():  # creates an application context to allow database operations
    db.create_all()  # creates all the database tables


@app.route("/")  # defines a route for the root URL ("/") of the application
def index():
    return render_template("index.html")  # renders the "index.html" template when the root URL is accessed

if __name__ == "__main__":
    app.run(debug=True, port=5000)
