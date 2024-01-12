from fastapi import APIRouter 
from fastapi import Request, HTTPException,Cookie
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,RedirectResponse
from routers.jwt import clear_access_token_cookie
# create instance of APIRouter
router = APIRouter()

# To access the html folder
template = Jinja2Templates(directory="templates")

# To add css to html
router.mount("/static", StaticFiles(directory="static"), name="static")


# logout route to delete the access token and redirect to home page
@router.get("/logout", response_class=HTMLResponse)
async def logout(request: Request, access_token: str = Cookie(None)):
   
    try:

        # redirecting the page to home page
        response = RedirectResponse(url="/")

        # clear_access_token_cookie function is used to remove token from the cookie

        clear_access_token_cookie(response)
        return response 
    
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}")