from flask import Flask,request # get() is used by flask
from model import predict_model

app=Flask(__name__)  # we have to use 2 '_' while defining the name

@app.route('/')  #'/' = default request
def basic():
    return 'api server started'

@app.route('/soil',methods=['get']) #'/soil' = request # get() is used by and we ahve to use plural form of method name
def soil():
    value=request.args.get('soil')
    print(value)
    value=int(value)
    response=predict_model(value)
    return {'msg':(response)}
if __name__=='__main__':
    app.run('0.0.0.0',port = 5001)