from sqlalchemy import text
from database import engine

def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM users;"))
            users = result.fetchall()
            print("Connected successfully. Found users:")
            for row in users:
                print(dict(row._mapping))  # for clean output
    except Exception as e:
        print("Connection failed:", str(e))

if __name__ == "__main__":
    test_connection()
