from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Importing get_current_user_from_SessionStorage method to take the username,email and expired time
from routers.jwt import get_current_user_from_SessionStorage

# importing all variables in config file
from  config.config import *

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")
     


# MyShipment router to display MyShipment page
@router.get("/myShipment")
def get_MyShipment(request: Request):

    try:
        return template.TemplateResponse("MyShipment.html", {"request": request})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 
    

# MyShipment router to display MyShipment page along with Shipment Data
@router.get("/myShipmentData")
def get_MyShipment(request: Request,current_user:dict = Depends(get_current_user_from_SessionStorage)):

    # print(current_user)
    try:

        # Validating role, If role is "Admin"  --> Then Admin can watch all Shipment Details
        if current_user["role"]== "Admin": 
            ShipmentData=list(Shipment.find({},{"_id":0}))
            return JSONResponse(content=(ShipmentData),status_code=200)
        
        # If the role is "User" --> Then the User can watch their Shipment Details
        else:
            ShipmentData=list(Shipment.find({"Email":current_user["email"]},{"_id":0}))
            return JSONResponse(content=(ShipmentData),status_code=200)
        
    except Exception as e:
        return JSONResponse(content={"Error":"Internal Server Error"}, status_code=500)
    


