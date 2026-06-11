from mongoengine import StringField,Document,IntField,DateTimeField
from datetime import datetime,timezone

class User(Document):
    email=StringField(required=True,unique=True)
    access_token=StringField(required=True)
    refresh_token=StringField(required=True)
    expires_in=IntField(required=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))