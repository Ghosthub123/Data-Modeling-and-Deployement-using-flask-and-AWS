import flask
from flask import request
app = flask.Flask(__name__)

from flask_cors import CORS 
CORS(app)

@app.route('/')

def default():
    return '<h1> API SERVER IS RUNNING </h1>'

@app.route('/predict')
def home():
    from sklearn.externals import joblib
    model_1 = joblib.load('marrige_age_predict_model.ml')
    my_value = model_1.predict([[request.args['gender'],
                               2,
                               38,
                               8,
                               5,
                               160.10]])
    return f'<h1>predicting..   Prediction is {str(my_value)}</h1>'



app.run()