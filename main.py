from fastapi import FastAPI, Header, Form

from login import user, api_test

app = FastAPI()

app.include_router(user.router, prefix="/v1")
app.include_router(api_test.router, prefix="/v0")
