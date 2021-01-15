from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def bmi_calculate():

    bmi = ""
    if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
        w = float(request.form.get('weight'))
        h = float(request.form.get('height'))
        bmi = round(w / ((h/100)**2),2)
    return render_template('index.html', bmi=bmi)


if __name__ == '__main__':
    app.run(debug=True)