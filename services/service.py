import string, random, datetime, sqlite3
from config import AUTH_DB

auth_db=AUTH_DB

def create_db():
    conn = sqlite3.connect(auth_db)

    sql='''
        CREATE TABLE AUTH
        (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TICKET INT NOT NULL,
            NAME           TEXT    NOT NULL
        )
        '''

    conn.execute(sql)

    conn.close()

def generate_ticket():
    letters = string.ascii_lowercase + string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(26))

    dt= datetime.datetime.now().strftime("%f")
    ticket=f"OYEN-{result_str}-{dt}"
    return ticket

def insert_ticket(ticket, name):
    conn = sqlite3.connect(auth_db)

    insert_sql=f"INSERT INTO AUTH (TICKET, NAME) VALUES ('{ticket}', '{name}')"

    conn.execute(insert_sql)
    conn.commit()

    conn.close()

def get_name(ticket):
    conn = sqlite3.connect(auth_db)
    sql=f"SELECT NAME FROM AUTH WHERE TICKET='{ticket}'"

    cur = conn.cursor()
    cur.execute(sql)

    name = cur.fetchall()
    conn.close()
    return name