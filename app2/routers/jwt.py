from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt
from jose import JWTError

#importing all variables in config file
from config.config import *

# To create instance of APIRouter
router = APIRouter()

#To access the html folder
template = Jinja2Templates(directory="templates")


#To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# OAuth2PasswordBearer is a dependency that handles token extraction
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin")




'''Using cookies to Store the Jwt Token'''


# Function to create JWT token
def create_jwt_token(user):

    credentials = {"sub": user["UserName"],"Email":user["Email"],"Role":user["Role"]}
    expires = timedelta(minutes=JWT_Token.EXPIRE_MINUTES)
    to_encode = credentials.copy()
    expire = datetime.utcnow() + expires
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_Token.SECRET_KEY, algorithm=JWT_Token.ALGORITHM)
    # print("JWT  -   ",encoded_jwt)
    return encoded_jwt



# Function to get jwt token and returns username, email and role of the user 
async def get_current_user_from_SessionStorage(token: str = Depends(oauth2_scheme)):
    try:
        # print(token,'in jwt')
        payload = jwt.decode(token, JWT_Token.SECRET_KEY, algorithms=[JWT_Token.ALGORITHM])
        # print(payload)
        user_data = Users.find_one({"Email": payload["Email"]})
        # print(user_data)
        return {"username": user_data["UserName"], "email": payload["Email"],"role":payload["Role"]}
        # return user_data
    except JWTError:
        return JSONResponse(content={},status_code=500)


