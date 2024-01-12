from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends,Form
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
        


# Change_User_Role router to display Change_User_Role page 
@router.get("/changeUserRole", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
def get_ChangeUserROle(request: Request):
    try:
        return template.TemplateResponse("Change_User_Role.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 


# Change_User_Role router to display Change_User_Role page 
@router.post("/changeUserRole", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
def post_ChangeUserROle(request: Request,
                        Email:str = Form(...),
                        current_user: dict = Depends(get_current_user_from_cookie)):
    try:
        # Fletching user details from DB based on email
        user=Users.find_one({"Email":Email})
        print("user -- >",user)
        # Checking the user is Exists based on the given Email
        if user is None:
            return template.TemplateResponse("Change_User_Role.html", {"request": request,"message":"Email Doesn't Exist.."})
        
        # If user exists admin will change the role of user
        else:

            #Updating the role on the database
            result= Users.update_one({"Email": user["Email"]} , {"$set": {"Role": "Admin"}})
            msg= "Successfully Changed role of User"
            return template.TemplateResponse("Change_User_Role.html",{"request":request,"message":msg})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 

