from .calc import solve_linear_equation
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .oauth2 import create_access_token
from .utils import verify
from .dependecies import get_current_user

from .crud import get_user_by_email, create_user
from .models import Token, User

auth = APIRouter(tags=["Authentication"])
cal = APIRouter(tags=["Caculatetion"])


@auth.post("/login", response_model=Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
):
    userIndb = get_user_by_email(email=user_credentials.username)
    user: User = User(**userIndb)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )
    if not verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(data={"email": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@auth.post("/user", status_code=status.HTTP_201_CREATED, response_model=User)
async def createUser(user: User):
    userIndb = get_user_by_email(email=user.email)
    if userIndb:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Email already registered"
        )
    new_user_Indb = create_user(user=user)
    return new_user_Indb


@cal.post("/calculate")
async def solveEquation(
    equation: str,
    current_active_user: User = Depends(get_current_user),
):
    try:
        solution = solve_linear_equation(equation=equation)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="invalid equation format",
        )
    return solution


# def serializeDict(document) -> dict:
#     return {
#         **{i: str(document[i]) for i in document if i == "_id"},
#         **{i: document[i] for i in document if i != "_id"},
#     }
