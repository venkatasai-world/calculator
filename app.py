from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    n1 = data.get("n1", 0)
    n2 = data.get("n2", 0)
    op = data.get("op", "")

    try:
        n1 = float(n1)
        n2 = float(n2)

        if op == "+":
            result = n1 + n2
        elif op == "-":
            result = n1 - n2
        elif op == "*":
            result = n1 * n2
        elif op == "/":
            if n2 == 0:
                result = "Cannot divide by zero"
            else:
                result = n1 / n2
        elif op == "%":
            result = n1 % n2
        else:
            result = "Invalid operation"
    except Exception as e:
        result = f"Error: {e}"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
