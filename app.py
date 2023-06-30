from flask import Flask, render_template, request

app = Flask(__name__)

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        x = float(request.form.get('x'))
        y = float(request.form.get('y'))
        operation = request.form.get('operation')

        calculator = Calculator()

        if operation == 'add':
            result = calculator.add(x, y)
        elif operation == 'subtract':
            result = calculator.subtract(x, y)
        elif operation == 'multiply':
            result = calculator.multiply(x, y)
        elif operation == 'divide':
            result = calculator.divide(x, y)

        return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
