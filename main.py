from flask import Flask, jsonify, request, render_template
from flask.wrappers import Response

# Create a new instance of the Flask class
app: Flask = Flask(__name__)

# Define route for the root URL ("/")
@app.route('/')
def home() -> str:
    # Render and return the 'home.html' template when this route is accessed
    return render_template('home.html')

# Define route for '/armstrong' URL and specify that it only responds to POST requests
@app.route('/armstrong', methods=['POST'])
def armstrong() -> Response:
    # Get 'number' from the POST request's form data and convert it to an integer
    n: int = int(request.form.get('number'))

    # Initial calculation setup for Armstrong number
    sum: int = 0
    order: int = len(str(n))
    copy_n: int = n

    # Calculate the sum of the number's digits each raised to the power of the number's length
    while n > 0:
        digit: int = n % 10
        sum += digit ** order
        n = n // 10

    # Create result dictionary based on whether the number is an Armstrong number or not
    result: dict
    if sum == copy_n:
        result = {
            "number": copy_n,
            "armstrong": True,
            "ip": "127.0.0.1/5000"
        }
    else:
        result = {
            "number": copy_n,
            "armstrong": False,
            "ip": "127.0.0.1/5000"
        }

    # Return the result as a JSON response
    return jsonify(result)

# Run the application only when the script is executed directly (not imported as a module)
if __name__ == '__main__':
    app.run(debug=True)
