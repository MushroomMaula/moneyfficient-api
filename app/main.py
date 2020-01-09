from fastapi import FastAPI, Security
from app.api import auth, user, expense
from app.frontend import frontend_server

app = FastAPI()

app.mount('/', frontend_server)

app.include_router(
    auth.router,
    prefix='/auth',
    tags=["auth"]
)


app.include_router(
    user.router,
    prefix='/user',
    tags=["users"]
)

app.include_router(
    expense.router,
    prefix='/expenses',
    tags=["expenses"]
)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
