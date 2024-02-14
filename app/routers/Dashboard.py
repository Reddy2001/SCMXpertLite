from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Importing get_current_user_from_cookie method to take the username,email and expired time
from routers.jwt import get_current_user_from_cookie

#  Importing Authenticate_User() function to check the user is Authenticated user or not
from routers.authenticate_user import authenticate_user

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


#  Dashboard router to display Dashboard page 
@router.get("/dashboard", response_class=HTMLResponse, dependencies=[Depends(authenticate_user)])
async def get_dashboard(request: Request, current_user: dict = Depends(get_current_user_from_cookie)):
    
    try:
        if current_user:
            return template.TemplateResponse("Dashboard.html", {"request": request, "name":current_user["username"],"role":current_user["role"]})
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error") 

