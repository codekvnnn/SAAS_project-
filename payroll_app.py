from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate_payroll', methods=['POST'])
def calculate_payroll():
    data = request.json
    hours_worked = data.get('hours_worked', 0)
    hourly_rate = data.get('hourly_rate', 0)

    # Basic payroll calculation
    total_pay = hours_worked * hourly_rate

    return jsonify({
        'total_pay': total_pay
    })

if __name__ == '__main__':
    app.run(debug=True)
