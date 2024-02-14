from fastapi import HTTPException,Depends
from routers.jwt import get_current_user_from_cookie


# Authenticate_User function to check if the user is authenticated or not
async def authenticate_user(current_user: dict = Depends(get_current_user_from_cookie)):
    if current_user is None or "username" not in current_user or "email" not in current_user or "role" not in current_user:
       # Redirect unauthenticated user to the home page
        url = "/"
        raise HTTPException(status_code=307, detail="Not authenticated", headers={"Location": url})
    # print(current_user,"current user")
    return True
        
