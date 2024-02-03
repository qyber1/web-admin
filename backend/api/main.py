from fastapi.templating import Jinja2Templates


def get_template():
    templates = Jinja2Templates(directory='frontend/templates')
    return templates