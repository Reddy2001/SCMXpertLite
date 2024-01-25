from fastapi import APIRouter
from fastapi import Request,Form,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# importing storing_Email class to get email
from routers.Forgot_Password import storing_Email

# importing all variables in config file
from config.config import *

# importing CryptContext class to hash the password 
from passlib.context import CryptContext

# importing "re" module in Python provides regular expression matching operations[It is used for password strength checking ]
import re


# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# Instance for CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


# Forgot Password Changing router to display Forgot_Password_Changing page 
@router.get("/forgotPasswordChanging")
def get_forgotPasswordChanging(request: Request):
    return template.TemplateResponse("Forgot_Password_Changing.html", {"request": request})



# Forgot Password Changing router to display Forgot_Password_Changing page 
@router.post("/forgotPasswordChanging")
def post_forgotPasswordChanging(request: Request, Password:str = Form(...), Re_type_Password:str = Form(...)):
    try:
        user=Users.find_one({"Email":storing_Email.EmailId})
        # print(user)
        # Validating Password and Re_Type Password is same or not
        if(Password != Re_type_Password):
            return template.TemplateResponse("Forgot_Password_Changing.html",{"request":request,"error":"Password and Re-type Password should be same"})
        
        # Validating user entered password is different from the Old password
        elif (pwd_context.verify(Password,user["Password"])):
            return template.TemplateResponse("Forgot_Password_Changing.html",{"request":request,"error":"Password should not be the Old password"})
        
         # Checking password have capital letter, small letter and special character
        elif not (re.search("[A-Z]",Password) and re.search("[a-z]",Password) and re.search(r'[!@#$%^&*(),.?":{}|<>]',Password)):
            return template.TemplateResponse("Password_Changing.html", {"request": request, "error":"Password must contain Capital letters, Small letters and Special character......."})
        
        else:
            # Hashing password
            hash_password = pwd_context.hash(Password)

            #Updating the new password on the database
            Users.update_one({"Email": storing_Email.EmailId},{"$set": {"Password": hash_password}})
            return template.TemplateResponse("Goto_login.html",{"request":request})


    except Exception :
        raise HTTPException(status_code=500, detail="Internal Server Error") 

            