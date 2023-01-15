from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/add", methods=['POST'])
def add():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    return jsonify({"msg": num1+num2, "status": 200})


@app.route("/sub", methods=['POST'])
def sub():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    return jsonify({"msg": abs(num1 - num2), "status": 200})


@app.route("/mul", methods=['POST'])
def mul():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    return jsonify({"msg": num1 * num2, "status": 200})


@app.route("/div", methods=['POST'])
def div():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    if num2 == 0:
        return jsonify({"msg": "Invalid Data, can't be divisible by 0"})
    return jsonify({"msg": num1 / num2, "status": 200})


if __name__ == "__main__":
    app.run(debug=True)
