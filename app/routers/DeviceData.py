from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.config import *

# Importing get_current_user_from_cookie method to take the username,email and expired time
from routers.jwt import get_current_user_from_cookie

#  Importing Authenticate_User() function to check the user is Authenticated user or not
from routers.Authenticate_User import Authenticate_User

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")

    

# DeviceData router to display Device Data page 
@router.get("/deviceData", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
def get_deviceData(request: Request, current_user: dict = Depends(get_current_user_from_cookie)):

    try:

        # Validating role, If role is "Admin"  --> Then only they can watch Device Data page
        if current_user["role"]== "Admin": 
            return template.TemplateResponse("DeviceData.html", {"request": request})
        
        # If the role is "User" --> They can't access Device data page[Get error message]
        else:
           return template.TemplateResponse("Device_Data_User.html",{"request":request})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 



# DeviceData Post route to take device id and displays the details 
@router.post("/deviceData",response_class=HTMLResponse,dependencies=[Depends(Authenticate_User)])
def post_deviceData(request:Request,
                    current_user:dict = Depends(get_current_user_from_cookie),
                    DeviceId:str=Form(...)):
    try:

        # Validating role, If role is "Admin"  --> Then only they can watch Device Data page
        if current_user["role"]== "Admin": 
            data=Device_Data.find({"Device_Id":DeviceId})
            # print(data)
            return template.TemplateResponse("DeviceData.html", {"request": request,"DeviceData":data,"id":DeviceId})
        
        # If the role is "User" --> They can't access Device data page[Get error message]
        else:
           return template.TemplateResponse("Device_Data_User.html",{"request":request})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 