# within this file we will create the tables for the marketplace

import sqlite3
baza_de_date_marketplace = "marketplace.db"  #numele fisierului unde avem baza de date
connection = sqlite3.connect(baza_de_date_marketplace)   #ne conectam la baza de date
cursor = connection.cursor()  #creaza cursor



# create tables

# table users
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    address TEXT,
    city TEXT,
    postal_code TEXT
);
""")






# table products
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock_count INTEGER NOT NULL DEFAULT 0,
    description TEXT);"""
)

# table orders
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES users(id) 
         );"""

)

# table order_items

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    total_price REAL NOT NULL,
    FOREIGN KEY(order_id) REFERENCES orders(id), 
    FOREIGN KEY(product_id) REFERENCES products(id)
        
        );"""
)

connection.commit()