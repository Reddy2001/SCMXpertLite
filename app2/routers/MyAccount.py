from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# importing all variables in config file
from config.config import *

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# MyAccount router to display MyAccount page 
@router.get("/myAccount")
def get_myAccount(request: Request):  
    
    return template.TemplateResponse("MyAccount.html",{"request":request})


