from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.API import auth

app = FastAPI()

app.include_router(auth.router, prefix="/api", tags=["staticTable"])
# app.include_router(imports.router, prefix="/api", tags=["Imports"])
# app.include_router(calcul.router, prefix="/api", tags=["Calcul"])

origin = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("__main__:app", host="localhost", port=8000, reload=True)
