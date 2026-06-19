from mongoengine import connect
from mongoengine.connection import get_connection
from config import settings


def connect_db():
    try:
        connect(
            host=settings.mongo_uri,
            db=settings.mongo_db_name
        )
        get_connection().admin.command("ping")
        print("MONGODB CONNECTED SUCCESSFULLY")
    except Exception as e:
        raise f"MONGODB FAILED TO CONNECT : {e}" from e
 