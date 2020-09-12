import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('modelSalaryPredictor.nair', 'rb'))
#ohe = pickle.load(open('StateEncoder.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    yearsExp = float(request.form['yearsExp'])
    prediction = model.predict(yearsExp)

    return render_template('index.html', prediction_text='Expected Profit from the Startup is  $ {}'.format(prediction[0]))


if __name__ == "__main__":
    app.run(debug=True)
