from fastapi import APIRouter
from fastapi import Request,Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse,RedirectResponse


# importing all variables in config file
from config.config import *


from routers.jwt import create_jwt_token

from passlib.context import CryptContext

# create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")

# Instance for CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


# async def is_valid(self):
#         form = await self.request.form()
#         # authenticate_user(self.login_user, self.login_password)
#         captcha_response = form.get("g-recaptcha-response")
#         if not captcha_response:
#             self.errors.append("Please Verify captcha.")
#         if not self.errors:
#             return True
#         return False  


#Signin router to display login page 
@router.get("/signin")
def get_signin(request: Request):
    return template.TemplateResponse("login.html", {"request": request})


@router.post("/signin", response_class=HTMLResponse)
async def signin(request: Request, forms: OAuth2PasswordRequestForm = Depends()):

    # Storing the details of user based on emain entered by the user
    user = Users.find_one({"Email": forms.username})

    # getting captcha response
    form = await request.form()
    captcha_response = form.get("_grecaptcha")
    # print(captcha_response)

    # Validating email is exits in database 
    if user==None:
        return template.TemplateResponse("login.html",{"request":request, "message":"User doesn't exist...."})
    
    # elif not captcha_response:
    #      return template.TemplateResponse("login.html",{"request":request, "message":"Please Verify Captcha...."})
    
    # Validation the hashed password and the user entered password with "verify method"
    elif (pwd_context.verify(forms.password,user["Password"])):
        
        # token=await login_for_access_token(user)
        # access_token=token["access_token"]
        # print("Access Token for user:", access_token)
        # return template.TemplateResponse("dashboard.html",{"request":request,"access_token":access_token})

        access_token = create_jwt_token(user)
        # prints access token on terminal
        print("access_token",access_token)
        
        # response = template.TemplateResponse("Dashboard.html",{"request":request})
        response= RedirectResponse("/dashboard", status_code=302)
        response.set_cookie(key="access_token", value=access_token, httponly=True)
        return response
    
    # If user entered wrong password Error Message will be printed on login page
    else:
        return template.TemplateResponse("login.html",{"request":request, "message":"Email or Password is Incorrect...."})
    
