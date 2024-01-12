from fastapi import APIRouter,HTTPException
from fastapi import Request,Form,Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import re

# importing all variables in config file
from config.config import *

from passlib.context import CryptContext


# Importing get_current_user_from_cookie method to take the username,email and expired time
from routers.jwt import get_current_user_from_cookie


# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# Instance for CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


        
# Authenticate_User function to check if the user is authenticated or not
async def Authenticate_User(current_user: dict = Depends(get_current_user_from_cookie)):
    if current_user is None or "username" not in current_user:
       # Redirect unauthenticated user to the home page
        url = "/"
        raise HTTPException(status_code=307, detail="Not authenticated", headers={"Location": url})
    return current_user
        

# Password Changing router to display Password_Changing page 
@router.get("/passwordChanging", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
def get_passwordChanging(request: Request):
    return template.TemplateResponse("Password_Changing.html", {"request": request})



# Password Changing router to display Password_Changing page 
@router.post("/passwordChanging", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
def post_passwordChanging(request: Request, Old_Password:str = Form(...), 
                          New_Password:str = Form(...), 
                          Re_type_Password:str = Form(...),
                          current_user: dict = Depends(get_current_user_from_cookie)):
    try:
        user = Users.find_one({"Email":current_user["email"]})

        # Checking Old Password with the Password present on the database
        if not (pwd_context.verify(Old_Password,user["Password"])):
            return template.TemplateResponse("Password_Changing.html",{"request":request,"error":"Old Password is not matched with Original Password"})
        
        # Checking New Password is Different from Old password or not
        elif (Old_Password == New_Password):
            return template.TemplateResponse("Password_Changing.html",{"request":request,"error":"New Password Should not be the Old Password"})

        # Validating Password and Re_Type Password is same or not
        elif(New_Password !=Re_type_Password):
            return template.TemplateResponse("Password_Changing.html",{"request":request,"error":"New Password and Re-type Password should be same"})
        
        # Checking password have capital letter, small letter and special character
        elif not (re.search("[A-Z]",New_Password) and re.search("[a-z]",New_Password) and re.search(r'[!@#$%^&*(),.?":{}|<>]',New_Password)):
            return template.TemplateResponse("Password_Changing.html", {"request": request, "error":"Password must contain Capital letters, Small letters and Special character......."})
        
        else:
            # Hashing the password
            hash_password = pwd_context.hash(New_Password)
            print("current_user", current_user)

            #Updating the new password on the database
            result= Users.update_one({"Email": current_user["email"]} , {"$set": {"Password": hash_password}})
            
            return template.TemplateResponse("Dashboard.html",{"request":request,"success":"Password Changed Successfully"})


    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

            
