from fastapi import APIRouter
from fastapi import Request,Form,Depends,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from routers.jwt import get_current_user_from_cookie


#importing all variables in config file
from config.config import *

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")



# Authenticate_User function to check if the user is authenticated or not
async def Authenticate_User(current_user: dict = Depends(get_current_user_from_cookie)):
    if current_user is None or "username" not in current_user or "email" not in current_user or "role" not in current_user:
       # Redirect unauthenticated user to the home page
        url = "/"
        raise HTTPException(status_code=307, detail="Not authenticated", headers={"Location": url})
    return current_user
  

# Feedback router to display Feedback page 
@router.get("/feedback", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
def get_feedback(request: Request):
    return template.TemplateResponse("Feedback.html", {"request": request})



# Feedback router to take the feedback and store it on the database
@router.post("/feedback", response_class=HTMLResponse, dependencies=[Depends(Authenticate_User)])
def post_feedback(request: Request, 
                  rating: str = Form(...), 
                  opinion: str = Form(...),
                  current_user: dict = Depends(get_current_user_from_cookie)):
    # if Feedback.find({}):
        # return template.TemplateResponse("Dashboard.html",{"request":request,"error":"Your Feedback already submitted...."})
    feedback={
        "Email":current_user["email"],
        "rating":rating,
        "opinion":opinion
    }
    Feedback.insert_one(feedback)
    return template.TemplateResponse("Dashboard.html",{"request":request,"success":"Thank you for your Feedback...."})
