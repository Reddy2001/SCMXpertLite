from fastapi import APIRouter,HTTPException
from fastapi import Request,Form,Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

# importing "re" module in Python provides regular expression matching operations[It is used for password strength checking ]
import re

# importing Users variables in config file for Users Collection
from config.config import Users

# importing CryptContext to hash the password
from passlib.context import CryptContext


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


# Instance for CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
   

password_changing="Password_Changing.html"

# Password Changing router to display Password_Changing page 
@router.get("/passwordChanging", response_class=HTMLResponse, dependencies=[Depends(authenticate_user)])
def get_password_changing(request: Request,current_user: dict = Depends(get_current_user_from_cookie)):
    return template.TemplateResponse(password_changing, {"request": request,"name":current_user['username']})



# Password Changing router to display Password_Changing page 
@router.post("/passwordChanging", response_class=HTMLResponse, dependencies=[Depends(authenticate_user)])
def post_password_changing(request: Request, old_password:str = Form(...), 
                          new_password:str = Form(...), 
                          re_type_password:str = Form(...),
                          current_user: dict = Depends(get_current_user_from_cookie)):
    try:

        # fletching user details from database based on email
        user = Users.find_one({"Email":current_user["email"]})

        # Checking Old Password with the Password present on the database
        if not (pwd_context.verify(old_password,user["Password"])):
            return template.TemplateResponse(password_changing,{"request":request,"name":current_user['username'],"error":"Old Password is not matched with Original Password"})
        
        # Checking New Password is Different from Old password or not
        elif (old_password == new_password):
            return template.TemplateResponse(password_changing,{"request":request,"name":current_user['username'],"error":"New Password Should not be the Old Password"})

        # Validating Password and Re_Type Password is same or not
        elif(new_password !=re_type_password):
            return template.TemplateResponse(password_changing,{"request":request,"name":current_user['username'],"error":"New Password and Re-type Password should be same"})
        
        # Checking length of password[Password must contain 8 characters]
        elif (len(new_password)<8):
            return template.TemplateResponse(password_changing, {"request": request,"name":current_user['username'], "error":"Password should contain minimum 8 Characters......."})
        
        # Checking password have capital letter, small letter and special character
        elif not (re.search("[A-Z]",new_password) and re.search("[a-z]",new_password) and re.search(r'[!@#$%^&*(),.?":{}|<>]',new_password)):
            return template.TemplateResponse(password_changing, {"request": request,"name":current_user['username'], "error":"Password must contain Capital letters, Small letters and Special character......."})
        
        else:
            # Hashing the password
            hash_password = pwd_context.hash(new_password)

            #Updating the new password on the database
            Users.update_one({"Email": current_user["email"]} , {"$set": {"Password": hash_password}})
            
            return template.TemplateResponse("Dashboard.html",{"request":request,"name":current_user['username'],"message":"Password Changed Successfully"})


    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

            