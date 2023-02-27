from fastapi import FastAPI
import uvicorn

# from app.routes import productRoutes, userRoute
from application.routes import productRoutes, userRoute

app = FastAPI()


@app.get('/')
async def getData():
    return {
        "status": 200,
        "data": "this is data from hello world wdnbj"
    }

app.include_router(productRoutes.router)
app.include_router(userRoute.router)
# custom port and setup..
if __name__ == '__main__':
    uvicorn.run(app="app:app", port=1000, reload=True, workers=1)
