import string, random, datetime, sqlite3

def create_db():
    conn = sqlite3.connect('auth.db')

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
    conn = sqlite3.connect('auth.db')

    insert_sql=f"INSERT INTO AUTH (TICKET, NAME) VALUES ('{ticket}', '{name}')"

    conn.execute(insert_sql)

    conn.close()