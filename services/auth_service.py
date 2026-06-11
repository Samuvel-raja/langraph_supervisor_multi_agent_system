from authlib.integrations.starlette_client import OAuth, OAuthError
from config import settings
from fastapi import Request



class Auth_Service:
    def __init__(self):
        self.google_client_id=settings.google_client_id
        self.google_client_secret=settings.google_client_secret
        self.oauth = OAuth()
        self.oauth.register(
            name='google',
            server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
            client_id=settings.google_client_id,
            client_secret=self.google_client_secret,
            client_kwargs={
                'scope': 'email openid profile',
                'redirect_uri': 'http://localhost:8000/auth'
            }
        )

    async def google_login_service(self,request,url):
        return await self.oauth.google.authorize_redirect(request, url,access_type="offline", prompt="consent")
        

    async def google_callback_service(self,request):
        try:
            token = await self.oauth.google.authorize_access_token(request)
        except OAuthError as e:
            return {
                "message":e
            }
        user = token.get('userinfo')
        if user:
            request.session['user'] = dict(user)
        return {
            "user":token
        }
