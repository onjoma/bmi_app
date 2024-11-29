from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def bmi_calculate():
    bmi = ""
    if request.method == 'POST' and 'weight' in request.form and 'feet' in request.form and 'inches' in request.form:
        weight_lbs = float(request.form.get('weight'))
        height_feet = float(request.form.get('feet'))
        height_inches = float(request.form.get('inches'))
        
        # Convert height to total inches (1 foot = 12 inches)
        total_inches = (height_feet * 12) + height_inches
        
        # BMI formula for imperial units: (weight in pounds × 703) / (height in inches)²
        bmi = round((weight_lbs * 703) / (total_inches ** 2), 2)
    return render_template('index.html', bmi=bmi)


if __name__ == '__main__':
    app.run(debug=True)