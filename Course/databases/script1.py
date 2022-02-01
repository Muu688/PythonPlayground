import psycopg2

def establish():
    conn=psycopg2.connect("dbname='pythoncourse' user='postgres' password='password' host='localhost'")
    cur=conn.cursor() # Cursor Obj

def create_table():
    conn=psycopg2.connect("dbname='pythoncourse' user='postgres' password='password' host='localhost'")
    cur=conn.cursor() # Cursor Obj
    # SQL Command to Execute.
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection_handler(conn)

def insert_data(item, quantity, price):
    conn=psycopg2.connect("dbname='pythoncourse' user='postgres' password='password' host='localhost'")
    cur=conn.cursor() # Cursor Obj
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    connection_handler(conn)

def connection_handler(conn):
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='pythoncourse' user='postgres' password='password' host='localhost'")
    cur=conn.cursor() # Cursor Obj
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def deletey(item):
    conn=psycopg2.connect("dbname='pythoncourse' user='postgres' password='password' host='localhost'")
    cur=conn.cursor() # Cursor Obj
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    connection_handler(conn)

def update_quantity(quantity, price, item):
    conn=psycopg2.connect("dbname='pythoncourse' user='postgres' password='password' host='localhost'")
    cur=conn.cursor() # Cursor Obj
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    connection_handler(conn)

create_table()
insert_data("Lazer Glasses", 1, 5000)
print(view())
deletey("Weeb Glasses")
print(view())
update_quantity(0, 10000, "Lazer Glasses")