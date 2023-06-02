import psycopg2
from flask import Flask, render_template, request, redirect, url_for

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
    #conn = db_conn()
    #cur = conn.cursor()
    #cur.execute('''SELECT * FROM meetings''')
    #meetings = cur.fetchall()
    #cur.close()
    #conn.close()
    #print(meetings)
    return render_template("base.html") #meetings= meetings )



@app.route("/meetings")
def meetings():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM meetings''')
    meetings = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("meetings.html", meetings= meetings)

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/add_meeting')
def add_meeting():
    return render_template('add_meeting.html')

@app.route("/new_meeting", methods=["POST"])
def new_meeting():
    conn = db_conn()
    cur = conn.cursor()
    topic = request.form["topic"]
    department = request.form["department"]
    comments = request.form["comments"]
    #cur.execute('''INSERT INTO meetings (topic, department, comments) VALUES(%s, %s, %s)''', (topic, department, comments))
    query_string="INSERT INTO meetings (topic, department, comments) VALUES ('" + topic + "','" +  department + "','" +  comments + "');"
    cur.execute(query_string)
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('meetings'))

@app.route("/update/<id>", methods=['POST'])
def update(id):
    conn = db_conn()
    cur = conn.cursor()
    topic = request.form["topic"]
    department = request.form["department"]
    comment = request.form["comment"]
    cur.execute('''UPDATE meetings SET topic=%s, department=%s, comment=%s WHERE id=%s''', (topic, department, comment, id))
    cur.execute()
    conn.commit()
    return redirect(url_for('add_meetings'))

#@app.route('/delete', methods=['POST', 'GET'])
#def delete():
 #   conn = db_conn()
 #   cur = conn.cursor()
  #  id = request.form['id']
  #  cur.execute('''DELETE FROM meetings WHERE id = %s''',(id))
  #  conn.commit()
  #  cur.close()
  #  conn.close()
   # return redirect(url_for('meetings'))

@app.route('/delete <id>') #, methods=['POST', 'GET'])
def delete(id):
    conn = db_conn()
    cur = conn.cursor()
   # id = request.form['id']
    print("ID ="  + id)
    cur.execute('''DELETE FROM meetings WHERE id = %s''',(id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('meetings'))



if __name__ == "__main__":
    app.run(debug=True)