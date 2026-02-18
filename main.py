from fastapi import FastAPI
from routes import user_routes   # import your routes file

app = FastAPI()

# include router
app.include_router(user_routes.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="[IP_ADDRESS]", port=8000)