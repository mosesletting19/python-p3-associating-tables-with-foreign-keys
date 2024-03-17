import sqlite3

#define connection and cursor
connection =sqlite3.connect('pets_database.db')
cursor=connection.cursor()
 
 #Step 1: Creating the Cats Table
cursor.execute('''CREATE TABLE cats (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    breed TEXT)''')
connection .commit()
# print("Table created successfully")

#insert data into the table
cats_data=[
    ('maru',3,'Scottish Fold'),
    ('Whiskers',4,'Siamese'),
    ('Hana',2,'Tabby')
    
]
cursor.executemany('INSERT INTO cats (name,age,breed) VALUES (?,?,?)',cats_data)
#commit  the changes to the database
connection.commit()
# print("Data inserted successfully")


#Step 2: Creating the Owners Table
cursor.execute('CREATE TABLE owners (id INTEGER PRIMARY KEY, name TEXT)')

#Step 3: Add Foreign Key to Cats Table
cursor.execute('ALTER TABLE cats ADD COLUMN owner_id INTEGER')

#Step 4: Associating Cats to Owners
cursor.execute('INSERT INTO owners (name) VALUES ("mugumogu")')
cursor.execute('INSERT INTO owners (name) VALUES ("Letting")')

cursor.execute('UPDATE cats SET owner_id = 1 WHERE name = "Maru"')

cursor.execute('UPDATE cats SET owner_id = 1 WHERE name = "Hana";')

cursor.execute('UPDATE cats SET owner_id = 2 WHERE name = "Whiskers"')
connection.commit()
 
 
cursor.execute('SELECT * FROM cats WHERE owner_id = 1')


