import sqlite3
from contextlib import closing


def execute_query(query, params=(), insert=False):
    # Connect to the database
    with closing(sqlite3.connect("database.db")) as db:
        with db:
            # Execute the query
            cursor = db.execute(query, params)
            # Fetch the result and get the last row id
            result = cursor.fetchall()
            last_row_id = cursor.lastrowid
    # Return the result and the last row id if insert is True, else return only the result
    return (result, last_row_id) if insert else result


def switch_frames(frame1, frame2):
    # Unpack the first frame
    frame1.pack_forget()
    # Pack the second frame
    frame2.pack()
