import jwt
from datetime import datetime, timedelta, timezone
import os
from jwt import PyJWTError


def create_jwt_token(user_id, expires_delta: timedelta = timedelta(hours=1)) -> str:
    expire = datetime.now(tz=timezone.utc) + expires_delta
    payload = {"user_id": user_id, "exp": expire}
    encoded_jwt = jwt.encode(
        payload, os.environ["SECRET_KEY"], os.environ["ALGORITHM"])
    return encoded_jwt


def unsign_jwt_token(jwt_token) -> int:
    try:
        payload = jwt.decode(
            jwt_token, os.environ["SECRET_KEY"], os.environ["ALGORITHM"])
        return payload["user_id"]
    except PyJWTError as e:
        return 0
