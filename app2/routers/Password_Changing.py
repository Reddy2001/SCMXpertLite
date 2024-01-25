from fastapi import APIRouter,HTTPException
from fastapi import Request,Form,Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

# importing "re" module in Python provides regular expression matching operations[It is used for password strength checking ]
import re

# importing all variables in config file
from config.config import *

# importing CryptContext to hash the password
from passlib.context import CryptContext


# Importing get_current_user_from_SessionStorage method to take the username,email and expired time
from routers.jwt import get_current_user_from_SessionStorage


# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# Instance for CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")



# Password Changing router to display Password_Changing page 
@router.get("/passwordChanging")
def get_passwordChanging(request: Request):
    return template.TemplateResponse("Password_Changing.html", {"request": request})



# Password Changing router to display Password_Changing page 
@router.post("/passwordChanging")
def post_passwordChanging(request: Request, Old_Password:str = Form(...), 
                          New_Password:str = Form(...), 
                          Re_type_Password:str = Form(...),
                          current_user: dict = Depends(get_current_user_from_SessionStorage)):
    try:

        # fletching user details from database based on email
        user = Users.find_one({"Email":current_user["email"]})

        # Checking Old Password with the Password present on the database
        if not (pwd_context.verify(Old_Password, user["Password"])):
            return JSONResponse(content={"Error":"Old Password is not matched with Original Password"},status_code=400)
        
        # Checking New Password is Different from Old password or not
        elif (Old_Password == New_Password):
            return JSONResponse(content={"Error":"New Password Should not be the Old Password"},status_code=400)

        # Validating Password and Re_Type Password is same or not
        elif(New_Password !=Re_type_Password):
            return JSONResponse(content={"Error":"New Password and Re-type Password should be same"},status_code=400)
        
        # Checking password have capital letter, small letter and special character
        elif not (re.search("[A-Z]",New_Password) and re.search("[a-z]",New_Password) and re.search(r'[!@#$%^&*(),.?":{}|<>]',New_Password)):
            return JSONResponse(content={"Error":"Password must contain Capital letters, Small letters and Special character...."},status_code=400)
        
        else:
            # Hashing the password
            hash_password = pwd_context.hash(New_Password)
            # print("current_user", current_user)

            #Updating the new password on the database
            result= Users.update_one({"Email": current_user["email"]} , {"$set": {"Password": hash_password}})
            
            return JSONResponse(content={"message":"Password Changed Successfully"},status_code=200)


    except Exception:
        return JSONResponse(content={"Error":"Internal Server Error"},status_code=500)

            
