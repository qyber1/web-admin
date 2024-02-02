from typing import Annotated, Union
from fastapi import APIRouter, Request,  Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from backend.utils.auth.hasher import Hasher
from backend.utils.auth.token import create_jwt_token, verify_jwt_token
from backend.utils.db.connection import get_session
from backend.utils.db.query import _get_current_user
from backend.utils.models.models import Admin

auth_router = APIRouter(prefix='/auth')
templates = Jinja2Templates(directory='frontend/templates')
TemplateResponse_ = templates.TemplateResponse
SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')


@auth_router.get('/login')
async def get_login_form(request: Request) -> TemplateResponse_:
    return templates.TemplateResponse(
        'login.html',
        {
        'request': request
        }
    )


@auth_router.post('/login', response_model=None)
async def auth(request: Request,
               form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
               session: AsyncSession = Depends(get_session)) -> Union[RedirectResponse, dict]:
    user = await _get_current_user(session, form_data.username)
    if not user:
        return templates.TemplateResponse(
            'login.html',
            {
                'request': request,
                'error_message': 'Неверные данные для входа, проверьте правильность и повторите попытку'
            }
        )
    if Hasher.verify_password(form_data.password, user[1]):
        jwt_token = create_jwt_token(data={'sub': user[0]})
        response = RedirectResponse('/index', status_code=303)
        response.set_cookie(key='token', value=jwt_token)
        return response
    else:
        return templates.TemplateResponse(
            'login.html',
            {
                'request': request,
                'error_message': 'Неверные данные для входа, проверьте правильность и повторите попытку'
            }
        )


async def get_current_user(request: Request, session: AsyncSession = Depends(get_session)) -> Admin:
    token = request.cookies.get('token')
    if not token:
        raise HTTPException(status_code=401, detail='Not token')
    data = verify_jwt_token(token)
    if data:
        user = await _get_current_user(session, data.get('sub'))
    else:
        raise HTTPException(status_code=401, detail='Not authorization')
    if not user:
        raise HTTPException(status_code=401,  detail='Not user')

    return user


