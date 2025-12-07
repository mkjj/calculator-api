from flask import Flask, request, jsonify

app = Flask(__name__)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@app.route('/calculate', methods=['POST'])
def calculate():
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
    except Exception:
        return jsonify({'error': 'Invalid input'}), 400


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'calculator-api'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
