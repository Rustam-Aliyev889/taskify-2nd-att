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
                topic    varchar(30) NOT NULL,
                department varchar(20) NOT NULL,
                comments varchar(150)
            )''')
#cur.execute('''INSERT INTO meetings (id, topic, department, comments) VALUES (1, 'Profit', 'Sales', 'Good job'), (2, 'Ads', 'Marketing', 'New ads'),(3, 'Bugs', 'Engineers', 'Fix')''')

conn.commit()
cur.close()
conn.close()   
