from typing import Annotated, Union

from fastapi import APIRouter, Request,  Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.responses import RedirectResponse

from sqlalchemy.ext.asyncio import AsyncSession

from backend.utils.auth.hasher import Hasher
from backend.utils.auth.token import create_jwt_token, verify_jwt_token
from backend.utils.db.connection import get_session
from backend.utils.db.query import _get_current_user
from backend.utils.models.models import Admin
from .main import TemplateResponse_


auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')


@auth_router.get('/login')
async def get_login_form(request: Request) -> TemplateResponse_:
    return TemplateResponse_(
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
        return TemplateResponse_(
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
        return TemplateResponse_(
            'login.html',
            {
                'request': request,
                'error_message': 'Неверные данные для входа, проверьте правильность и повторите попытку'
            }
        )


@auth_router.get("/logout")
async def logout(request: Request) -> TemplateResponse_:
    print(request.cookies)
    response =TemplateResponse_("login.html", {
        'request': request
    })
    response.set_cookie(key="token", value="", expires='2020-01-01 00:00:00.0')
    return response


async def get_current_user(request: Request,  session: AsyncSession = Depends(get_session)) -> RedirectResponse| Admin:
    token = request.cookies.get('token')
    print('cookie - ', token)
    if not token:
        raise HTTPException(status_code=303, detail='Redirect to /auth/login', headers={"Location": "/auth/login"})
    data = verify_jwt_token(token)
    if data:
        user = await _get_current_user(session, data.get('sub'))
    else:
        raise HTTPException(status_code=401, detail='Not authorization')
    if not user:
        raise HTTPException(status_code=401,  detail='Not user')

    return user


