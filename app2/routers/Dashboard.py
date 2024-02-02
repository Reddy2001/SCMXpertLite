from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Importing get_current_user_from_SessionStorage method to take the username,email and expired time


# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")
 


#  Dashboard router to display Dashboard page 
@router.get("/dashboard")
async def get_dashboard(request: Request):
    return template.TemplateResponse("dashboard.html", {"request": request})

