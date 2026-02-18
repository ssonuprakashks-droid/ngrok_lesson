from fastapi import FastAPI
from routes import user_routes  
from db import engine, Base
from models import User
 
Base.metadata.create_all(bind=engine)

app = FastAPI()

# include router
app.include_router(user_routes.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)