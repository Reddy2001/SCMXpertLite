from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Importing Device_Data from config file for Device_Data Collection
from config.config import Device_Data

# Importing get_current_user_from_cookie method to take the username,email and expired time
from routers.jwt import get_current_user_from_cookie

#  Importing authenticate_user() function to check the user is Authenticated user or not
from routers.authenticate_user import authenticate_user

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")

    

# DeviceData router to display Device Data page 
@router.get("/deviceData", response_class=HTMLResponse, dependencies=[Depends(authenticate_user)])
def get_device_data(request: Request, current_user: dict = Depends(get_current_user_from_cookie)):

    try:

        # Validating role, If role is "Admin"  --> Then only they can watch Device Data page
        if current_user["role"]== "Admin" or current_user["role"] == 'Super Admin': 
            return template.TemplateResponse("DeviceData.html", {"request": request})
        
        # If the role is "User" --> They can't access Device data page[Get error message]
        else:
           return template.TemplateResponse("Device_Data_User.html",{"request":request})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 



# DeviceData Post route to take device id and displays the details 
@router.post("/deviceData",response_class=HTMLResponse,dependencies=[Depends(authenticate_user)])
def post_device_data(request:Request,
                     device_id:str=Form(...),
                    current_user:dict = Depends(get_current_user_from_cookie)):
    try:

        # Validating role, If role is "Admin"  --> Then only they can watch Device Data page
        if current_user["role"]== "Admin" or current_user["role"] == 'Super Admin': 
            data=Device_Data.find({"Device_Id":device_id})
            # print(data)
            return template.TemplateResponse("DeviceData.html", {"request": request,"DeviceData":data,"id":device_id})
        
        # If the role is "User" --> They can't access Device data page[Get error message]
        else:
           return template.TemplateResponse("Device_Data_User.html",{"request":request})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 