class ProductService:
    def get_allProducts():
        return {
            "status_code": 200,
            "message": "success",
            "data": "all products!"
        }

    def getProduct():
        return {
            "status_code": 200,
            "message": "success",
            "data": "single product!"
        }
