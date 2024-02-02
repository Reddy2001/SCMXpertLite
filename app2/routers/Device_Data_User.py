from fastapi import APIRouter, HTTPException
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")



# DeviceDataUser router to display Device Data User page 
@router.get("/deviceDataUser")
def get_deviceDataUser(request: Request):
    try:
        return template.TemplateResponse("Device_Data_User.html", {"request": request})
        
    except Exception:
        raise HTTPException(status_code=500, detail=f"Internal Server Error") 

