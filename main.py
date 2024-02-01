import uvicorn
from fastapi import FastAPI

from backend.api import auth_router, index_router


def main():
    app = FastAPI(title='admin-panel')
    app.include_router(auth_router)
    app.include_router(index_router)
    return app


if __name__ == '__main__':
    uvicorn.run(app=main())
