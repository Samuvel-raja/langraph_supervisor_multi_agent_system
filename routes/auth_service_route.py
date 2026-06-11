from fastapi import APIRouter
from controllers.auth_controller import Auth_Controller
from fastapi.requests import Request

auth_controller = Auth_Controller()

auth_router = APIRouter()

@auth_router.get("/login")
async def google_login(request:Request):
    url = request.url_for("auth")
    return await auth_controller.login(request,url)

@auth_router.get("/auth")
async def auth(request:Request):
    return await auth_controller.callback(request)