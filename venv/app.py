from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

from application.routes import productRoutes, userRoute


description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""


tags_metadata = [
    {
        "name": "Users",
        "description": "this is the user api requests..",
    },
    {
        "name": "Product",
        "description": "this is the product api requests..",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(
    title="E-Commerce",
    description=description,
    version=2.0,
    openapi_tags=tags_metadata,
    openapi_url='/ksoftEcommerce.json',
    docs_url='/docs',
    contact={
        "name": "Ashok Sahu",
        "url": "https://ashok-sahu.netlify.app/",
        "email": "ashoksahu1105@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
)

# !mount in the browser
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def getHome(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.get("/about", response_class=HTMLResponse)
async def getAbout(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
@app.get("/contact", response_class=HTMLResponse)
async def getContact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})


app.include_router(productRoutes.router)
app.include_router(userRoute.router)


# custom port and setup..
if __name__ == '__main__':
    uvicorn.run(app="app:app", port=1000, reload=True, workers=1)
