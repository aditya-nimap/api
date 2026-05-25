from fastapi import FastAPI
from api.v1.router import api_router

app = FastAPI(
    title="Creator AI API",
    description="WhatsApp Creator Bot Backend APIs",        
    version="1.0.0",
)


@app.get("/")
async def health_check():
    return {"message": "Creator AI API is running!"}    


app.include_router(
   api_router,
)
