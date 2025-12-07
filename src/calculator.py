from flask import Flask, request, jsonify

app = Flask(__name__)


def add(a, b):  # FIXED: Added one extra blank line before this function (E302)
    return a + b


def subtract(a, b):  # FIXED: Added one extra blank line before this function (E302)
    return a - b


def multiply(a, b):  # FIXED: Added one extra blank line before this function (E302)
    return a * b


def divide(a, b):  # FIXED: Added one extra blank line before this function (E302)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@app.route('/calculate', methods=['POST'])
def calculate():  # FIXED: Added one extra blank line before this function (E302)
    try:
        data = request.get_json()
        operation = data['operation']
        num1 = float(data['num1'])
        num2 = float(data['num2'])

        operations = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }

        if operation not in operations:
            return jsonify({'error': 'Invalid operation'}), 400

        result = operations[operation](num1, num2)
        return jsonify({'result': result})

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception:  # FIXED: Removed the unused variable `e` (F841)
        return jsonify({'error': 'Invalid input'}), 400


@app.route('/health', methods=['GET'])
def health():  # FIXED: Added one extra blank line before this function (E302)
    return jsonify({'status': 'healthy', 'service': 'calculator-api'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# FIXED: Added one extra blank line here (E305) and ensured the file ends with a newline (W292)