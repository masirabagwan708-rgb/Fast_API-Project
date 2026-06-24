
from pymongo import MongoClient

app = FastAPI()



conn = MongoClient(
    "mongodb+srv://Masira_db:Masira%400103@cluster0.9awrm4l.mongodb.net/")



# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     return templates.TemplateResponse(
#         name="index.html",
#         context={"request": request}
#     )


# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/")
# def home():
#     return {"message": "Hello, FastAPI!"}