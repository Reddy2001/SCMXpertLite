from fastapi import APIRouter,Form
from fastapi import Request,Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi import Cookie

# importing all variables in config file
from config.config import *

# importing create_jwt_token method to create JWT Token
from routers.jwt import create_jwt_token

# importing CryptContext class to hash the password 
from passlib.context import CryptContext

# create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")

# Instance for CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")



# Signin router to display login page 
@router.get("/signin")
def get_signin(request: Request):
    return template.TemplateResponse("login.html", {"request": request})



# Signin route to take inputs from the login.html
@router.post("/signin")
async def signin(request: Request, username:str = Form(...),password:str = Form(...)):


     
    try:

        # Storing the details of user based on emain entered by the user
        user = Users.find_one({"Email": username})

        # Validating email is exits in database 
        if user==None:
            return JSONResponse(content={"Error":"User Doesn't exist with this Email"},status_code=401)
        
        # Validation the hashed password and the user entered password with "verify method"
        elif (pwd_context.verify(password,user["Password"])):
            
            access_token = create_jwt_token(user)
            return JSONResponse(content={"access_token":access_token,"username":user['UserName'],"email":user["Email"],"role":user["Role"]},status_code=200)
        
        # If user entered wrong password Error Message will be printed on login page
        else:
            return JSONResponse(content={"Error":"Invalid Password"},status_code=401)
    
    except Exception as e:
        print(e)
