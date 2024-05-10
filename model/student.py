# model/student.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db

StudentRouter = APIRouter(tags=["Student"])

# CRUD operations

@StudentRouter.get("/student/", response_model=list)
async def read_students(
    db=Depends(get_db)
):
    query = "SELECT studentID, firstName, lastName, uicEmail, password FROM student"
    db[0].execute(query)
    students = [{"studentID": student[0], "firstName": student[1], "lastName": student[2], "uicEmail": student[3], "password": student[4]} for student in db[0].fetchall()]
    return students

@StudentRouter.get("/student/{student_id}", response_model=dict)
async def read_student(
    student_id: int, 
    db=Depends(get_db)
):
    query = "SELECT studentID, firstName, lastName, uicEmail, password FROM student WHERE studentID = %s"
    db[0].execute(query, (student_id,))
    student = db[0].fetchone()
    if student:
        return {"studentID": student[0], "firstName": student[1], "lastName": student[2], "uicEmail": student[3], "password": student[4]}
    raise HTTPException(status_code=404, detail="Student not found")

@StudentRouter.post("/student/login", response_model=dict)
async def login_student(
    uicEmail: str = Form(...),
    password: str = Form(...),
    db=Depends(get_db)
):
    query = "SELECT studentID, firstName, lastName, uicEmail, password FROM student WHERE uicEmail = %s AND password = %s"
    db[0].execute(query, (uicEmail, password))
    student = db[0].fetchone()
    if student:
        return {"studentID": student[0], "firstName": student[1], "lastName": student[2], "uicEmail": student[3], "password": student[4]}
    else:
        raise HTTPException(status_code=401, detail="Incorrect email or password")

@StudentRouter.post("/student/", response_model=dict)
async def create_student(
    firstName: str = Form(...),
    lastName: str = Form(...),
    uicEmail: str = Form(...),
    password: str = Form(...),
    db=Depends(get_db)
):
    query = "INSERT INTO student (firstName, lastName, uicEmail, password) VALUES (%s, %s, %s, %s)"
    db[0].execute(query, (firstName, lastName, uicEmail, password))
    db[1].commit()

    # Retrieve the last inserted ID using LAST_INSERT_ID()
    db[0].execute("SELECT LAST_INSERT_ID()")
    new_student_id = db[0].fetchone()[0]

    return {"studentID": new_student_id, "firstName": firstName, "lastName": lastName, "uicEmail": uicEmail, "password": password}

@StudentRouter.put("/student/{student_id}", response_model=dict)
async def update_student(
    student_id: int,
    firstName: str = Form(...),
    lastName: str = Form(...),
    uicEmail: str = Form(...),
    password: str = Form(...),
    db=Depends(get_db)
):
    query = "UPDATE student SET firstName = %s, lastName = %s, uicEmail = %s, password = %s WHERE studentID = %s"
    db[0].execute(query, (firstName, lastName, uicEmail, password, student_id))

    # Check if the update was successful
    if db[0].rowcount > 0:
        db[1].commit()
        return {"message": "Student updated successfully"}
    
    # If no rows were affected, student not found
    raise HTTPException(status_code=404, detail="Student not found")

@StudentRouter.delete("/student/{student_id}", response_model=dict)
async def delete_student(
    student_id: int,
    db=Depends(get_db)
):
    try:
        # Check if the student exists
        query_check_student = "SELECT studentID FROM student WHERE studentID = %s"
        db[0].execute(query_check_student, (student_id,))
        existing_student = db[0].fetchone()

        if not existing_student:
            raise HTTPException(status_code=404, detail="Student not found")

        # Delete the student
        query_delete_student = "DELETE FROM student WHERE studentID = %s"
        db[0].execute(query_delete_student, (student_id,))
        db[1].commit()

        return {"message": "Student deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()