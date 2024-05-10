# model/db.py
import mysql.connector

db_config = {
    "host": "139.59.246.2",
    "user": "thisisbookstore",
    "password": "thisisgrp13",
    "database": "bookstore_grp13",
    "port": 3306,
}

# db_config = {
#    "host": "localhost",
#    "user": "root",
#    "password": "",
#    "database": "bookstore_grp13",
#    "port": 3306,
#}



# ETO PO YUNG GINAMIT KONG CONFIG FOR DATABASE
# db_config = {
#    "host": "localhost",
#    "user": "root",
#    "password": "",
#    "database": "bookstore_grp13",
#    "port": 3306,
#}

def get_db():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    try:
        yield cursor, db
    finally:
        cursor.close()
        db.close()
