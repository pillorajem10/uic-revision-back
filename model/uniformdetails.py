# model/uniformdetails.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db

UniformdetailsRouter = APIRouter(tags=["Uniform Details"])

# CRUD operations

@UniformdetailsRouter.get("/Uniformdetails/", response_model=list)
async def read_uniforms(
    db=Depends(get_db)
):
    query = "SELECT uniformreservationID, reservationdetailsID, uniformID, uniformQuantity FROM uniformdetails"
    db[0].execute(query)
    uniforms = [{"uniformreservationID": details[0], "reservationdetailsID": details[1], "uniformID": details[2], "uniformQuantity": details[3]} for details in db[0].fetchall()]
    return uniforms

@UniformdetailsRouter.get("/Uniformdetails/{uniform_id}", response_model=dict)
async def read_uniform_by_id(
    uniform_id: int, 
    db=Depends(get_db)
):
    query = "SELECT uniformreservationID, reservationdetailsID, uniformID, uniformQuantity FROM uniformdetails WHERE uniformID = %s"
    db[0].execute(query, (uniform_id,))
    uniform_details = db[0].fetchone()
    if uniform_details:
        return {"uniformreservationID": uniform_details[0], "reservationdetailsID": uniform_details[1], "uniformID": uniform_details[2], "uniformQuantity": uniform_details[3]}
    raise HTTPException(status_code=404, detail="Uniform not found")

@UniformdetailsRouter.post("/Uniformdetails/", response_model=dict)
async def create_uniform(
    uniformreservationID: int = Form(...),
    reservationdetailsID: int = Form(...),
    uniformID: int = Form(...),
    uniformQuantity: int = Form(...),
    db=Depends(get_db)
):
    query = "INSERT INTO uniformdetails (uniformreservationID, reservationdetailsID, uniformID, uniformQuantity) VALUES (%s, %s, %s, %s)"
    db[0].execute(query, (uniformreservationID, reservationdetailsID, uniformID, uniformQuantity))
    db[1].commit()

    # Retrieve the last inserted ID using LAST_INSERT_ID()
    db[0].execute("SELECT LAST_INSERT_ID()")
    new_uniform_id = db[0].fetchone()[0]

    return {"uniformID": new_uniform_id, "uniformreservationID": uniformreservationID, "reservationdetailsID": reservationdetailsID, "uniformID": uniformID, "uniformQuantity": uniformQuantity}

@UniformdetailsRouter.put("/Uniformdetails/{uniform_id}", response_model=dict)
async def update_uniform(
    uniform_id: int,
    uniformreservationID: int = Form(...),
    reservationdetailsID: int = Form(...),
    uniformID: int = Form(...),
    uniformQuantity: int = Form(...),
    db=Depends(get_db)
):
    query = "UPDATE uniformdetails SET uniformreservationID = %s, reservationdetailsID = %s, uniformID = %s, uniformQuantity = %s WHERE uniformID = %s"
    db[0].execute(query, (uniformreservationID, reservationdetailsID, uniformID, uniformQuantity, uniform_id))

    # Check if the update was successful
    if db[0].rowcount > 0:
        db[1].commit()
        return {"message": "Uniform updated successfully"}
    
    # If no rows were affected, uniform not found
    raise HTTPException(status_code=404, detail="Uniform not found")

@UniformdetailsRouter.delete("/Uniformdetails/{uniform_id}", response_model=dict)
async def delete_uniform(
    uniform_id: int,
    db=Depends(get_db)
):
    try:
        # Check if the uniform exists
        query_check_uniform = "SELECT uniformID FROM uniformdetails WHERE uniformID = %s"
        db[0].execute(query_check_uniform, (uniform_id,))
        existing_uniform = db[0].fetchone()

        if not existing_uniform:
            raise HTTPException(status_code=404, detail="Uniform not found")

        # Delete the uniform
        query_delete_uniform = "DELETE FROM uniformdetails WHERE uniformID = %s"
        db[0].execute(query_delete_uniform, (uniform_id,))
        db[1].commit()

        return {"message": "Uniform deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()
