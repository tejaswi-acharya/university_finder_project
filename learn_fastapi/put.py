#put means to update/replace something that already exists

from fastapi import FastAPI,HTTPException,Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

students = {
    1: {"name":"Tejaswi","age":19,"year":"Bachelour's 2nd year"},
    2: {"name":"Swastika","age":19,"year":"12th Grade"}
}

#class for post method
class Student(BaseModel):
    name: str
    age: int
    year: str

#class for put method(if same class used then its compulsary to fill for name,age,year)
class UpdateStudent(BaseModel):
    name: Optional[str]= None
    age: Optional[int]= None
    year: Optional[str]= None

@app.get("/")
def home():
    return {"name":"First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(...,description="The ID of the student you want to view", gt=0,lt=3)):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]


@app.post("/create-student/{student_id}")

def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error":"Student already exists"}
    
    students[student_id]= student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student:UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist!"}
    
    if student.name != None:
        students[student_id]["name"] = student.name
    if student.age != None:
        students[student_id]["age"] = student.age
    if student.year != None:
        students[student_id]["year"] = student.year
    
    return students[student_id]


