from pydantic import BaseModel


class LoginForm(BaseModel):
    username: str
    password: str
class Token(BaseModel):
    access_token: str
    type_token: str


class Admin(BaseModel):
    username: str
    password: str