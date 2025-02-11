from fastapi import FastAPI

from Services.Folder import router

app = FastAPI(
    title='Condor API',
    description='This is the API of the Condor project',
    version='0.5'
)
app.include_router(router)