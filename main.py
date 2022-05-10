"""
@author M. Gamboa
@since 2022-05-10
@Flask Exercise
"""
#Module Inclusion
from flask import Flask

app = Flask('__main__')
#Create an instance from Flask with the name __name__

@app.route('/test', methods=['GET'])#From App you would pull thse items
def go_home():
    return 'The Fitness Gram Pacer Test is a multistage...!'

if __name__ == '__main__':#Runs the application since the project name is the same
    app.run(debug=True, port=5000, host='0.0.0.0')
    