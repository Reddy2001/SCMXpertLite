from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends,Form
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

# Assigning NewShipment.html to newShipment Variable
newShipments="NewShipment.html"

# NewShipment get router to display NewShipment page 
@router.get("/newShipment", response_class=HTMLResponse, dependencies=[Depends(authenticate_user)])
def get_new_shipment(request: Request, current_user: dict = Depends(get_current_user_from_cookie)):
    return template.TemplateResponse(newShipments, {"request": request,"name":current_user["username"]})



# NewShipment post router to take input from UserInterface
@router.post("/newShipment", response_class=HTMLResponse, dependencies=[Depends(authenticate_user)])
def post_new_shipment(request: Request, shipment_number: int = Form(...),
                    container_number: int = Form(...), 
                    route_details: str = Form(...), 
                    goods_type: str = Form(...), 
                    device_name: str = Form(...), 
                    delivery_date: str = Form(...), 
                    po_number: int = Form(...), 
                    delivery_number: int = Form(...), 
                    ndc_number: int = Form(...), 
                    batch_id: int = Form(...), 
                    serial_number: int = Form(...), 
                    shipment_description: str = Form(...),
                    current_user: dict = Depends(get_current_user_from_cookie)):

    try:

        user_email=current_user["email"]

        # Checking Shipment Number size[size must be 7]
        if (len(str(shipment_number)) != 7):
            return template.TemplateResponse(newShipments,{"request":request,"name":current_user['username'],"error":"Shipment Number must contain 7 digits......"})
        
        # Checking Uniqueness of Shipment Number
        elif Shipment.find_one({"ShipmentNumber":shipment_number}):
            return template.TemplateResponse(newShipments,{"request":request,"name":current_user['username'],"error":"Shipment Number should be unique....."})
        

        # Pushing data to the new_shipment_data dictionary
        new_shipment_data={
            "Email":user_email,
            "ShipmentNumber":shipment_number,
            "ContainerNumber":container_number,
            "RouteDetails":route_details,
            "GoodsType":goods_type,
            "DeviceName":device_name,
            "DeliveryDate":delivery_date,
            "PO_Number":po_number,
            "DeliveryNumber":delivery_number,
            "NDC_Number":ndc_number,
            "BatchId":batch_id,
            "SerialNumber":serial_number,
            "ShipmentDescription": shipment_description
        }
                

        # Pushing data to the database[Shipment Collection]
        Shipment.insert_one(new_shipment_data)
        msg="New Shipment registered successfully...."
        return template.TemplateResponse(newShipments,{"request":request,"name":current_user['username'],"message":msg})
    except Exception:
         raise HTTPException(status_code=400, detail="Missing Parameters")

