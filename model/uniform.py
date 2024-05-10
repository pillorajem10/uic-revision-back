# model/book.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db

UniformRouter = APIRouter(tags=["Uniform"])

# CRUD operations

@UniformRouter.get("/uniform/", response_model=list)
async def read_uniforms(
    db=Depends(get_db)
):
    query = "SELECT mngstore, uniformID, type, size, uniformQuantityAvailability, uniformPriceDetails FROM uniform"
    db[0].execute(query)
    uniforms = [{
        # "mngstore": uniform[0], 
        # "uniformID": uniform[1], 
        # "type": uniform[2], 
        # "size": uniform[3], 
        # "uniformQuantityAvailability": uniform[4], 
        # "uniformPriceDetails": uniform[5], 
        "id": uniform[1],
        "category": "uniform",
        "name": uniform[2],
        "price": uniform[5],
        "stock": uniform[4],
        "size": uniform[3],
        "image": "",
        "mngstore": uniform[0],
    } for uniform in db[0].fetchall()]
    return uniforms

@UniformRouter.get("/uniform/{uniform_id}", response_model=dict)
async def read_uniform_by_id(
    uniform_id: int, 
    db=Depends(get_db)
):
    query = "SELECT mngstore, uniformID, type, size, uniformQuantityAvailability, uniformPriceDetails FROM uniform WHERE uniformID = %s"
    db[0].execute(query, (uniform_id,))
    uniform = db[0].fetchone()
    if uniform:
        return {"mngstore": uniform[0], "uniformID": uniform[1], "type": uniform[2], "size": uniform[3], "uniformQuantityAvailability": uniform[4], "uniformPriceDetails": uniform[5]}
    raise HTTPException(status_code=404, detail="Uniform not found")

@UniformRouter.post("/uniform/", response_model=dict)
async def create_uniform(
    mngstore: str = Form(...),
    type: str = Form(...),
    size: str = Form(...),
    uniformQuantityAvailability: int = Form(...),
    uniformPriceDetails: int = Form(...),
    db=Depends(get_db)
):
    query = "INSERT INTO uniform (mngstore, type, size, uniformQuantityAvailability, uniformPriceDetails) VALUES (%s, %s, %s, %s, %s)"
    db[0].execute(query, (mngstore, type, size, uniformQuantityAvailability, uniformPriceDetails))
    db[1].commit()

    # Retrieve the last inserted ID using LAST_INSERT_ID()
    db[0].execute("SELECT LAST_INSERT_ID()")
    new_uniform_id = db[0].fetchone()[0]

    return {"uniformID": new_uniform_id, "mngstore": mngstore, "type": type, "size": size, "uniformQuantityAvailability": uniformQuantityAvailability, "uniformPriceDetails": uniformPriceDetails}

@UniformRouter.put("/uniform/{uniform_id}", response_model=dict)
async def update_uniform(
    uniform_id: int,
    mngstore: str = Form(...),
    type: str = Form(...),
    size: str = Form(...),
    uniformQuantityAvailability: int = Form(...),
    uniformPriceDetails: int = Form(...),
    db=Depends(get_db)
):
    query = "UPDATE uniform SET mngstore = %s, type = %s, size = %s, uniformQuantityAvailability = %s, uniformPriceDetails = %s WHERE uniformID = %s"
    db[0].execute(query, (mngstore, type, size, uniformQuantityAvailability, uniformPriceDetails, uniform_id))

    # Check if the update was successful
    if db[0].rowcount > 0:
        db[1].commit()
        return {"message": "Uniform updated successfully"}
    
    # If no rows were affected, uniform not found
    raise HTTPException(status_code=404, detail="Uniform not found")

@UniformRouter.delete("/uniform/{uniform_id}", response_model=dict)
async def delete_uniform(
    uniform_id: int,
    db=Depends(get_db)
):
    try:
        # Check if the uniform exists
        query_check_uniform = "SELECT uniformID FROM uniform WHERE uniformID = %s"
        db[0].execute(query_check_uniform, (uniform_id,))
        existing_uniform = db[0].fetchone()

        if not existing_uniform:
            raise HTTPException(status_code=404, detail="Uniform not found")

        # Delete the uniform
        query_delete_uniform = "DELETE FROM uniform WHERE uniformID = %s"
        db[0].execute(query_delete_uniform, (uniform_id,))
        db[1].commit()

        return {"message": "Uniform deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()
