from fastapi import FastAPI, Header, Form

from login import user, api_test

app = FastAPI()

app.include_router(user.router)
app.include_router(api_test.router, prefix="/test")
