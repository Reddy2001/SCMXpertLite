from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from config.config import *

# Importing get_current_user_from_cookie method to take the username,email and expired time
from routers.jwt import get_current_user_from_cookie



# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# Authenticate_User function to check if the user is authenticated or not
async def Authenticate_User(current_user: dict = Depends(get_current_user_from_cookie)):
    if current_user is None or "username" not in current_user or "email" not in current_user or "role" not in current_user:
       # Redirect unauthenticated user to the sign-in page
        url = "/"
        raise HTTPException(status_code=307, detail="Not authenticated", headers={"Location": url})
    return current_user
        


# MyAccount router to display MyAccount page 
@router.get("/myAccount", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
def get_myAccount(request: Request, current_user: dict = Depends(get_current_user_from_cookie)):
    try:
        if current_user:
            print("Current User Is ",current_user)
            return template.TemplateResponse("MyAccount.html", {"request": request,"name":current_user["username"],"email":current_user["email"],"role":current_user["role"]})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 


