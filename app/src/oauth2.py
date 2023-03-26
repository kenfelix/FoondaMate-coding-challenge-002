from jose import JWTError, jwt

from datetime import datetime, timedelta

from pydantic import ValidationError

from .models import TokenData
from .config import settings


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict):
    new_data = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    new_data.update({"exp": expire})
    encoded_jwt = jwt.encode(new_data, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


async def verify_create_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except (JWTError, ValidationError):
        raise credentials_exception
    return token_data