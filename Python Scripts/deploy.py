from flask import Flask,request,jsonify
import numpy as np
import pickle
model = pickle.load(open('./LR_model.pkl','rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"
@app.route('/predict',methods=['POST'])
def predict():
    BodyTemp = float(request.form.get('BodyTemp'))
    HeartRate = float(request.form.get('HeartRate'))
    Oxi = float(request.form.get('Oxi'))
    # HealthStatusCode = request.form.get('HealthStatusCode')
    input_query = np.array([[BodyTemp,HeartRate,Oxi]])
    result = model.predict(input_query)[0]
    print("BodyTemp:",BodyTemp)
    return jsonify({'HealthStatusCode':str(result)})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
    # input_query = np.array([[37.2,120,93]])
    # result = model.predict(input_query)[0]
    # print(result)