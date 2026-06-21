from fastapi import APIRouter
from fastapi.requests import Request
from controllers.user_controller import User_Controller

router = APIRouter()
user_controller = User_Controller()

@router.get("/user")
def get_user_by_auth_token(request: Request):
    auth_token = request.headers.get("authorization")
    return user_controller.get_user_by_auth_token(auth_token)

@router.get("/user/google")
def get_user_by_google_id(request: Request):
    google_id = request.query_params.get("google_id")
    return user_controller.get_user_by_google_id(google_id)

