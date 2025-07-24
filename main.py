from fastapi import FastAPI
from pydantic import BaseModel
from starlette.config import undefined
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/hello")
def read_hello():

  return JSONResponse({"message": "Hello world"}, status_code=200)

class WelcomeRequest(BaseModel):
    name: str

@app.get("/welcome")
def welcome_user(request: WelcomeRequest):
        return JSONResponse(f"Bienvenue {request.name}", status_code=200)

student_memo = []
class Student (BaseModel):
    reference : str
    name: str
    firstname :str
    lastname: str
    age : int


@app.post("/Studend")

def add_student ( new_student : list[Student]):
    for new_student in new_student:
        if  any (s.reference == new_student.reference for s in student_memo)
            continue
            student_memo.append (new_student)

    return JSONResponse(f"CREATED{student_memo}", status_code=201)



@app.get("/Studend")
def get_student ():
 return JSONResponse(f"CREATED{student_memo}", status_code=200)



@app.put("/Studend")
def reference_student ( ref_student = list[Student.reference] ):
    for ref_student in ref_student:
        if  any (s.reference == new_student.reference for s in student_memo)






