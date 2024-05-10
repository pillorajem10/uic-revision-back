# model/reservationdetails.py
from fastapi import Depends, HTTPException, APIRouter, Form, Body
from .db import get_db
import json

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

ReservationdetailsRouter = APIRouter(tags=["Reservation Details"])

# CRUD operations
@ReservationdetailsRouter.post("/reservationdetails/{reservation_id}", response_model=list)
async def read_reservations_by_studentID(
    reservation_id: int,
    db=Depends(get_db)
):
    query = """
        SELECT 
            rd.reservationdetailsID, 
            rd.createDate, 
            rd.expiryDate, 
            rd.numofItems, 
            rd.totalAmount, 
            rd.studentID, 
            rd.items, 
            rd.status, 
            s.firstname, 
            s.lastname 
        FROM 
            reservationdetails rd 
            LEFT JOIN student s ON rd.studentID = s.studentID
        WHERE
            rd.studentID=%s
    """
    db[0].execute(query,(reservation_id,))
    reservations = [{
        # "reservationdetailsID": reservation[0], 
        # "createDate": reservation[1], 
        # "expiryDate": reservation[2], 
        # "numofItems": reservation[3], 
        # "totalAmount": reservation[4], 
        # "studentID": reservation[5], 
        # "items": reservation[6]

        "id": reservation[0],
        "items": reservation[6],
        "total": reservation[4],
        "date": reservation[1],
        "student": reservation[5],
        "studentName": reservation[8] + " " + reservation[9],
        "status": reservation[7]
    } for reservation in db[0].fetchall()]
    return reservations

@ReservationdetailsRouter.get("/reservationdetails/", response_model=list)
async def read_reservations(
    db=Depends(get_db)
):
    query = """
        SELECT 
            rd.reservationdetailsID, 
            rd.createDate, 
            rd.expiryDate, 
            rd.numofItems, 
            rd.totalAmount, 
            rd.studentID, 
            rd.items, 
            rd.status, 
            s.firstname, 
            s.lastname 
        FROM 
            reservationdetails rd 
            LEFT JOIN student s ON rd.studentID = s.studentID
    """
    db[0].execute(query)
    reservations = [{
        # "reservationdetailsID": reservation[0], 
        # "createDate": reservation[1], 
        # "expiryDate": reservation[2], 
        # "numofItems": reservation[3], 
        # "totalAmount": reservation[4], 
        # "studentID": reservation[5], 
        # "items": reservation[6]

        "id": reservation[0],
        "items": reservation[6],
        "total": reservation[4],
        "date": reservation[1],
        "student": reservation[5],
        "studentName": reservation[8] + " " + reservation[9],
        "status": reservation[7]
    } for reservation in db[0].fetchall()]
    return reservations

@ReservationdetailsRouter.get("/reservationdetails/{reservation_id}", response_model=dict)
async def read_reservation_by_id(
    reservation_id: int, 
    db=Depends(get_db)
):
    query = "SELECT reservationdetailsID, createDate, expiryDate, numofItems, totalAmount, studentID, items FROM reservationdetails WHERE reservationdetailsID = %s"
    db[0].execute(query, (reservation_id,))
    reservationdetails = db[0].fetchone()
    if reservationdetails:
        return {"reservationdetailsID": reservationdetails[0], "createDate": reservationdetails[1], "expiryDate": reservationdetails[2], "numofItems": reservationdetails[3], "totalAmount": reservationdetails[4], "studentID": reservationdetails[5], "items": reservationdetails[6]}
    raise HTTPException(status_code=404, detail="Reservation not found")



