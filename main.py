"""
@author M. Gamboa
@since 2022-05-10
@Flask Exercise
"""
#Module Inclusion
from flask import Flask, request

app = Flask('__main__')
#Create an instance from Flask with the name __name__

device = {
    "code":"112233",
    "descrip":"Temp, Sensor",
    "value":67   
}

@app.route('/devices', methods=['GET'])#From App you would pull thse items
def go_home():
    return device

@app.route('/users', methods=['POST'])
def save_user():
    user = request.json
    print(user)
    return user

@app.route('/', methods=['POST'])
def save_device():
    device = request.json
    return device

if __name__ == '__main__':#Runs the application since the project name is the same
    app.run(debug=True, port=5000, host='0.0.0.0')
    