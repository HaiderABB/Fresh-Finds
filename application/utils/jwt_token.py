import jwt
from datetime import datetime, timedelta, timezone
import os


def create_jwt_token(user_id, expires_delta: timedelta = timedelta(hours=1)) -> str:
    expire = datetime.now(tz=timezone.utc) + expires_delta
    payload = {"user_id": user_id, "exp": expire}
    encoded_jwt = jwt.encode(
        payload, os.environ["SECRET_KEY"], os.environ["ALGORITHM"])
    return encoded_jwt
