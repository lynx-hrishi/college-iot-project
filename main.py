from fastapi import FastAPI, Request
from getSensorDataService import makeConnectionToComPort, getSensorsDataService, returnSensorDataService
from fastapi.templating import Jinja2Templates

app = FastAPI()
# app.mount("/static")
templates = Jinja2Templates(directory="templates")

serialInstance = makeConnectionToComPort()

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", { "request": request })

@app.get("/get-data")
async def get_sensor_data():
    d=getSensorsDataService(serialInstance)
    data = returnSensorDataService()
    return { "data": data }