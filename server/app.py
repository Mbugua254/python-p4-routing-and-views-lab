from flask import Flask

app = Flask(__name__)

# Base URL route
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# Route to print a string
@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)  
    return parameter  

# Route to count numbers up to a parameter
@app.route("/count/<int:parameter>")
def count(parameter):
    # Generate numbers from 0 to parameter - 1 (inclusive), ensuring trailing newline
    numbers = "\n".join(str(i) for i in range(parameter)) + "\n"
    return numbers, 200

# Route to perform math operations
@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"

    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid Operation."

    return str(result), 200


if __name__ == "__main__":
    app.run(debug=True)
