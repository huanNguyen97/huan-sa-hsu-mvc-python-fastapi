# import from python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# import from owner
from routers.router import router

app = FastAPI()

templates = Jinja2Templates(directory="./elements/views")

app.include_router(router)
