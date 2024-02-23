from fastapi import APIRouter
from fastapi import Request,Depends,Form,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse,RedirectResponse

# importing Users variables in config file for Users Collection
from config.config import Users

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

# Assigning login.html in login variable
login="login.html"

# Signin router to display login page 
@router.get("/signin")
def get_signin(request: Request,error:str | None=None):
    # print("error",error)
    return template.TemplateResponse(login, {"request": request,"message":error})



# Signin route to take inputs from the login.html
@router.post("/signin", response_class=HTMLResponse)
async def signin(request: Request, forms: OAuth2PasswordRequestForm = Depends(),
                 captcha:str = Form(...),
                 original_captcha:str = Form(...)):
    try:

        # Storing the details of user based on emain entered by the user
        user = Users.find_one({"Email": forms.username})

        # Validating email is exits in database 
        if user==None:
            return template.TemplateResponse(login,{"request":request, "message":"User doesn't exist...."})
        
        # Validating Password
        elif (pwd_context.verify(forms.password,user["Password"])):
            if original_captcha == captcha:
            
                access_token = create_jwt_token(user)

                response= RedirectResponse("/dashboard", status_code=302)


                '''Here we are using Httponly flag, When the HttpOnly flag is set on a cookie,
                    it instructs the browser not to expose the cookie to client-side scripts (e.g., JavaScript).
                    This means that the cookie is only accessible by the server and cannot be read or modified by
                    client-side scripts running in the user's browser and we can also use "Secure" flag, The Secure 
                    flag indicates that the cookie should only be sent over secure connections (i.e., HTTPS). 
                    If a cookie has the Secure flag set and the connection is not secure, the browser will not send
                    the cookie in the request.'''
                
                response.set_cookie(key="access_token", value=access_token, httponly=True)

                return response
            else:
                return template.TemplateResponse(login,{"request":request,"message":"Please enter Valid captcha"})
        
        # If user entered wrong password Error Message will be printed on login page
        else:
            return template.TemplateResponse(login,{"request":request, "message":"Email or Password is Incorrect...."})
        
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error") 
