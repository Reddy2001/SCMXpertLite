from fastapi import APIRouter
from fastapi import Request,Form
from fastapi import HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# importing packages to send otp to email
import random
import smtplib

# importing Users variables in config file for Users Collection and importing sender mail and sender mail password for sending mail
from config.config import Users,Sender_Mail,Sender_Mail_Password


# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")



# Generating OTP to send Mail
def generate_otp():
    otp=random.randint(100000,999999)
    return otp



# Connecting to the SMTP Server
async def smtp_connection(otp,receiver_email):
    
    # Creating server
    server=smtplib.SMTP('smtp.gmail.com',587)

    print(otp,receiver_email)
    # Adding TLS security 
    server.starttls()
    email=Sender_Mail
    password=Sender_Mail_Password
    server.login(email,password)
    msg='Hello, Your OTP is '+str(otp)
    receiver=receiver_email 
    
    # Sending email to receiver
    server.sendmail(email,receiver,msg)

    # Closing server
    server.quit()



# Global Variables
receiver_email=""
otp = None



# Forgot_Password router to display Forgot_Password page 
@router.get("/forgotPassword")
def get_forgot_password(request: Request):
    return template.TemplateResponse("Forgot_Password.html", {"request": request})



# Forgot_Password router to take mail from the user and send mail to that entered mail
@router.post("/forgotPassword")
async def post_forgot_password(request: Request,email: str=Form(...)):

    global receiver_email
    receiver_email = email

    try:

        # Validating Mail is present in database or not, if not it prints error message
        if not Users.find_one({"Email": email}):
            print("users",Users.find_one({"Email":email}))
            return template.TemplateResponse("Forgot_Password.html", {"request": request, "error": "Email doesn't exist"})
        
        # If Mail is there in Database then we send OTP to the registered mail
        else:
            global otp

            # Calling Generate_OTP method to generate otp
            otp = generate_otp()

            print("genrated otp",otp)

            # Storing otp and receiver mail to validate the otp
            otp_number(otp)
            email_id(receiver_email)

            print("Receiver mail",receiver_email)

            '''   
            smtp_connection method is called to send OTP mail to the User.
            Here we are commiting this method call, because this system don't have Gmail Access.
            So it will not work in this system. If any system have Gmail Access this code will run effectively. 
            '''
            # server_setup= await smtp_connection(otp, receiver_email)
            

            return template.TemplateResponse("OTP_Validation.html", {"request": request})

    except KeyError:
        raise HTTPException(status_code=400, detail="Missing Parameters")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Storing OTP Number
def otp_number(number):
    storing_otp.otp=number

class storing_otp:
    def __init__(self):
        otp=None


#storing Email Address
def email_id(email):
    storing_email.email=email

class storing_email:
    def __init__(self):
        email=None
