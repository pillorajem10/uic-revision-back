# model/reservation.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db

ReservationRouter = APIRouter(tags=["Reservation"])

# CRUD operations

@ReservationRouter.get("/reservation/", response_model=list)
async def read_reservations(
    db=Depends(get_db)
):
    query = "SELECT reservationdetailsID FROM reservation"
    db[0].execute(query)
    reservations = [{"reservationdetailsID": reservation[0]} for reservation in db[0].fetchall()]
    return reservations

@ReservationRouter.get("/reservation/{reservation_id}", response_model=dict)
async def read_reservation_by_id(
    reservation_id: int, 
    db=Depends(get_db)
):
    query = "SELECT reservationdetailsID FROM reservation WHERE reservationdetailsID = %s"
    db[0].execute(query, (reservation_id,))
    reservation = db[0].fetchone()
    if reservation:
        return {"reservationdetailsID": reservation[0]}
    raise HTTPException(status_code=404, detail="Reservation not found")

@ReservationRouter.post("/reservation/", response_model=dict)
async def create_reservation(
    reservationdetails_id: int = Form(...), 
    db=Depends(get_db)
):
    query = "INSERT INTO reservation (reservationdetailsID) VALUES (%s)"
    db[0].execute(query, (reservationdetails_id,))
    db[1].commit()

    # Retrieve the last inserted ID using LAST_INSERT_ID()
    db[0].execute("SELECT LAST_INSERT_ID()")
    new_reservation_id = db[0].fetchone()[0]

    return {
        "reservationdetailsID": new_reservation_id
    }

@ReservationRouter.put("/reservation/{reservation_id}", response_model=dict)
async def update_reservation(
    reservation_id: int,
    reservationdetails_id: int = Form(...), 
    db=Depends(get_db)
):
    query = "UPDATE reservation SET reservationdetailsID = %s WHERE reservationdetailsID = %s"
    db[0].execute(query, (reservationdetails_id, reservation_id))

    # Check if the update was successful
    if db[0].rowcount > 0:
        db[1].commit()
        return {"message": "Reservation updated successfully"}
    
    # If no rows were affected, reservation not found
    raise HTTPException(status_code=404, detail="Reservation not found")

@ReservationRouter.delete("/reservation/{reservation_id}", response_model=dict)
async def delete_reservation(
    reservation_id: int,
    db=Depends(get_db)
):
    try:
        # Check if the reservation exists
        query_check_reservation = "SELECT reservationdetailsID FROM reservation WHERE reservationdetailsID = %s"
        db[0].execute(query_check_reservation, (reservation_id,))
        existing_reservation = db[0].fetchone()

        if not existing_reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")

        # Delete the reservation
        query_delete_reservation = "DELETE FROM reservation WHERE reservationdetailsID = %s"
        db[0].execute(query_delete_reservation, (reservation_id,))
        db[1].commit()

        return {"message": "Reservation deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()
