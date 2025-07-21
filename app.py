# main.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def plot():
    if request.method == "POST":
        try:
            x = [float(i) for i in request.form["x"].split(",")]
            y = [float(i) for i in request.form["y"].split(",")]
            axis_x = float(request.form["axis_x"])
            axis_y = float(request.form["axis_y"])


            x_output = []
            y_output = []

            for value in x:
                orig = value
                if value < 1:
                    value *= 10
                x_output.append(
                    f"Plot {round(orig, 3)} at {round(value * axis_x, 3)}CM on the x axis"
                )

            for value in y:
                orig = value
                if value < 1:
                    value *= 10
                y_output.append(
                    f"Plot {round(orig, 3)} at {round(value * axis_y, 3)}CM on the y axis"
                )

            return render_template("index.html", x_output=x_output, y_output=y_output)
        
        except (KeyError, ValueError, TypeError) as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
