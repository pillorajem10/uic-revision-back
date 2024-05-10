# model/admin.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db

AdminRouter = APIRouter(tags=["Admin"])

# CRUD operations

@AdminRouter.get("/admin/", response_model=list)
async def read_admins(
    db=Depends(get_db)
):
    query = "SELECT mngstore, adminID, username, password FROM admin"
    db[0].execute(query)
    admins = [{"mngstore": admin[0], "adminID": admin[1], "username": admin[2], "password": admin[3]} for admin in db[0].fetchall()]
    return admins

@AdminRouter.get("/admin/{admin_id}", response_model=dict)
async def read_admin_by_id(
    admin_id: str, 
    db=Depends(get_db)
):
    query = "SELECT mngstore, adminID, username, password FROM admin WHERE adminID = %s"
    db[0].execute(query, (admin_id,))
    admin = db[0].fetchone()
    if admin:
        return {"mngstore": admin[0], "adminID": admin[1], "username": admin[2], "password": admin[3]}
    raise HTTPException(status_code=404, detail="Admin not found")

@AdminRouter.post("/admin/", response_model=dict)
async def create_admin(
    mngstore: str = Form(...),
    adminID: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    db=Depends(get_db)
):
    query = "INSERT INTO admin (mngstore, adminID, username, password) VALUES (%s, %s, %s, %s)"
    db[0].execute(query, (mngstore, adminID, username, password))
    db[1].commit()

    # Retrieve the last inserted ID using LAST_INSERT_ID()
    db[0].execute("SELECT LAST_INSERT_ID()")
    new_admin_id = db[0].fetchone()[0]

    return {"adminID": new_admin_id, "mngstore": mngstore, "adminID": adminID, "username": username, "password": password}

@AdminRouter.post("/admin/login", response_model=dict)
async def login_admin(
    username: str = Form(...),
    password: str = Form(...),
    db=Depends(get_db)
):
    query = "SELECT mngstore, adminID, username, password FROM admin WHERE username = %s AND password = %s"
    db[0].execute(query, (username, password))
    admin = db[0].fetchone()

    if not admin:
        return {"message": "Invalid username or password"}
    
    return {"adminID": admin[1], "mngstore": admin[0], "username": admin[2]}

@AdminRouter.put("/admin/{admin_id}", response_model=dict)
async def update_admin(
    admin_id: str,
    mngstore: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    db=Depends(get_db)
):
    query = "UPDATE admin SET mngstore = %s, username = %s, password = %s WHERE adminID = %s"
    db[0].execute(query, (mngstore, username, password, admin_id))

    # Check if the update was successful
    if db[0].rowcount > 0:
        db[1].commit()
        return {"message": "Admin updated successfully"}
    
    # If no rows were affected, admin not found
    raise HTTPException(status_code=404, detail="Admin not found")

@AdminRouter.delete("/admin/{admin_id}", response_model=dict)
async def delete_admin(
    admin_id: str,
    db=Depends(get_db)
):
    try:
        # Check if the admin exists
        query_check_admin = "SELECT adminID FROM admin WHERE adminID = %s"
        db[0].execute(query_check_admin, (admin_id,))
        existing_admin = db[0].fetchone()

        if not existing_admin:
            raise HTTPException(status_code=404, detail="Admin not found")

        # Delete the admin
        query_delete_admin = "DELETE FROM admin WHERE adminID = %s"
        db[0].execute(query_delete_admin, (admin_id,))
        db[1].commit()

        return {"message": "Admin deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()
