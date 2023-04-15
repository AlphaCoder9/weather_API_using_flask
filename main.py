from flask import Flask, render_template

app = Flask(__name__)


# Adding app route method using decorator
@app.route("/")
def Home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>/")
def about(station, date):
    temperature = 50
    return {'Station': station,
            'Data': date,
            'Temp': temperature}


# This will allow you to see error in the webpage.
if __name__ == "__main__":
    app.run(debug=True)
