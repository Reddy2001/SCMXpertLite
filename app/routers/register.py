from fastapi import APIRouter
from fastapi import Request,Form,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from passlib.context import CryptContext

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


# Signup router to display register page
@router.get("/signup")
def get_signup(request: Request):
    return template.TemplateResponse("register.html", {"request": request})


# Signup router to take inputs from the user and validate them, then stored in database
@router.post("/signup")
def post_signup(request: Request, name: str = Form(...), mail: str = Form(...), password: str = Form(...), con_password: str = Form(...)):
    try:

        # Checking length for the username[Username must be have more than 6 characters]
        if len(name)<6:
            return template.TemplateResponse("register.html", {"request": request, "error":"Username must consists more than 6 characters......."})
        
        # Checking length of password[Password must contain 8 characters]
        elif len(password)<8:
            return template.TemplateResponse("register.html", {"request": request, "error":"Password should contain minimum 8 Characters......."})
        
        # Checking password have capital letter, small letter and special character
        elif not (re.search("[A-Z]",password) and re.search("[a-z]",password) and re.search(r'[!@#$%^&*(),.?":{}|<>]',password)):
            return template.TemplateResponse("register.html", {"request": request, "error":"Password must contain Capital letters, Small letters and Special character......."})
        
        # Validating password and conform password is same or not
        elif password != con_password:
            return template.TemplateResponse("register.html", {"request": request, "error":"Password and Conform Password should be same......."})
        
        # Checking mail is Unique or not 
        elif Users.find_one({"Email":mail}):
            return template.TemplateResponse("register.html", {"request": request, "error":"Email already exists......."})
        
        # Hashing the Password 
        hash_password = pwd_context.hash(password)


        try:
            # Schema for userDetails
            data=UserDetail(UserName=name,Email=mail,Password=hash_password,Role="User")

            
        except:
            return template.TemplateResponse("register.html", {"request": request, "error":"Email format is Wrong......."})


        # Pushing data by converting it into dictionary to the database collection
        Users.insert_one(dict(data))

        return template.TemplateResponse("login.html", {"request": request,"success":"Successfully registered, Please login to continue"})
    

    except:
        raise HTTPException(status_code=500, detail="Internal Server Error") 