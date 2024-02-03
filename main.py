from fastapi import FastAPI

from backend.api import root_router


def main():
    app = FastAPI(title='admin-panel')
    app.include_router(root_router)
    return app


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=main())
