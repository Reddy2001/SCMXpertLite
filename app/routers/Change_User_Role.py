from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# importing Users variables in config file for Users Collection
from config.config import Users

# Importing get_current_user_from_cookie method to take the username,email and expired time
from routers.jwt import get_current_user_from_cookie

#  Importing Authenticate_User() function to check the user is Authenticated user or not
from routers.authenticate_user import Authenticate_User


# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")



# Change_User_Role router to display Change_User_Role page 
@router.get("/changeUserRole", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
def get_ChangeUserRole(request: Request,current_user: dict = Depends(get_current_user_from_cookie)):
    try:
        # Except Admin anyone should not access that route
        if current_user["role"] != "Super Admin":
            return template.TemplateResponse("Dashboard.html",{"request":request,"name":current_user['username'],"Error":"Only Super Admin can access Change User Role page","role":"User"})
        
        return template.TemplateResponse("Change_User_Role.html", {"request": request,"name":current_user['username']})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 


# Change_User_Role router to display Change_User_Role page 
@router.post("/changeUserRole", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
def post_ChangeUserRole(request: Request,
                        Email:str = Form(...),
                        current_user: dict = Depends(get_current_user_from_cookie)):
    try:
        # Fletching user details from DB based on email
        user=Users.find_one({"Email":Email})

        # Checking the user is Exists based on the given Email
        if user is None:
            return template.TemplateResponse("Change_User_Role.html", {"request": request,"name":current_user['username'],"error":"Email Doesn't Exist.."})
        
        elif user["Role"] == "Admin":
            return template.TemplateResponse("Change_User_Role.html",{"request":request,"name":current_user['username'],"error":"He/She is already an Admin"})
        
        # If user exists admin will change the role of user
        else:

            #Updating the role on the database
            Users.update_one({"Email": user["Email"]} , {"$set": {"Role": "Admin"}})
            return template.TemplateResponse("Change_User_Role.html",{"request":request,"name":current_user['username'],"message": "Successfully Changed role of User"})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 

