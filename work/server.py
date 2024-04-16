import uvicorn

from fastapi import FastAPI

from schemas import Tee
# "models" for ORM

api = FastAPI()

teee = []

@api.get("/")
async def list_cats():
    return teee

@api.put("/add")
async def add_cat(tee: Tee):
    teee.append(tee)

if __name__ == '__main__':
    uvicorn.run('server:api', reload=True)
    # API