from distutils.command.config import config
from flask import Flask ,request,jsonify
import config

from project_app.utils import IrisSpecies

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def test():
    return 'BASE API IS RUNNING'

@app.route('/predict_class',methods=['POST','GET'])
def predict_class():
    data = request.form
    SepalLengthCm= eval(data['SepalLengthCm'])
    SepalWidthCm =eval(data['SepalWidthCm'])
    PetalLengthCm =eval(data['PetalLengthCm'])
    PetalWidthCm =eval(data['PetalWidthCm'])

    obj = IrisSpecies(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    result = obj.get_result()
    return jsonify({'predicted class is ' : f"{result}"})


if __name__== '__main__':
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)