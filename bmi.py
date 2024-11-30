from flask import Flask, render_template, request, flash
from utils.bmi_data import get_bmi_info

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages

@app.route('/', methods=['GET', 'POST'])
def calculate_bmi():
    bmi = None
    bmi_info = None
    feet = request.form.get('feet', '')
    inches = request.form.get('inches', '')
    weight = request.form.get('weight', '')
    
    if request.method == 'POST':
        try:
            # Convert inputs to appropriate types
            feet = int(feet) if feet else None
            inches = int(inches) if inches else 0
            weight = float(weight) if weight else None
            
            # Validate inputs with specific range messages
            if feet is None or weight is None:
                flash('Please enter both height and weight values.', 'error')
            elif weight <= 0 or weight > 1000:
                flash('Weight must be between 1 and 1000 pounds.', 'error')
            elif feet < 1 or feet > 8:
                flash('Height (feet) must be between 1 and 8 feet.', 'error')
            elif inches < 0 or inches >= 12:
                flash('Height (inches) must be between 0 and 11 inches.', 'error')
            else:
                # Calculate BMI
                height_inches = (feet * 12) + inches
                bmi = round((weight / (height_inches ** 2)) * 703, 1)
                
                # Get BMI information and recommendations
                bmi_info = get_bmi_info(bmi, feet, inches)
                
        except ValueError:
            flash('Please enter valid numbers for height and weight.', 'error')
    
    return render_template('index.html', 
                         bmi=bmi, 
                         feet=feet, 
                         inches=inches, 
                         weight=weight,
                         bmi_info=bmi_info)

if __name__ == '__main__':
    app.run(debug=True)