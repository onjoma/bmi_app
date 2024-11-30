"""
BMI Categories, Health Information, and Recommendations Data
"""

BMI_CATEGORIES = {
    'underweight': {
        'range': 'Below 18.5',
        'description': 'Being underweight can indicate nutritional deficiencies or other health issues.',
        'risks': [
            'Weakened immune system',
            'Nutritional deficiencies',
            'Osteoporosis risk',
            'Fertility issues',
            'Anemia'
        ],
        'recommendations': {
            'nutrition': [
                'Increase caloric intake with nutrient-dense foods',
                'Add healthy fats like avocados, nuts, and olive oil',
                'Eat protein-rich foods at every meal',
                'Consider eating smaller meals more frequently',
                'Include whole grain carbohydrates'
            ],
            'exercise': [
                'Focus on strength training to build muscle',
                'Avoid excessive cardio',
                'Include resistance exercises',
                'Ensure proper rest between workouts',
                'Consider working with a fitness professional'
            ],
            'general': [
                'Consult with a healthcare provider',
                'Keep a food diary',
                'Monitor your weight weekly',
                'Get adequate sleep',
                'Consider nutritional supplements (after consulting a doctor)'
            ]
        }
    },
    'normal': {
        'range': '18.5 - 24.9',
        'description': 'A healthy BMI range indicates a good balance between height and weight.',
        'risks': [
            'Generally lower health risks',
            'Maintain this range for optimal health'
        ],
        'recommendations': {
            'nutrition': [
                'Maintain a balanced diet',
                'Eat plenty of fruits and vegetables',
                'Choose whole grains',
                'Include lean proteins',
                'Stay hydrated'
            ],
            'exercise': [
                'Regular physical activity (150 minutes/week)',
                'Mix of cardio and strength training',
                'Stay active throughout the day',
                'Include flexibility exercises',
                'Try different activities you enjoy'
            ],
            'general': [
                'Regular health check-ups',
                'Maintain healthy habits',
                'Get adequate sleep',
                'Manage stress levels',
                'Stay consistent with healthy lifestyle choices'
            ]
        }
    },
    'overweight': {
        'range': '25.0 - 29.9',
        'description': 'Being overweight may increase the risk of certain health conditions.',
        'risks': [
            'Increased risk of heart disease',
            'Higher blood pressure',
            'Type 2 diabetes risk',
            'Joint problems',
            'Sleep issues'
        ],
        'recommendations': {
            'nutrition': [
                'Control portion sizes',
                'Reduce processed food intake',
                'Increase fiber-rich foods',
                'Choose lean proteins',
                'Limit added sugars'
            ],
            'exercise': [
                'Start with walking programs',
                'Gradually increase activity',
                'Include both cardio and strength training',
                'Find activities you enjoy',
                'Consider working with a fitness professional'
            ],
            'general': [
                'Set realistic weight loss goals',
                'Track your food intake',
                'Regular health check-ups',
                'Get support from family/friends',
                'Focus on sustainable changes'
            ]
        }
    },
    'obese': {
        'range': '30.0 or greater',
        'description': 'Obesity is associated with various health risks and requires medical attention.',
        'risks': [
            'High risk of heart disease',
            'Type 2 diabetes',
            'High blood pressure',
            'Certain cancers',
            'Breathing problems'
        ],
        'recommendations': {
            'nutrition': [
                'Consult with a registered dietitian',
                'Create a structured meal plan',
                'Control portion sizes',
                'Avoid processed foods',
                'Keep a food diary'
            ],
            'exercise': [
                'Start slowly with approved exercises',
                'Focus on low-impact activities',
                'Regular walking programs',
                'Swimming or water exercises',
                'Work with healthcare providers'
            ],
            'general': [
                'Seek medical supervision',
                'Set realistic goals',
                'Consider behavioral therapy',
                'Join support groups',
                'Regular health monitoring'
            ]
        }
    }
}

def get_bmi_category(bmi):
    """
    Determine BMI category based on BMI value
    """
    if bmi < 18.5:
        return 'underweight'
    elif 18.5 <= bmi <= 24.9:
        return 'normal'
    elif 25.0 <= bmi <= 29.9:
        return 'overweight'
    else:
        return 'obese'

def get_ideal_weight_range(height_feet, height_inches):
    """
    Calculate ideal weight range based on height for BMI between 18.5 and 24.9
    Height should be in feet and inches
    Returns weight range in pounds
    """
    # Convert height to inches
    total_inches = (height_feet * 12) + height_inches
    
    # Calculate weight range using BMI formula: weight(lb) / [height(inches)]^2 x 703
    min_weight = round((18.5 * (total_inches ** 2)) / 703, 1)
    max_weight = round((24.9 * (total_inches ** 2)) / 703, 1)
    
    return min_weight, max_weight

def get_bmi_info(bmi, height_feet, height_inches):
    """
    Get comprehensive BMI information including category, risks, and recommendations
    """
    category = get_bmi_category(bmi)
    info = BMI_CATEGORIES[category].copy()
    
    # Add ideal weight range
    min_weight, max_weight = get_ideal_weight_range(height_feet, height_inches)
    info['ideal_weight_range'] = f"{min_weight} - {max_weight} pounds"
    
    return info
