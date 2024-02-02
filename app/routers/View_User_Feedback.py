from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Importing get_current_user_from_cookie method to take the username,email and expired time
from routers.jwt import get_current_user_from_cookie


#  Importing Authenticate_User() function to check the user is Authenticated user or not
from routers.Authenticate_User import Authenticate_User


# importing all variables in config file
from  config.config import *

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# View_User_Feedback router to display View_User_Feedback page along with User's Feedback
@router.get("/viewUserFeedback", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
def get_View_User_Feedback(request: Request, current_user: dict = Depends(get_current_user_from_cookie)):
    
    try:
        if current_user["role"] == 'Admin':
            # Storing Feedback details from database on a list
            FeedbackData=list(Feedback.find({}))
            # print("Feedback data",FeedbackData)
            return template.TemplateResponse("View_User_Feedback.html", {"request": request,"FeedbackData":FeedbackData, "name":current_user["username"]})
        else:
            return template.TemplateResponse("login.html",{"request":request,"message":"Only Admin can access the User's Feedback page"})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 
    


