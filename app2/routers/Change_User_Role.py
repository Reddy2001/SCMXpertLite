from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi import Request, Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# importing all variables in config file
from config.config import *

# Importing get_current_user_from_SessionStorage method to take the username,email and expired time
from routers.jwt import get_current_user_from_SessionStorage

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")



# Change_User_Role router to display Change_User_Role page 
@router.get("/changeUserRole")
def get_ChangeUserRole(request: Request):
    try:
        return template.TemplateResponse("Change_User_Role.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 


# Change_User_Role router to display Change_User_Role page 
@router.post("/changeUserRole")
def post_ChangeUserRole(request: Request,
                        Email:str = Form(...),
                        current_user: dict = Depends(get_current_user_from_SessionStorage)):
    try:
        # Fletching user details from DB based on email
        user=Users.find_one({"Email":Email})
        # print("user -- >",user)
        # Checking the user is Exists based on the given Email
        if user is None:
            return JSONResponse(content={"Error":"Email Doesn't Exist..."},status_code=400)
        
        # If user exists admin will change the role of user
        elif user['Role'] == "Admin":
            return JSONResponse(content={"Error":"He/She is already an Admin"},status_code=400)
        elif current_user["role"] !="Admin":
            return JSONResponse(content={"Error":"You are not Admin"},status_code=400)
        else:

            #Updating the role on the database
            result= Users.update_one({"Email": user["Email"]} , {"$set": {"Role": "Admin"}})
            return JSONResponse(content={"message":"Role Changed Successfully.."},status_code=200)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 

