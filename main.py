from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model.student import StudentRouter
from model.book import BookRouter
from model.uniform import UniformRouter
from model.admin import AdminRouter
from model.reservation import ReservationRouter
from model.reservationdetails import ReservationdetailsRouter
from model.bookdetails import BookdetailsRouter
from model.uniformdetails import UniformdetailsRouter

app = FastAPI()

origins = [
    # "http://localhost:5000",   Ito po yung ginamit kong URL for frontend - Jem Pillora
    "http://localhost:8000",
    "https://uicbookstore.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include CRUD routes from modules
app.include_router(StudentRouter, prefix="/api")
app.include_router(BookRouter, prefix="/api")
app.include_router(UniformRouter, prefix="/api")
app.include_router(AdminRouter, prefix="/api")
app.include_router(ReservationRouter, prefix="/api")
app.include_router(ReservationdetailsRouter, prefix="/api")
app.include_router(BookdetailsRouter, prefix="/api")
app.include_router(UniformdetailsRouter, prefix="/api")
