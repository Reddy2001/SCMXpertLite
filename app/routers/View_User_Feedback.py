from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Importing get_current_user_from_cookie method to take the username,email and expired time
from routers.jwt import get_current_user_from_cookie


#  Importing Authenticate_User() function to check the user is Authenticated user or not
from routers.authenticate_user import authenticate_user


# importing Feedback variables in config file for Feedback Collection
from  config.config import Feedback

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# View_User_Feedback router to display View_User_Feedback page along with User's Feedback
@router.get("/viewUserFeedback", response_class=HTMLResponse, dependencies=[Depends(authenticate_user)])
def get_view_user_feedback(request: Request, current_user: dict = Depends(get_current_user_from_cookie)):
    
    try:
        if current_user["role"] == 'Admin' or current_user["role"] == 'Super Admin':
            # Storing Feedback details from database on a list
            feedback_data=list(Feedback.find({}))
            # print("Feedback data",FeedbackData)
            return template.TemplateResponse("View_User_Feedback.html", {"request": request,"FeedbackData":feedback_data, "name":current_user["username"]})
        else:
            return template.TemplateResponse("Dashboard.html",{"request":request,"Error":"Only Admins can access the User's Feedback page","role":"User"})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 
    


