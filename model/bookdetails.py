# model/bookdetails.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db

BookdetailsRouter = APIRouter(tags=["Book Details"])

# CRUD operations

@BookdetailsRouter.get("/bookdetails/", response_model=list)
async def read_books(
    db=Depends(get_db)
):
    query = "SELECT bookreservationID, reservationdetailsID, bookID, bookQuantity FROM bookdetails"
    db[0].execute(query)
    books = [{"bookreservationID": details[0], "reservationdetailsID": details[1], "bookID": details[2], "bookQuantity": details[3]} for details in db[0].fetchall()]
    return books

@BookdetailsRouter.get("/bookdetails/{book_id}", response_model=dict)
async def read_book_by_id(
    book_id: int, 
    db=Depends(get_db)
):
    query = "SELECT bookreservationID, reservationdetailsID, bookID, bookQuantity FROM bookdetails WHERE bookID = %s"
    db[0].execute(query, (book_id,))
    bookdetails = db[0].fetchone()
    if bookdetails:
        return {"bookreservationID": bookdetails[0], "reservationdetailsID": bookdetails[1], "bookID": bookdetails[2], "bookQuantity": bookdetails[3]}
    raise HTTPException(status_code=404, detail="Book not found")

@BookdetailsRouter.post("/bookdetails/", response_model=dict)
async def create_book(
    bookreservationID: int = Form(...),
    reservationdetailsID: int = Form(...),
    bookID: int = Form(...),
    bookQuantity: int = Form(...),
    db=Depends(get_db)
):
    query = "INSERT INTO bookdetails (bookreservationID, reservationdetailsID, bookID, bookQuantity) VALUES (%s, %s, %s, %s)"
    db[0].execute(query, (bookreservationID, reservationdetailsID, bookID, bookQuantity))
    db[1].commit()

    # Retrieve the last inserted ID using LAST_INSERT_ID()
    db[0].execute("SELECT LAST_INSERT_ID()")
    new_book_id = db[0].fetchone()[0]

    return {"bookID": new_book_id, "bookreservationID": bookreservationID, "reservationdetailsID": reservationdetailsID, "bookID": bookID, "bookQuantity": bookQuantity}

@BookdetailsRouter.put("/bookdetails/{book_id}", response_model=dict)
async def update_book(
    book_id: int,
    bookreservationID: int = Form(...),
    reservationdetailsID: int = Form(...),
    bookID: int = Form(...),
    bookQuantity: int = Form(...),
    db=Depends(get_db)
):
    query = "UPDATE bookdetails SET bookreservationID = %s, reservationdetailsID = %s, bookID = %s, bookQuantity = %s WHERE bookID = %s"
    db[0].execute(query, (bookreservationID, reservationdetailsID, bookID, bookQuantity, book_id))

    # Check if the update was successful
    if db[0].rowcount > 0:
        db[1].commit()
        return {"message": "Book updated successfully"}
    
    # If no rows were affected, book not found
    raise HTTPException(status_code=404, detail="Book not found")

@BookdetailsRouter.delete("/bookdetails/{book_id}", response_model=dict)
async def delete_book(
    book_id: int,
    db=Depends(get_db)
):
    try:
        # Check if the book exists
        query_check_book = "SELECT bookID FROM bookdetails WHERE bookID = %s"
        db[0].execute(query_check_book, (book_id,))
        existing_book = db[0].fetchone()

        if not existing_book:
            raise HTTPException(status_code=404, detail="Book not found")

        # Delete the book
        query_delete_book = "DELETE FROM bookdetails WHERE bookID = %s"
        db[0].execute(query_delete_book, (book_id,))
        db[1].commit()

        return {"message": "Book deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()