@ReservationdetailsRouter.post("/reservationdetails/", response_model=dict, responses={400: {"description": "Bad Request"}, 413: {"description": "Payload Too Large"}})
async def create_reservation(
    createDate: str = Form(...), 
    expiryDate: str = Form(...), 
    numofItems: int = Form(...),
    totalAmount: int = Form(...),
    studentID: int = Form(...),
    items: str = Form(...),  # expect a list of dictionary, each dictionary containing 'bookID' and 'quantity'
    db=Depends(get_db),
):
    items_str = json.dumps(items)
    items_list = json.loads(items)
    
    query = "INSERT INTO reservationdetails (createDate, expiryDate, numofItems, totalAmount, studentID, items) VALUES (%s, %s, %s, %s, %s, %s)"
    
    db[0].execute(query, (createDate, expiryDate, numofItems, totalAmount, studentID, items_str))
    db[1].commit()

    # Retrieve the last inserted ID using LAST_INSERT_ID()
    new_reservationdetails_id = db[0].lastrowid

    for item in items_list:
        if item['category'] == "uniform":
            item_id = item['id']
            quantity = item['stock']

            # Update the uniformQuantityAvailability field in your database
            update_query = "UPDATE uniform SET uniformQuantityAvailability = uniformQuantityAvailability - %s WHERE uniformID = %s"
            db[0].execute(update_query, (quantity, item_id))
            db[1].commit()
        else:
            item_id = item['id']
            quantity = item['stock']

            # Update the uniformQuantityAvailability field in your database
            update_query = "UPDATE book SET bookquantityAvailability = bookquantityAvailability - %s WHERE bookID = %s"
            db[0].execute(update_query, (quantity, item_id))
            db[1].commit()

    return {
        "reservationdetailsID": new_reservationdetails_id,
        "createDate": createDate,
        "expiryDate": expiryDate,
        "numofItems": numofItems,
        "totalAmount": totalAmount,
        "studentID": studentID,
        "items": items
    }
@ReservationdetailsRouter.put("/reservationdetails/{reservationdetailsID}", response_model=dict)
async def update_reservation(
    reservationdetailsID: int,
    createDate: str = Form(...), 
    expiryDate: str = Form(...), 
    numofItems: int = Form(...),
    totalAmount: int = Form(...),
    studentID: int = Form(...),
    items: str = Form(...),
    db=Depends(get_db)
):
    query = "UPDATE reservationdetails SET createDate = %s, expiryDate = %s, numofItems = %s, totalAmount = %s, studentID = %s, items = %s WHERE reservationdetailsID = %s"
    items_str = json.dumps(items)
    db[0].execute(query, (createDate, expiryDate, numofItems, totalAmount, studentID, items_str, reservationdetailsID))

    # Check if the update was successful
    if db[0].rowcount > 0:
        db[1].commit()
        return {"message": "Reservation details updated successfully"}
    
    # If no rows were affected, reservation details not found
    raise HTTPException(status_code=404, detail="Reservation details not found")
@ReservationdetailsRouter.put("/reservationdetails/status/{reservationdetailsID}", response_model=dict)
async def set_reservation_status(
    reservationdetailsID: int,
    status: str = Form(...), 
    db=Depends(get_db)
):
    query = "UPDATE reservationdetails SET status = %s WHERE reservationdetailsID = %s"
    db[0].execute(query, (status, reservationdetailsID))

    # Check if the update was successful
    if db[0].rowcount > 0:
        db[1].commit()
        return {"message": "Reservation status updated successfully"}
    
    # If no rows were affected, reservation details not found
    raise HTTPException(status_code=404, detail="Reservation details not found")

@ReservationdetailsRouter.put("/reservationdetails/items/{reservationdetailsID}", response_model=dict)
async def set_items(
    reservationdetailsID: int,
    items: str = Form(...), 
    totalAmount: int = Form(...),
    db=Depends(get_db)
):
    
    items_str = json.dumps(items)
    logger.info("ITEMS STRINGGGGGGGGGGG", items_str)
    # logger.info("ITEMS OBEJCTTTTTTTTTTTTT", items)
    query = "UPDATE reservationdetails SET items = %s, totalAmount = %s WHERE reservationdetailsID = %s"
    db[0].execute(query, (items_str, totalAmount, reservationdetailsID))

    # Check if the update was successful
    if db[0].rowcount > 0:
        db[1].commit()
        return {"message": "Reservation items updated successfully"}
    
    # If no rows were affected, reservation details not found
    raise HTTPException(status_code=404, detail="Reservation details not found")

@ReservationdetailsRouter.delete("/reservationdetails/{reservationdetailsID}", response_model=dict)
async def delete_reservation(
    reservationdetailsID: int,
    db=Depends(get_db)
):
    try:
        # Check if the reservation details exist
        query_check_reservation = "SELECT reservationdetailsID FROM reservationdetails WHERE reservationdetailsID = %s"
        db[0].execute(query_check_reservation, (reservationdetailsID,))
        existing_reservation = db[0].fetchone()

        if not existing_reservation:
            raise HTTPException(status_code=404, detail="Reservation details not found")

        # Delete the reservation details
        query_delete_reservation = "DELETE FROM reservationdetails WHERE reservationdetailsID = %s"
        db[0].execute(query_delete_reservation, (reservationdetailsID,))
        db[1].commit()

        return {"success": True, "message": "Reservation details deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()