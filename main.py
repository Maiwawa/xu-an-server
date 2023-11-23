import uvicorn
from fastapi import FastAPI

app = FastAPI()

# your app code here
@app.get("/")
def home():
    return {"Data":"Test"}

@app.get("/ConnectCheck")
def home():
    return {"Connect":"Success"}

if __name__ == "__main__":
    uvicorn.run(app, port=8080)