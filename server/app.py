from flask import Flask

app = Flask(__name__)

# 1. Index Route (Base URL: "/")
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# 2. Print String Route (URL Format: "/print/<parameter>")
@app.route("/print/<string:param>")
def print_string(param):
    print(param)  # Print the string to the console
    return param  # Return the string as plain text

# 3. Count Numbers Route (URL Format: "/count/<parameter>")
@app.route("/count/<int:param>")
def count(param):
    # Generate a list of numbers from 0 to param-1, join them with newlines, and add a final newline
    result = "\n".join(str(i) for i in range(param)) + "\n"  # Add a trailing newline
    return result  # Return the result as plain text

# 4. Math Operations Route (URL Format: "/math/<num1>/<operation>/<num2>")
@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else "Division by zero error"
    elif operation == '%':
        result = num1 % num2
    else:
        result = "Invalid operation"
    
    return str(result)  # Return the result as plain text

# Main entry point for running the Flask app
if __name__ == '__main__':
    app.run(port=5555, debug=True)
