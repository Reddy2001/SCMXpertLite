from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from fastapi import Request, Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

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

class ShipmentDetails(BaseModel):
    Shipment_Number : str
    Container_Number: str
    Route_Details : str
    Goods_Type : str
    Device : str
    Expected_Delivery : str
    PO_Number : str
    Delivery_Number : str
    NDC_Number : str
    Batch_ID : str
    Serial_Number : str
    Shipment_Description : str


# NewShipment get router to display NewShipment page 
@router.get("/newShipment")
def get_newShipment(request: Request):
    return template.TemplateResponse("NewShipment.html", {"request": request})



# NewShipment post router to validate inputs of User
@router.post("/newShipment")
def post_newShipment(request: Request,
                    data:ShipmentDetails | None = None,
                    current_user: str = Depends(get_current_user_from_SessionStorage)):
    # print(data, current_user)
    User_email=current_user["email"]

    # Checking Shipment Number size[size must be 7]
    if (len(data.Shipment_Number) != 7):
        return JSONResponse(content={"Error":"Shipment Number must contain 7 digits...."},status_code=400)
    
    # Checking Uniqueness of Shipment Number
    elif Shipment.find_one({"ShipmentNumber":data.Shipment_Number}):
        return JSONResponse(content={"Error":"Shipment Number already exists.... "},status_code=400)
    
    elif data.Container_Number=='' or data.Route_Details=='' or data.Goods_Type=='' or data.Device=='' or data.Expected_Delivery=='' or data.PO_Number=='' or data.Delivery_Number=='' or data.NDC_Number=='' or data.Batch_ID=='' or data.Serial_Number=='' or data.Shipment_Description=='':
        return JSONResponse(content={"Error":"Enter All Required Fields(*)"},status_code=400)
    

    # Pushing newShipment to the newShipment dictionary
    newShipment={
        "Email":User_email,
        "ShipmentNumber":data.Shipment_Number,
        "ContainerNumber":data.Container_Number,
        "RouteDetails":data.Route_Details,
        "GoodsType":data.Goods_Type,
        "DeviceName":data.Device,
        "DeliveryDate":data.Expected_Delivery,
        "PO_Number":data.PO_Number,
        "DeliveryNumber":data.Delivery_Number,
        "NDC_Number":data.NDC_Number,
        "BatchId":data.Batch_ID,
        "SerialNumber":data.Serial_Number,
        "ShipmentDescription":data.Shipment_Description
    }

    # Pushing newShipment to the newShipmentbase[Shipment Collection]
    # print(newShipmentnewShipment)
    Shipment.insert_one(newShipment)

    return JSONResponse(content={"message":"New Shipment registered successfully...."},status_code=200)
