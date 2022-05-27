from random import randint
import wmi


#POO en Python
#Definicion de la clase
class Sensor:
    def __init__(self):
        self._wmi = wmi.WMI(namespace="root\OpenHardwareMonitor")
        
        
    def get_temp(self):
        return self._sensor['coretemp']
    
    def get_temp_for_windows(self):
        return self._wmi.SensorType['Temperature']
    
    #Simular la toma de algun valor
    def get_random_number(self):
        return randint(0,100)