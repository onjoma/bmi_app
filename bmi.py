from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages

@app.route('/', methods=['POST', 'GET'])
def bmi_calculate():
    bmi = ""
    # Initialize form data dictionary
    form_data = {
        'weight': '',
        'feet': '',
        'inches': ''
    }
    
    if request.method == 'POST' and 'weight' in request.form and 'feet' in request.form and 'inches' in request.form:
        # Store the form data
        form_data = {
            'weight': request.form.get('weight'),
            'feet': request.form.get('feet'),
            'inches': request.form.get('inches')
        }
        
        try:
            weight_lbs = float(form_data['weight'])
            height_feet = float(form_data['feet'])
            height_inches = float(form_data['inches'])
            
            # Input validation
            if weight_lbs <= 0:
                flash('Please enter a valid weight greater than 0 pounds', 'error')
                return render_template('index.html', form_data=form_data)
            
            if height_feet < 0 or height_inches < 0 or height_inches >= 12:
                flash('Please enter a valid height. Inches should be between 0 and 11', 'error')
                return render_template('index.html', form_data=form_data)
            
            if height_feet == 0 and height_inches == 0:
                flash('Height cannot be zero', 'error')
                return render_template('index.html', form_data=form_data)
            
            # Convert height to total inches (1 foot = 12 inches)
            total_inches = (height_feet * 12) + height_inches
            
            # BMI formula for imperial units: (weight in pounds × 703) / (height in inches)²
            bmi = round((weight_lbs * 703) / (total_inches ** 2), 2)
            
            # Validate BMI result
            if bmi > 100:
                flash('The calculated BMI seems unusually high. Please check your inputs', 'warning')
            
        except ValueError:
            flash('Please enter valid numbers for weight and height', 'error')
            return render_template('index.html', form_data=form_data)
        except ZeroDivisionError:
            flash('Height cannot be zero', 'error')
            return render_template('index.html', form_data=form_data)
        
    return render_template('index.html', bmi=bmi, form_data=form_data)


if __name__ == '__main__':
    app.run(debug=True)