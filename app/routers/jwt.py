from fastapi.responses import  RedirectResponse
from fastapi import Request
from datetime import datetime, timedelta
from jose import jwt
from jose import ExpiredSignatureError, JWTError
from starlette.exceptions import HTTPException as starletteException

#importing JWT_Token class in config file
from config.config import JwtToken


        #################      Using cookies to Store the Jwt Token    ######################



'''Creating JWT Token'''

def create_jwt_token(user):

    credentials = {"sub": user["UserName"],"Email":user["Email"],"Role":user["Role"]}
    expires = timedelta(minutes=JwtToken.EXPIRE_MINUTES) # Expire time will be 60 min
    to_encode = credentials.copy()
    expire = datetime.utcnow() + expires
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JwtToken.SECRET_KEY, algorithm=JwtToken.ALGORITHM)
    return encoded_jwt





'''Decoding JWT Token'''

# getting the JWT token to decode it 
def get_current_user(token: str ):

    try:
        payload = jwt.decode(token, JwtToken.SECRET_KEY, algorithms=[JwtToken.ALGORITHM])
        # print("payload is",payload)
        return payload
    except ExpiredSignatureError:
        # response.delete_cookie(key="access_token", httponly=True)
        raise starletteException(
            status_code=302,
            detail="Token has expired",
            headers={"Location": f"/signin?error=Token has expired, Please login Again"}
        )
    except JWTError:
        raise starletteException(
            status_code=302,
            detail="Token has expired",
            headers={"Location": f"/signin?error=Token has expired,Please login Again"}
        )


# Function to get jwt token and send token to get_current_user function to decode it 
async def get_current_user_from_cookie(request: Request):
    token = request.cookies.get("access_token")
    if token is None:
        return None

    try:
        payload = get_current_user(token)
        # print(payload)
        return {"username": payload["sub"], "email": payload["Email"],"role":payload["Role"]}

    except JWTError:
        pass





'''Deleting JWT token'''

# Function to delete jwt token from the cookie
def clear_access_token_cookie(response: RedirectResponse):

    # Removing access_token from the cookie
    response.delete_cookie(key="access_token", httponly=True)
