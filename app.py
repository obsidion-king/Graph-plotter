# main.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/plot', methods=['POST'])
def plot():
    data = request.json
    x = [float(i) for i in data['x'].split(",")]
    y = [float(i) for i in data['y'].split(",")]
    axis_x = float(data['axis_x'])
    axis_y = float(data['axis_y'])

    x_output = []
    y_output = []

    for value in x:
        orig = value
        if value < 1:
            value *= 10
        x_output.append(f"Plot {round(orig, 3)} at {round(value * axis_x, 3)}CM on the x axis")

    for value in y:
        orig = value
        if value < 1:
            value *= 10
        y_output.append(f"Plot {round(orig, 3)} at {round(value * axis_y, 3)}CM on the y axis")

    return jsonify({'x_axis': x_output, 'y_axis': y_output})

if __name__ == '__main__':
    app.run(debug=True)
