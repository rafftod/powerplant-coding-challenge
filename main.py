from fastapi import FastAPI
import uvicorn

app = FastAPI()


# placeholder to assess the API is working
@app.get("/")
def read_root():
    return {"Hello": "World"}


# production plan endpoint
@app.post("/productionplan")
def production_plan():
    return {"Production": "Plan"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8888, reload=True, log_level="info")
