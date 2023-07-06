from datetime import datetime

from fastapi import FastAPI


from os import environ

from models.database import database
from routers import sbom, users,debinstall,grype,servers



now = datetime.now()

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(users.router)

app.include_router(debinstall.router)

app.include_router(sbom.router)

app.include_router(grype.router)

app.include_router(servers.router)