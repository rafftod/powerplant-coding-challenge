from fastapi import FastAPI
from validation import ProblemPayload
from solve import solve
import uvicorn

app = FastAPI()


# placeholder to assess the API is working
@app.get("/")
def read_root():
    return {"Hello": "World"}


# production plan endpoint
@app.post("/productionplan")
def production_plan(production_payload: ProblemPayload):
    return solve(production_payload.dict())


if __name__ == "__main__":
    uvicorn.run("main:app", port=8888, reload=True, log_level="info")
