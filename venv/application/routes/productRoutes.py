from fastapi import APIRouter
from application.controllers.productController import ProductService

router = APIRouter(prefix="/products", tags=["Product"])


# !http://localhost:5000/products
@router.get('/')
async def getAllProducts():
    return ProductService.get_allProducts()


# !http://localhost:5000/products/product
@router.get('/product')
async def getSingleProduct():
    return ProductService.getProduct()


