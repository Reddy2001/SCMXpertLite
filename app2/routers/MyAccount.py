from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# importing all variables in config fil
from config.config import *

# Importing get_current_user_from_SessionStorage method to take the username,email and expired time
from routers.jwt import get_current_user_from_SessionStorage



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


