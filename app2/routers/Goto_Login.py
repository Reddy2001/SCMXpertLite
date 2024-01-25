from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



# To create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# Goto Login router to display Goto_Login page 
@router.get("/gotoLogin")
def get_GotoLogin(request: Request):
    return template.TemplateResponse("Goto_Login.html", {"request": request})


