from fastapi import APIRouter
from fastapi import Request,Form,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from passlib.context import CryptContext

# importing random
import random

# importing UserDetails from models file
from models.model import UserDetail

# importing Users variables in config file for Users Collection
from  config.config import Users

# importing "re" module in Python provides regular expression matching operations[It is used for password strength checking]
import re

# Instance for CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# Assigning register.html in register variable
register_page="register.html"

def id_generator():
    return random.randint(1000000,9999999)
    

# Signup router to display register page
@router.get("/signup")
def get_signup(request: Request):
    return template.TemplateResponse(register_page, {"request": request})


# Signup router to take inputs from the user and validate them, then stored in database
@router.post("/signup")
def post_signup(request: Request, name: str = Form(...), mail: str = Form(...), password: str = Form(...), con_password: str = Form(...)):
    try:
        id = id_generator()
        # Checking that Id is unique or not
        while True:
            if Users.find_one({"Id":id}):
                id=id_generator()
            break


        # Schema for userDetails
        data=UserDetail(UserName=name,Email=mail,Password=password,Role="User",Id=id)
       

        # Checking password have capital letter, small letter and special character
        if not (re.search("[A-Z]",password) and re.search("[a-z]",password) and re.search(r'[!@#$%^&*(),.?":{}|<>]',password)):
            return template.TemplateResponse(register_page, {"request": request, "error":"Password must contain Capital letters, Small letters and Special character......."})
        
        # Validating password and conform password is same or not
        elif password != con_password:
            return template.TemplateResponse(register_page, {"request": request, "error":"Password and Conform Password should be same......."})
        
        # Checking mail is Unique or not 
        elif Users.find_one({"Email":mail}):
            return template.TemplateResponse(register_page, {"request": request, "error":"Email already exists......."})
        
        # Hashing the Password 
        hash_password = pwd_context.hash(password)

        userData=dict(data)

        # updating password with hash password on the userData
        userData['Password']=hash_password

        # Pushing userData to the UserData collection 
        Users.insert_one(userData)

        return template.TemplateResponse("login.html", {"request": request,"success":"Successfully registered, Please login to continue"})
    
    except ValueError:
        return template.TemplateResponse(register_page, {"request": request, "error":"Password should contain minimum 8 Characters......."})
    
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error") 