from fastapi import APIRouter
from fastapi import Request,Form,HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Importing Stored OTP to validate with user Entering OTP
from routers.Forgot_Password import storing_OTP

# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# OTP Validation router to display OTP Validation page 
@router.get("/otpValidation")
def get_OTPValidation(request: Request):
    return template.TemplateResponse("OTP_Validation.html", {"request": request})


# OTP Validation router to Take OTP from the user
@router.post("/otpValidation")
def post_OTPValidation(request:Request, User_otp: int=Form(...)):
    print("otp page",storing_OTP.OTP)
    print("user_OTP",User_otp)

    try:
        
        # Comparing User entered OTP with Generated OTP
        if (User_otp == storing_OTP.OTP):
            return template.TemplateResponse("Forgot_Password_Changing.html",{"request":request})
        
        # If user entered Wrong OTP it prints error message on the OTP_Validation page
        else:
            return template.TemplateResponse("OTP_Validation.html",{"request":request,"error":"Incorrect OTP, Please enter valid OTP"})
        

    except KeyError:
        raise HTTPException(status_code=400, detail="Missing Parameters")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

