from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1702",
    database="todo_app"
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def index():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    cursor.execute("INSERT INTO tasks (title, description) VALUES (%s, %s)", (title, description))
    db.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_task(id):
    status = request.form['status']
    cursor.execute("UPDATE tasks SET status=%s WHERE id=%s", (status, id))
    db.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    cursor.execute("DELETE FROM tasks WHERE id=%s", (id,))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
