
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
