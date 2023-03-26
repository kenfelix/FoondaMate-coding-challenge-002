from .oauth2 import verify_create_access_token
from fastapi import Depends, status, HTTPException
from fastapi.security import (
    OAuth2PasswordBearer,
)
from .crud import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = await verify_create_access_token(
        token=token, credentials_exception=credentials_exception
    )
    user = get_user_by_email(email=token_data.email)
    return user
