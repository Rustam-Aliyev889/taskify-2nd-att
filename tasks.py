import psycopg2

conn = psycopg2.connect(
        host = "localhost",
        database = "taskmanager",
        user = "postgres",
        password = "password",
        port = "5432"
    ) 
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tasks (
                id     SERIAL PRIMARY KEY,
                task   varchar(30) NOT NULL,
                date   DATE,
                department varchar(20) NOT NULL,
                urgency   varchar(10),
                comments varchar(150)
            )''')
conn.commit()
cur.close()
conn.close()   