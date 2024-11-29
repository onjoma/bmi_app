from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages

@app.route('/', methods=['POST', 'GET'])
def bmi_calculate():
    bmi = ""
    if request.method == 'POST' and 'weight' in request.form and 'feet' in request.form and 'inches' in request.form:
        try:
            weight_lbs = float(request.form.get('weight'))
            height_feet = float(request.form.get('feet'))
            height_inches = float(request.form.get('inches'))
            
            # Input validation
            if weight_lbs <= 0:
                flash('Please enter a valid weight greater than 0 pounds', 'error')
                return render_template('index.html')
            
            if height_feet < 0 or height_inches < 0 or height_inches >= 12:
                flash('Please enter a valid height. Inches should be between 0 and 11', 'error')
                return render_template('index.html')
            
            if height_feet == 0 and height_inches == 0:
                flash('Height cannot be zero', 'error')
                return render_template('index.html')
            
            # Convert height to total inches (1 foot = 12 inches)
            total_inches = (height_feet * 12) + height_inches
            
            # BMI formula for imperial units: (weight in pounds × 703) / (height in inches)²
            bmi = round((weight_lbs * 703) / (total_inches ** 2), 2)
            
            # Validate BMI result
            if bmi > 100:
                flash('The calculated BMI seems unusually high. Please check your inputs', 'warning')
            
        except ValueError:
            flash('Please enter valid numbers for weight and height', 'error')
            return render_template('index.html')
        except ZeroDivisionError:
            flash('Height cannot be zero', 'error')
            return render_template('index.html')
        
    return render_template('index.html', bmi=bmi)


if __name__ == '__main__':
    app.run(debug=True)