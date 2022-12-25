import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth import authentication
from router import user, arrival_departure


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(arrival_departure.router)


if __name__ == "__main__":
    uvicorn.run(app)