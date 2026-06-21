from services.user_service import User_service

class User_Controller:
    def __init__(self):
        self.user_service = User_service()
    
    def get_user_by_auth_token(self,auth_token):
        return self.user_service.get_user_by_auth_token(auth_token)
