from passlib.context import CryptContext

pswrd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashpassword(password: str):
    return pswrd_context.hash(password)


def verify(plain_password, hashed_password):
    return pswrd_context.verify(plain_password, hashed_password)
