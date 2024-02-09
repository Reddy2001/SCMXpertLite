from fastapi import APIRouter,Request,Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Importing get_current_user_from_cookie method to take the username,email and expired time
from routers.jwt import get_current_user_from_cookie

#  Importing Authenticate_User() function to check the user is Authenticated user or not
from routers.authenticate_user import Authenticate_User


# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# contactSuperAdmin router to display Contact_Super_Admin page 
@router.get("/contactSuperAdmin", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
async def get_superAdmin(request: Request, current_user: dict = Depends(get_current_user_from_cookie)):

    return template.TemplateResponse("Contact_Super_Admin.html", {"request": request,"name":current_user['username']})


