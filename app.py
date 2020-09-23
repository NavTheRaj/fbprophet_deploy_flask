import flask
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import pickle
import json
#app = Flask(__name__)
app = flask.Flask(__name__)

filename = "forecast_model.pckl"

filemode = "rb"

m2 = pickle.load(open(filename,filemode))

CORS(app)
@app.route("/predict", methods=['POST','GET'])
def predict():
#    json_data = request.data

#    print(json_data)

#     horizon = int(json_data['horizon'])

     horizon = 10

     future2 = m2.make_future_dataframe(periods=horizon)
     forecast2 = m2.predict(future2)

     data = forecast2[['ds', 'yhat',]][-horizon:]

     ret = data.to_json(orient='records',date_format="iso")

     return ret# running REST interface, port=3000 for direct test


if __name__ == "__main__":
    app.run()
