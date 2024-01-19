from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


#importing all route files 
from routers.home import router as home_route
from routers.register import router as signup_route
from routers.login import router as signin_route
from routers.Dashboard import router as dashboard_route
from routers.MyAccount import router as myAccount_route
from routers.NewShipment import router as newShipment_route
from routers.Feedback import router as Feedback_route
from routers.MyShipment import router as myShipment_route
from routers.DeviceData import router as deviceData_route
from routers.jwt import router as jwt_router
from routers.Forgot_Password import router as forgotPassword_route
from routers.OTP_Validation import router as otpValidation_route
from routers.Forgot_Password_Changing import router as ForgotPasswordChanging_route
from routers.Goto_Login import router as gotoLogin_route
from routers.logout import router as logout_route
from routers.Password_Changing import router as passwordChanging_route
from routers.Device_Data_User import router as deviceDataUser_route
from routers.Change_User_Role import router as changeUserRole_route
from routers.View_User_Feedback import router as viewUserFeedback



#To create instance of fastapi
app = FastAPI()


#To access the html folder
template = Jinja2Templates(directory="templates")


#To add css to html
app.mount("/static", StaticFiles(directory="static"), name="static")




#To include routes
app.include_router(home_route)
app.include_router(signup_route)
app.include_router(signin_route)
app.include_router(dashboard_route)
app.include_router(myAccount_route)
app.include_router(newShipment_route)
app.include_router(Feedback_route)
app.include_router(myShipment_route)
app.include_router(deviceData_route)
app.include_router(jwt_router)
app.include_router(forgotPassword_route)
app.include_router(otpValidation_route)
app.include_router(ForgotPasswordChanging_route)
app.include_router(gotoLogin_route)
app.include_router(logout_route)
app.include_router(passwordChanging_route)
app.include_router(deviceDataUser_route)
app.include_router(changeUserRole_route)
app.include_router(viewUserFeedback)