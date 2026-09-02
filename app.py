from flask import Flask, render_template  # type: ignore        #imports flask library

app = Flask(__name__)   # creates an instance of the Flask class

@app.route("/")  # defines a route for the root URL ("/") of the application
def index():
    return render_template("index.html")  # renders the "index.html" template when the root URL is accessed

if __name__ == "__main__":
    app.run(debug=True, port=5000)
