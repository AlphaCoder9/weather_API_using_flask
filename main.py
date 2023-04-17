import pandas as pandas
from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


# Adding app route method using decorator
@app.route("/")
def Home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>/")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {'Station': station,
            'Data': date,
            'Temp': temperature}


# This will allow you to see error in the webpage.
if __name__ == "__main__":
    app.run(debug=True)
