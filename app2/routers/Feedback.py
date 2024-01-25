from fastapi import APIRouter
from fastapi import Request,Form,Depends,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi import Header, HTTPException



# Importing get_current_user_from_SessionStorage method to take the username,email and expired time
from routers.jwt import get_current_user_from_SessionStorage

#importing all variables in config file
from config.config import *

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")



# Feedback router to display Feedback page 
@router.get("/feedback")
def get_feedback(request: Request):
    return template.TemplateResponse("Feedback.html", {"request": request})


# Feedback router to take the feedback and store it on the database
@router.post("/feedback")
def post_feedback(request: Request, 
                  rating: str = Form(...), 
                  opinion: str = Form(...),
                  current_user:dict = Depends(get_current_user_from_SessionStorage)):
    print(rating,opinion,current_user)
    try:
        feedback={
            "name":current_user['username'],
            "Email":current_user["email"],
            "rating":rating,
            "opinion":opinion
        }
        Feedback.insert_one(feedback)
        return JSONResponse(content={"messege":"Feedback saved Successfully"},status_code=200)
    except Exception:
        return JSONResponse(content={"Error":"Internal Server Error"},status_code=500)
