# model/book.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db

BookRouter = APIRouter(tags=["Book"])

# CRUD operations

@BookRouter.get("/book/", response_model=list)
async def read_books(
    db=Depends(get_db)
):
    query = "SELECT mngstore, bookID, mngbkstore, bookTitle, bookquantityAvailability, bookpriceDetails FROM book"
    db[0].execute(query)
    books = [{
        # "mngstore": book[0],
        # "bookID": book[1],
        # "mngbkstore": book[2],
        # "bookTitle": book[3],
        # "bookquantityAvailability": book[4],
        # "bookpriceDetails": book[5]

        "id": book[1],
        "category": "book",
        "name": book[3],
        "price": book[5],
        "stock": book[4],
        "image": "",
        "mngstore": book[0],
    } for book in db[0].fetchall()]
    return books

@BookRouter.get("/book/{book_id}", response_model=dict)
async def read_book_by_id(
    book_id: int,
    db=Depends(get_db)
):
    query = "SELECT mngstore, bookID, mngbkstore, bookTitle, bookquantityAvailability, bookpriceDetails FROM book WHERE bookID = %s"
    db[0].execute(query, (book_id,))
    book = db[0].fetchone()
    if book:
        return {"mngstore": book[0], "bookID": book[1], "mngbkstore": book[2], "bookTitle": book[3], "bookquantityAvailability": book[4], "bookpriceDetails": book[5]}
    raise HTTPException(status_code=404, detail="Book not found")

@BookRouter.post("/book/", response_model=dict)
async def create_book(
    mngstore: str = Form(...),
    mngbkstore: str = Form(...),
    bookTitle: str = Form(...),
    bookquantityAvailability: int = Form(...),
    bookpriceDetails: int = Form(...),
    db=Depends(get_db)
):
    query = "INSERT INTO book (mngstore, mngbkstore, bookTitle, bookquantityAvailability, bookpriceDetails) VALUES (%s, %s, %s, %s, %s)"
    db[0].execute(query, (mngstore, mngbkstore, bookTitle, bookquantityAvailability, bookpriceDetails))
    db[1].commit()

    # Retrieve the last inserted ID using LAST_INSERT_ID()
    db[0].execute("SELECT LAST_INSERT_ID()")
    new_book_id = db[0].fetchone()[0]

    return {"bookID": new_book_id, "mngstore": mngstore, "mngbkstore": mngbkstore, "bookTitle": bookTitle, "bookquantityAvailability": bookquantityAvailability, "bookpriceDetails": bookpriceDetails}

@BookRouter.put("/book/{book_id}", response_model=dict)
async def update_book(
    book_id: int,
    mngstore: str = Form(...),
    mngbkstore: str = Form(...),
    bookTitle: str = Form(...),
    bookquantityAvailability: int = Form(...),
    bookpriceDetails: int = Form(...),
    db=Depends(get_db)
):
    query = "UPDATE book SET mngstore = %s, mngbkstore = %s, bookTitle = %s, bookquantityAvailability = %s, bookpriceDetails = %s WHERE bookID = %s"
    db[0].execute(query, (mngstore, mngbkstore, bookTitle, bookquantityAvailability, bookpriceDetails, book_id))

    # Check if the update was successful
    if db[0].rowcount > 0:
        db[1].commit()
        return {"message": "Book updated successfully"}

    # If no rows were affected, book not found
    raise HTTPException(status_code=404, detail="Book not found")

@BookRouter.delete("/book/{book_id}", response_model=dict)
async def delete_book(
    book_id: int,
    db=Depends(get_db)
):
    try:
        # Check if the book exists
        query_check_book = "SELECT bookID FROM book WHERE bookID = %s"
        db[0].execute(query_check_book, (book_id,))
        existing_book = db[0].fetchone()

        if not existing_book:
            raise HTTPException(status_code=404, detail="Book not found")

        # Delete the book
        query_delete_book = "DELETE FROM book WHERE bookID = %s"
        db[0].execute(query_delete_book, (book_id,))
        db[1].commit()

        return {"message": "Book deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()
