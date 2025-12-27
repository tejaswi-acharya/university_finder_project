#query parameter
#it is used to pass query to the url and is similar to path parameter

#example: google.com/results?search=Python

from fastapi import FastAPI,HTTPException,Path
from typing import Optional

app = FastAPI()

students = {
    1: {"name":"Tejaswi","age":19,"class":"Bachelour's 2nd year"},
    2: {"name":"Swastika","age":19,"class":"12th Grade"}
}


@app.get("/")
def home():
    return {"name":"First Data"}



@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(...,description="The ID of the student you want to view", gt=0,lt=3)):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]
    
#Note: in path parameter we added the {student_id} as endpoint in the url,but incase of query you don't need to
#Note 2: you cannot have an optional argument before a required argument in python
#Note 3: the "*"  helps to prevent the syntax error here 
@app.get("/get-by-name")
def get_student(*, name: Optional[str]=None, test : int):   #two query parameter 1 as name another as test in integer value
    for id in students:
        if students[id]["name"]==name:
            return students[id]
    return {"Data":"Not Found!"}   
        
    