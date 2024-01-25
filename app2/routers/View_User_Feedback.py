from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Importing get_current_user_from_SessionStorage method to take the username,email and expired time
from routers.jwt import get_current_user_from_SessionStorage

# importing all variables in config file
from  config.config import *

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")



# View_User_Feedback router to display View_User_Feedback page 
@router.get("/viewUserFeedback")
def get_View_User_Feedback(request: Request):
    try:

        return template.TemplateResponse("View_User_Feedback.html", {"request": request})
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}") 
    

# View_User_Feedback router to display View_User_Feedback page along with Users Feedback
@router.get("/viewUserFeedbacks")
def post_View_User_Feedback(request: Request,current_user:dict = Depends(get_current_user_from_SessionStorage)):
    print(current_user)
    try:
        if current_user["role"] == "Admin":
            FeedbackData=list(Feedback.find({},{"_id":0}))
            # print(FeedbackData)
            return JSONResponse(content=(FeedbackData),status_code=200)
        
    except Exception as e:
        return JSONResponse(content={"Error":"Internal Server Error"},status_code=500)
    
