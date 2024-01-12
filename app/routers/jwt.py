from fastapi.responses import  RedirectResponse
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt
from jose import ExpiredSignatureError, JWTError

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




'''Using cookie'''


# Function to create JWT token
def create_jwt_token(user):
    # print(user)
    credentials = {"sub": user["UserName"],"Email":user["Email"],"Role":user["Role"]}
    expires = timedelta(minutes=JWT_Token.EXPIRE_MINUTES)
    to_encode = credentials.copy()
    expire = datetime.utcnow() + expires
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_Token.SECRET_KEY, algorithm=JWT_Token.ALGORITHM)
    # print("JWT  -   ",encoded_jwt)
    return encoded_jwt


# getting the JWT token using oauth2_scheme to decode it
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_Token.SECRET_KEY, algorithms=[JWT_Token.ALGORITHM])
        # print("payload is",payload)
        return payload
    except ExpiredSignatureError:
        raise credentials_exception
    except JWTError:
        raise credentials_exception


# Function to get jwt token and send token to get_current_user function to decode it 
async def get_current_user_from_cookie(request: Request):
    token = request.cookies.get("access_token")
    if token is None:
        return None

    try:
        payload = get_current_user(token)
        # print(payload)
        user_data = Users.find_one({"Email": payload["Email"]})
        return {"username": user_data["UserName"], "email": payload["Email"],"role":payload["Role"]}

    except JWTError:
        pass



# Function to delete jwt token from the cookie
def clear_access_token_cookie(response: RedirectResponse):

    # Removing access_token from the cookie
    response.delete_cookie(key="access_token", httponly=True)













# # Function to create JWT token
# def create_jwt_token(data: dict, expires_delta: timedelta):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + expires_delta
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, JWT_Token.SECRET_KEY, algorithm=JWT_Token.ALGORITHM)
#     return encoded_jwt


# # Dependency to get the JWT token
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=401,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, JWT_Token.SECRET_KEY, algorithms=[JWT_Token.ALGORITHM])
#         print("payload is",payload)
#         return payload
#     except jwt.ExpiredSignatureError:
#         raise credentials_exception
#     except jwt.JWTError:
#         raise credentials_exception


# #  Route to generate JWT 
# # @router.post("/token")
# # async def login_for_access_token(token : OAuth2PasswordRequestForm = Depends()):

# #     credentials = {"sub": token.username}
# #     expires = timedelta(minutes=JWT_Token.EXPIRE_MINUTES)
# #     access_token = create_jwt_token(credentials, expires)

# #     print("access_token",access_token)
# #     print(access_token)
    
# #     return {"access_token": access_token, "token_type": "bearer"}


# @router.post("/token")
# async def login_for_access_token(user,token:OAuth2PasswordRequestForm=Depends()):
#     if token.username == user["Email"]:
#         credentials = {"sub": user["Email"]}
#         expires = timedelta(minutes=JWT_Token.EXPIRE_MINUTES)
#         access_token = create_jwt_token(credentials, expires)
#         print("Generated Access Token:", access_token)
#         return {"access_token": access_token, "token_type": "bearer"}
    
#     else:
#         return {"error":None}









# Decode_JWT_Token function and returns UserName, Email and Expired time 
# def Decode_JWT_Token(token:str):
#     credentials_exception = HTTPException(
#         status_code=401,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, JWT_Token.SECRET_KEY, algorithms=[JWT_Token.ALGORITHM])
#         # print("payload is",payload)
#         return payload
#     except jwt.ExpiredSignatureError:
#         raise credentials_exception
#     except jwt.JWTError:
#         raise credentials_exception




# # Dependency to get the JWT token using oauth2_scheme
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     payload = Decode_JWT_Token(token)
#     if payload is None:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
#     return payload

