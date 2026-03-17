

import sqlite3
from sesiunea_12.marketplace.tables import baza_de_date_marketplace

connection = sqlite3.connect(baza_de_date_marketplace)
cursor = connection.cursor()

# CREATE we will create a user and register it in the database

cursor.execute(
    """
    INSERT INTO users(username, email, password, first_name, last_name)
    VALUES ('denisa12', 'denisa@email', '1234', 'denisa', 'radu' )
    """
)

connection.commit()

# CREATE

userquery = """
    INSERT INTO users(username, email, password, first_name, last_name)
    VALUES (?, ?, ?, ?, ? )
    """

utilizatori = [
    ('denisa2e', 'denisa12@gmail', '1234','denisa','radu'),
    ('denisa2l', 'denisa5@yahoo.com', '5555','denisa','radu'),
    ('denisa2', 'denisa4@mail.ro', '1789','denisa','radu')
]
cursor.executemany(userquery, utilizatori)

connection.commit()

# READ we will read a user from the db using id

cursor.execute("SELECT * FROM users WHERE id = 2")
user_id = cursor.fetchall()
print(user_id)

# UPDATE we will update a user from the db using an id

cursor.execute("""UPDATE users SET first_name = 'Alina' WHERE id = 1""") #folosim ghilimele triple
connection.commit()

# DELETE - we will delete a user using the id

cursor.execute("""DELETE FROM users WHERE id = 2""")
connection.commit()

print("DB path:", baza_de_date_marketplace)




