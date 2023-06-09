import pandas as pandas
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Adding Stations from station file to render it on HTML
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


# Adding app route method using decorator
@app.route("/")
def Home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>/")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {'Station': station,
            'Data': date,
            'Temp': temperature}


@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result


@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(year)].to_dict(orient="records")
    return result


# This will allow you to see error in the webpage.
if __name__ == "__main__":
    app.run(debug=True)
