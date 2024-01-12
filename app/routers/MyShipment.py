from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Importing get_current_user_from_cookie method to take the username,email and expired time
from routers.jwt import get_current_user_from_cookie

# importing all variables in config file
from  config.config import *

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")

# New dependency function to check if the user is authenticated
async def Authenticate_User(current_user: dict = Depends(get_current_user_from_cookie)):
    if current_user is None or "username" not in current_user or "email" not in current_user or "role" not in current_user:
       # Redirect unauthenticated user to the sign-in page
        url = "/"
        raise HTTPException(status_code=307, detail="Not authenticated", headers={"Location": url})
    return current_user
        


# MyShipment router to display MyShipment page along with My Shipment Data
@router.get("/myShipment", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
def get_MyShipment(request: Request, current_user: dict = Depends(get_current_user_from_cookie)):


    try:

        # Validating role, If role is "Admin"  --> Then Admin can watch all Shipment Details
        if current_user["role"]== "Admin": 
            ShipmentData=list(Shipment.find({}))
            return template.TemplateResponse("MyShipment.html",{"request":request,"ShipmentData":ShipmentData,"name":current_user["username"]})
        
        # If the role is "User" --> Then the User can watch their Shipment Details
        else:
            ShipmentData=list(Shipment.find({"Email":current_user["email"]}))
            return template.TemplateResponse("MyShipment.html", {"request": request,"ShipmentData":ShipmentData, "name":current_user["username"]})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 
    


