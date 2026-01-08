from fastapi import FastAPI,HTTPException,Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

students = {
    1: {"name":"Tejaswi","age":19,"year":"Bachelour's 2nd year"},
    2: {"name":"Swastika","age":19,"year":"12th Grade"}
}

class Student(BaseModel):
    name: str
    age: int
    year: str

@app.get("/")
def home():
    return {"name":"First Data"}



# @app.get("/get-student/{student_id}")
# def get_student(student_id: int = Path(...,description="The ID of the student you want to view", gt=0,lt=3)):
#     if student_id not in students:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return students[student_id]
    

# @app.get("/get-by-name/{student_id}") 
# def get_student_by_name(*,student_id: int, name: Optional[str]=None, test : int):   
#     for id in students:
#         if students[id]["name"]==name:
#             return students[id]
#     return {"Data":"Not Found!"}   
        

@app.post("/create-student/{student_id}")

def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error":"Student already exists"}
    
    students[student_id]= student
    return students[student_id]