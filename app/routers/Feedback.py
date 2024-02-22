from fastapi import APIRouter
from fastapi import Request,Form,Depends,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,RedirectResponse

# importing feedbackDetails model from models file
from models.model import FeedbackDetails

# Importing get_current_user_from_cookie method to take the username,email and expired time
from routers.jwt import get_current_user_from_cookie


#  Importing authenticate_user() function to check the user is Authenticated user or not
from routers.authenticate_user import authenticate_user

#importing Feedback variables in config file for Feedback Collection
from config.config import Feedback

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# Feedback router to display Feedback page 
@router.get("/feedback", response_class=HTMLResponse, dependencies=[Depends(authenticate_user)])
def get_feedback(request: Request):
    return template.TemplateResponse("Feedback.html", {"request": request})



# Feedback router to take the feedback and store it on the database
@router.post("/feedback", response_class=HTMLResponse, dependencies=[Depends(authenticate_user)])
def post_feedback(request: Request, 
                  rating: int = Form(...), 
                  opinion: str = Form(...),
                  current_user: dict = Depends(get_current_user_from_cookie)):
    try:
        # schema for feedback
        feedback=FeedbackDetails(name=current_user['username'],
                                 Email=current_user["email"],
                                 rating=rating,
                                 opinion=opinion)
        
        # inserting feedback details by converting it into dict() to feedback collection
        Feedback.insert_one(dict(feedback))
        response= RedirectResponse("/dashboard", status_code=302)
        return response
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error") 
