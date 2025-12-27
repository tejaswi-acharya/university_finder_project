#learning END POINT PARAMETER
# there are 2 endpoint parameters: 1.path parameter 2. query parameter
from fastapi import FastAPI,HTTPException,Path

app = FastAPI()

students = {
    1: {"name":"Tejaswi","age":19,"class":"Bachelour's 2nd year"},
    2: {"name":"Swastika","age":19,"class":"12th Grade"}
}

#here we try to return the data of the students based on the id value

@app.get("/")
def home():
    return {"name":"First Data"}


# example: ...google.com/get-student/1= tejaswi's details on the basis of id, ....google.com/get-student/2=swastika's detail on the basis of id
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(...,description="The ID of the student you want to view", gt=0,lt=3)):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]
    
