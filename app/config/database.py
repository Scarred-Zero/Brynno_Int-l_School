from mysql.connector import connect


def get_connection():
    try:
        db = connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="brynno_international_school_db"
        )

        if db.is_connected():
            print("DATABASE CONNECTED")

        cursor = db.cursor(dictionary=True, buffered=True)
        return db, cursor

    except Exception as e:
        print("DATABASE ERROR:", str(e))
