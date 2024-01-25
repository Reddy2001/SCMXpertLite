from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi import Request, Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.config import *

# Importing get_current_user_from_SessionStorage method to take the username,email and expired time
from routers.jwt import get_current_user_from_SessionStorage


# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")



# DeviceData router to display Device Data page 
@router.get("/deviceData")
def get_deviceData(request: Request):

    try:
        return template.TemplateResponse("DeviceData.html", {"request": request})
        
    except Exception as e:
         return JSONResponse(content={"Error":"Internal Server Error"}, status_code=500) 



# DeviceData Post route to take device id and displays the details 
@router.post("/deviceData")
def post_deviceData(request:Request,
                    current_user:dict = Depends(get_current_user_from_SessionStorage),
                    DeviceId:str=Form(...)):
    # print(DeviceId)
    try:
        if current_user["role"]=="Admin":
            data=list(Device_Data.find({"Device_Id":DeviceId},{"_id":0}))
            # print(data)
            return JSONResponse(content=(data),status_code=200)
        
    except Exception as e:
         return JSONResponse(content={"Error":"Internal Server Error"}, status_code=500) 
    