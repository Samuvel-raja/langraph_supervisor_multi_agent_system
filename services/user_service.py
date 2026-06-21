
from models.user_model import User

class User_service:
   @staticmethod
   def create_user(data):
      try:
         google_id = data.get("google_id","")
         existing_user = User.objects(google_id=google_id).first()
         if existing_user:
            access_token = data.get("access_token")
            refresh_token = data.get("refresh_token")
            existing_user.access_token=access_token
            existing_user.refresh_token=refresh_token
            existing_user.save()
            return {
               "message":"User updated successfully"
            }
         user = User(**data)
         print("user created success")
         user.save()
         return {
            "message":"User created successfully"
         }
      except Exception as e:
         raise e
   
   @staticmethod
   def get_user_by_google_id(google_id):
      try:
         user = User.objects(google_id=google_id).first()
         return user
      except Exception as e:
         raise e

   @staticmethod
   def get_user_by_auth_token(auth_token):
      try:
         user = User.objects(auth_token=auth_token).first()
         print("user", user)
         return {
            "email":user.email,
            "access_token":user.access_token,
            "refresh_token":user.refresh_token
         }
      except Exception as e:
         raise e
