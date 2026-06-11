from services.auth_service import Auth_Service

class Auth_Controller:
    def __init__(self):
        self.auth_service = Auth_Service()
    
    async def login(self,request,url):
        return await self.auth_service.google_login_service(request,url)
    
    async def callback(self,request):
        return await self.auth_service.google_callback_service(request)