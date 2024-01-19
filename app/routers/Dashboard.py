from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Importing get_current_user_from_cookie method to take the username,email and expired time
from routers.jwt import get_current_user_from_cookie


# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")

# OAuth2PasswordBearer is a dependency that handles token extraction
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# Dashboard router to display Dashboard page  ,current_user: dict = Depends(get_current_user)  , "user": current_user
# @router.get("/dashboard")
# def get_dashboard(request: Request,access_token : str = Depends(get_current_user)):
#     print("get method",access_token)

#     if access_token:
#         return template.TemplateResponse("Dashboard.html", {"request": request})
#     else:
#         return template.TemplateResponse("login.html", {"request": request})



        
# Authenticate_User function to check if the user is authenticated or not
async def Authenticate_User(current_user: dict = Depends(get_current_user_from_cookie)):
    if current_user is None or "username" not in current_user or "email" not in current_user or "role" not in current_user:
       # Redirect unauthenticated user to the home page
        url = "/"
        raise HTTPException(status_code=307, detail="Not authenticated", headers={"Location": url})
    return current_user
        



#  Dashboard router to display Dashboard page 
@router.get("/dashboard", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
async def get_dashboard(request: Request, current_user: dict = Depends(get_current_user_from_cookie)):
    try:
        if current_user:
            # print(current_user["role"])
            return template.TemplateResponse("dashboard.html", {"request": request, "name":current_user["username"],"role":current_user["role"]})
    except Exception:
        raise HTTPException(status_code=500, detail=f"Internal Server Error") 

