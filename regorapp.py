import numpy as np 
import statsmodels.api as sm 
import statsmodels.tsa.api as smt 
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
results = pickle.load(open('regor_GP_20_v1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    init_features = [eval(x) for x in request.form.values()]
    final_features = [np.array(init_features)]
    prediction = results.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', 
                            prediction_text='The Total cases are approximately around {}'.format(output)
                            )

if __name__ == '__main__':
    app.run(debug=True)
