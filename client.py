from http import client
from device import Sensor
import json
import time

#Creacion de un objeto de la clase HTTPCOnnection
_conn = client.HTTPConnection(host = 'localhost', port = 5000)

#Creacion de un objeto de la clase Sensor
s = Sensor()
header = ("Content.type" , "application\json")

while True:
    data = {
        'id': 1,
        'name': 'Temp Sensor',
        'value': s.get_random_number()
    }
    json_data = json.dumps(data)
    
    _conn.request('POST', '/devices', data, headers=header)
    _conn.close()


    print (s.get_random_number())
    #print (s.get_temp_for_windows())
    time.sleep(1)