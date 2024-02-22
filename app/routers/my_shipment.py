from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Importing get_current_user_from_cookie method to take the username,email and expired time
from routers.jwt import get_current_user_from_cookie


#  Importing Authenticate_User() function to check the user is Authenticated user or not
from routers.authenticate_user import authenticate_user


# importing Shipment variables in config file for Shipment Collection
from  config.config import Shipment

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# MyShipment router to display MyShipment page along with My Shipment Data
@router.get("/myShipment", response_class=HTMLResponse, dependencies=[Depends(authenticate_user)])
def get_my_shipment(request: Request, current_user: dict = Depends(get_current_user_from_cookie)):


    try:

        # Validating role, If role is "Admin" or "Super Admin" --> Then Admin and Super Admin can watch all Shipment Details
        if current_user["role"]== "Admin" or current_user['role'] == 'Super Admin': 
            shipment_data=list(Shipment.find({}))
            return template.TemplateResponse("MyShipment.html",{"request":request,"ShipmentData":shipment_data,"name":current_user["username"],"role":current_user['role']})
        
        # If the role is "User" --> Then the User can watch their Shipment Details
        else:
            shipment_data=list(Shipment.find({"Email":current_user["email"]}))
            return template.TemplateResponse("MyShipment.html", {"request": request,"ShipmentData":shipment_data, "name":current_user["username"],"role":current_user['role']})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 
  