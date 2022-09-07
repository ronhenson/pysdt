from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def fastapi_hello_world():
    msg = "Welcome to PyBites' FastAPI Learning Path 🐍 🎉"
    return {"message": msg}
