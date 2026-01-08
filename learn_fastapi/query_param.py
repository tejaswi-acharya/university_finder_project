# query parameter
# it is used to pass query to the url and is similar to path parameter
#
# example: google.com/results?search=Python

from fastapi import FastAPI, HTTPException, Path
from typing import Optional

app = FastAPI()

students = {
    1: {"name": "Tejaswi", "age": 19, "class": "Bachelor's 2nd year"},
    2: {"name": "Swastika", "age": 19, "class": "12th Grade"}
}


@app.get("/")
def home():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(
    student_id: int = Path(
        ...,
        description="The ID of the student you want to view",
        gt=0,
        lt=3
    )
):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]


# Note:
# In path parameters we add {student_id} in the URL.
# In query parameters, we do NOT add anything in the URL path.
#
# Note 2:
# You cannot have an optional argument before a required argument in Python.
#
# Note 3:
# The "*" makes all parameters keyword-only and helps prevent syntax errors.
#
# This endpoint COMBINES:
# - Path parameter (student_id)
# - Query parameters (name, test)

@app.get("/get-by-name/{student_id}")
def get_student_by_name(
    *,
    student_id: int,
    name: Optional[str] = None,
    test: Optional[int] = None
):
    if student_id not in students:
        return {"Data": "Student ID not found"}

    student = students[student_id]

    # If name is provided, check if it matches
    if name and student["name"] != name:
        return {"Data": "Name not found"}

    return student
