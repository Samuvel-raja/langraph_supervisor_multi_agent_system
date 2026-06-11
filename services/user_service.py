from authlib.integrations.starlette_client import OAuth, OAuthError
from models.user_model import User
from fastapi.responses import JSONResponse

class User_service:
   async def create_user_service(self, user: dict):
      try:
         existing_user = User.objects(email=user.get("email"))
         if existing_user:
            return JSONResponse({
               "status": 400,
               "message": "User already exists"
            })
         user = User(**user)
         user.save()
         return JSONResponse({
            "status": 201,
            "message": "User created successfully"
         })
      except Exception as e:
         return JSONResponse({
            "status": 500,
            "message": str(e)
         })