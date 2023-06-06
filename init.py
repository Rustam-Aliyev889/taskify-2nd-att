import psycopg2

conn = psycopg2.connect(
        host = "localhost",
        database = "taskmanager",
        user = "postgres",
        password = "password",
        port = "5432"
    ) 
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS meetings (
                id     SERIAL PRIMARY KEY,
                topic  varchar(30) NOT NULL,
                date   DATE,
                time   TIME,
                department varchar(20) NOT NULL,
                comments varchar(150)
            )''')
conn.commit()
cur.close()
conn.close()   
