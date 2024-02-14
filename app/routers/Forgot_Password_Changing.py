from fastapi import APIRouter
from fastapi import Request,Form,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# importing storing_Email class to get email
from routers.forgot_password import storing_email

# importing Users variables in config file for Users Collection
from config.config import Users

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

# storing Forgot_Password_Changing.html to the forgot_password_changing variable
forgot_password_changing="Forgot_Password_Changing.html"

# Password Changing router to display Password_Changing page 
@router.get("/forgotPasswordChanging")
def get_forgot_password_changing(request: Request):
    return template.TemplateResponse(forgot_password_changing, {"request": request})



# Password Changing router to display Password_Changing page 
@router.post("/forgotPasswordChanging")
def post_forgot_password_changing(request: Request, password:str = Form(...), re_type_password:str = Form(...)):
    try:
        user=Users.find_one({"Email":storing_email.email})

        # Validating Password and Re_Type Password is same or not
        if(password != re_type_password):
            return template.TemplateResponse(forgot_password_changing,{"request":request,"error":"Password and Re-type Password should be same"})
        
        # Validating user entered password is different from the Old password
        elif (pwd_context.verify(password,user["Password"])):
            return template.TemplateResponse(forgot_password_changing,{"request":request,"error":"Password should not be the Old password"})
        
        # Checking length of password[Password must contain 8 characters]
        elif len(password)<8:
            return template.TemplateResponse(forgot_password_changing, {"request": request, "error":"Password should contain minimum 8 Characters......."})

         # Checking password have capital letter, small letter and special character
        elif not (re.search("[A-Z]",password) and re.search("[a-z]",password) and re.search(r'[!@#$%^&*(),.?":{}|<>]',password)):
            return template.TemplateResponse(forgot_password_changing, {"request": request, "error":"Password must contain Capital letters, Small letters and Special character......."})
        
        else:
            # Hashing password
            hash_password = pwd_context.hash(password)

            #Updating the new password on the database
            Users.update_one({"Email": storing_email.email},{"$set": {"Password": hash_password}})
            return template.TemplateResponse("Goto_Login.html",{"request":request})


    except Exception :
        raise HTTPException(status_code=500, detail="Internal Server Error") 

            
