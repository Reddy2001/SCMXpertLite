from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends,Form
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
        


# NewShipment get router to display NewShipment page 
@router.get("/newShipment", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
def get_newShipment(request: Request, current_user: dict = Depends(get_current_user_from_cookie)):
    return template.TemplateResponse("NewShipment.html", {"request": request,"name":current_user["username"]})



# NewShipment post router to take input from UserInterface
@router.post("/newShipment", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
def post_newShipment(request: Request, ShipmentNumber: str = Form(...),
                    ContainerNumber: str = Form(...), 
                    RouteDetails: str = Form(...), 
                    GoodsType: str = Form(...), 
                    DeviceName: str = Form(...), 
                    DeliveryDate: str = Form(...), 
                    PO_Number: str = Form(...), 
                    DeliveryNumber: str = Form(...), 
                    NDC_Number: str = Form(...), 
                    BatchId: str = Form(...), 
                    SerialNumber: str = Form(...), 
                    ShipmentDescription: str = Form(...),
                    current_user: dict = Depends(get_current_user_from_cookie)):
    
    User_email=current_user["email"]

    # Checking Shipment Number size[size must be 7]
    if (len(ShipmentNumber) != 7):
        return template.TemplateResponse("NewShipment.html",{"request":request,"error":"Shipment Number must contain 7 digits......"})
    
    # Checking Uniqueness of Shipment Number
    elif Shipment.find_one({"ShipmentNumber":ShipmentNumber}):
        return template.TemplateResponse("NewShipment.html",{"request":request,"error":"Shipment Number should be unique....."})
    

    # Pushing data to the newShipmentData dictionary
    newShipmentData={
        "Email":User_email,
        "ShipmentNumber":ShipmentNumber,
        "ContainerNumber":ContainerNumber,
        "RouteDetails":RouteDetails,
        "GoodsType":GoodsType,
        "DeviceName":DeviceName,
        "DeliveryDate":DeliveryDate,
        "PO_Number":PO_Number,
        "DeliveryNumber":DeliveryNumber,
        "NDC_Number":NDC_Number,
        "BatchId":BatchId,
        "SerialNumber":SerialNumber,
        "ShipmentDescription":ShipmentDescription
    }

    # Pushing data to the database[Shipment Collection]
    # print(newShipmentData)
    Shipment.insert_one(newShipmentData)
    msg="New Shipment registered successfully...."
    return template.TemplateResponse("NewShipment.html",{"request":request,"message":msg})

