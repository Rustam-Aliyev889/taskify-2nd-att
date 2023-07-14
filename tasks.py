import psycopg2

conn = psycopg2.connect(
        host = "dpg-cioihe5ph6elhbtn9da0-a.oregon-postgres.render.com",
        database = "taskmanager_d17c",
        user = "taskmanager_d17c_user",
        password = "JvqT9guGY2l026uNtkySBbp1hlY5TVbK",
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