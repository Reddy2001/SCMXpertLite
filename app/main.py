from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles




''' Importing all route files '''

# "/" route file
from routers.home import router as home_route

# "/signup" route file
from routers.register import router as signup_route

# "/singin" route file
from routers.login import router as signin_route

# "/dashboard" route file
from routers.dashboard import router as dashboard_route

# "/myAccount" route file
from routers.my_account import router as myAccount_route

# "/newShipment" route file
from routers.new_shipment import router as newShipment_route

# "/feedback" route file
from routers.feedback import router as Feedback_route

# "/myShipment" route file
from routers.my_shipment import router as myShipment_route

# "/deviceData" route file
from routers.device_data import router as deviceData_route

# "/forgotPassword" route file
from routers.forgot_password import router as forgotPassword_route

# "/otpValidation" route file
from routers.otp_validation import router as otpValidation_route

# "/forgotPasswordChanging" route file
from routers.forgot_password_changing import router as ForgotPasswordChanging_route

# "/gotoLogin" route file
from routers.goto_login import router as gotoLogin_route

# "/logout" route file
from routers.logout import router as logout_route

# "/passwordChanging" route file
from routers.password_changing import router as passwordChanging_route

# "/deviceDataUser" route file
from routers.device_data_user import router as deviceDataUser_route

# "/changeUserRole" route file
from routers.change_user_role import router as changeUserRole_route

# "/viewUserFeedback" route file
from routers.view_user_feedback import router as viewUserFeedback

# "/contactSuperAdmin" route file
from routers.contact_super_admin import router as superAdminPage


# To create instance of fastapi
app = FastAPI()


# To access the html folder
template = Jinja2Templates(directory="templates")


# To add css to html
app.mount("/static", StaticFiles(directory="static"), name="static")




# To include routes
app.include_router(home_route)
app.include_router(signup_route)
app.include_router(signin_route)
app.include_router(dashboard_route)
app.include_router(myAccount_route)
app.include_router(newShipment_route)
app.include_router(Feedback_route)
app.include_router(myShipment_route)
app.include_router(deviceData_route)
app.include_router(forgotPassword_route)
app.include_router(otpValidation_route)
app.include_router(ForgotPasswordChanging_route)
app.include_router(gotoLogin_route)
app.include_router(logout_route)
app.include_router(passwordChanging_route)
app.include_router(deviceDataUser_route)
app.include_router(changeUserRole_route)
app.include_router(viewUserFeedback)
app.include_router(superAdminPage)