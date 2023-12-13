import string, random, datetime, sqlite3
from config import AUTH_DB

auth_db=AUTH_DB

def create_db():
    # Create users table
    conn = sqlite3.connect(auth_db)

    sql='''
        CREATE TABLE USERS
        (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME VARCHAR(50) NOT NULL,
            PASSWORD VARCHAR(255) NOT NULL
        )
        '''

    conn.execute(sql)

    # Create user records
    insert_users_sql = '''
        INSERT INTO USERS (NAME, PASSWORD)
        VALUES ('John Doe', 'john123'),
                ('Oyen', 'cuteOyen')
    '''

    conn.execute(insert_users_sql)
    conn.commit()
    conn.close()

    # Create tickets table
    conn = sqlite3.connect(auth_db)

    tic_sql='''
        CREATE TABLE TICKETS
        (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TICKET INTEGER NOT NULL,
            NAME VARCHAR(10) NOT NULL
        )
        '''

    conn.execute(tic_sql)

    conn.close()

def generate_ticket(name, password):

    # Check if credentials are valid
    conn = sqlite3.connect(auth_db)
    sql=f"SELECT COUNT(*) FROM USERS WHERE NAME='{name}' AND PASSWORD='{password}'"
    result = conn.execute(sql).fetchone()[0]
    print(result)
    if result == 0: # Invalid user
        return
    
    # Generate ticket
    letters = string.ascii_lowercase + string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(26))

    dt= datetime.datetime.now().strftime("%f")
    ticket=f"OYEN-{result_str}-{dt}"
    return ticket

def insert_ticket(ticket, name):
    conn = sqlite3.connect(auth_db)

    insert_sql=f"INSERT INTO TICKETS (TICKET, NAME) VALUES ('{ticket}', '{name}')"

    conn.execute(insert_sql)
    conn.commit()

    conn.close()

def get_name(ticket):
    conn = sqlite3.connect(auth_db)
    sql=f"SELECT NAME FROM TICKETS WHERE TICKET='{ticket}'"

    cur = conn.cursor()
    cur.execute(sql)

    name = cur.fetchall()
    conn.close()
    return name

def delete_ticket(ticket):
    conn = sqlite3.connect(auth_db)

    del_sql=f"DELETE FROM TICKETS WHERE TICKET='{ticket}'"

    conn.execute(del_sql)
    conn.commit()

    conn.close()