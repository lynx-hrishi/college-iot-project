import serial, json

def makeConnectionToComPort(port_no: str= "COM5") -> serial.Serial:
    serialInstance = serial.Serial()
    serial_port = port_no
    serialInstance.baudrate = 9600
    serialInstance.port = serial_port
    serialInstance.open()
    return serialInstance

def getSensorsDataService(serialInstance: serial.Serial):
    try:
        final_msg = serialInstance.readline().decode('utf8').strip()
        with open("sensors_data.json", 'w') as f:
            f.write(final_msg)
        return final_msg
    except Exception as e:
        return e

def returnSensorDataService():
    with open("sensors_data.json", 'r') as f:
        data = json.load(f)
        return data
