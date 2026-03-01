from fastapi import FastAPI
from getSensorDataService import makeConnectionToComPort, getSensorsDataService, returnSensorDataService

app = FastAPI()

serialInstance = makeConnectionToComPort()

@app.get("/")
async def home():
    return { "msg": "Server is running" }

@app.get("/get-data")
async def get_sensor_data():
    d=getSensorsDataService(serialInstance)
    data = returnSensorDataService()
    return { "data": data }