import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2.extras

app = Flask(__name__)



def db_conn():
    conn = psycopg2.connect(
        host = "localhost",
        database = "taskmanager",
        user = "postgres",
        password = "password",
        port = "5432"
    )
    return conn


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/meetings")
def meetings():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM meetings''')
    meetings = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("meetings.html", meetings= meetings)


@app.route('/add_meeting')
def add_meeting():
    return render_template('add_meeting.html')

@app.route("/new_meeting", methods=["POST"])
def new_meeting():
    conn = db_conn()
    cur = conn.cursor()
    topic = request.form["topic"]
    date = request.form["date"]
    time = request.form["time"]
    department = request.form["department"]
    comments = request.form["comments"]
    query_string="INSERT INTO meetings (topic, date, time, department, comments) VALUES ('" + topic + "','" + date + "','" + time + "','" +  department + "','" +  comments + "');"
    cur.execute(query_string)
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('meetings'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_meetings(id):
    conn = db_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM meetings WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', meetings = data[0])
 
@app.route('/update/<id>', methods=['POST'])
def update_meetings(id):
    if request.method == 'POST':
        topic = request.form["topic"]
        date = request.form["date"]
        time = request.form["time"]
        department = request.form["department"]
        comments = request.form["comments"]
        conn = db_conn()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE meetings
            SET topic = %s,
                date = %s,
                time = %s,
                department = %s,
                comments = %s
            WHERE id = %s
        """, (topic, date, time, department, comments, id))
        conn.commit()
        return redirect(url_for('meetings'))


@app.route('/delete <id>') #, methods=['POST', 'GET'])
def delete(id):
    conn = db_conn()
    cur = conn.cursor()
   # id = request.form['id']
    cur.execute('''DELETE FROM meetings WHERE id = %s''',(id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('meetings'))


# Tasks


@app.route("/tasks")
def tasks():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM tasks''')
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("tasks.html", tasks= tasks)


@app.route('/add_task')
def add_task():
    return render_template('add_task.html')


@app.route("/new_task", methods=["POST"])
def new_task():
    conn = db_conn()
    cur = conn.cursor()
    task = request.form["task"]
    date = request.form["date"]
    department = request.form["department"]
    urgency = request.form["urgency"]
    comments = request.form["comments"]
    query_string="INSERT INTO tasks (task, date, department, urgency, comments) VALUES ('" + task + "','" + date + "','" + department + "','" +  urgency + "','" +  comments + "');"
    cur.execute(query_string)
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('tasks'))


if __name__ == "__main__":
    app.run(debug=True)