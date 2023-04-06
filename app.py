from flask import Flask, render_template, url_for, request, redirect, jsonify
from psycopg2 import connect, extras


app = Flask(__name__)

connection = psycopg2.connect(
	host = 'localhost',
	user = 'postgres',
	password = 'Pichisosoranchero1',
	db = 'flask_todo',
	port = 8080,
)

connection.autocommit = True

@app.route('/')
def index():
	return render_template('base.html')

@app.route('/add', methods=["POST"])
def add():
	if request.methos == 'POST':
		cursor = connection.cursor()	

		query = f"""insert into flask_todo (nombre) values()"""
	else:
		return None
	pass

@app.route('/update/<int:todo_id>')
def update():
	conn = get_connect()
	cur = conn.cursor(cursor_factory=extras.RealDictCursor)
	
	new_task = request.get_json()
	pass	

@app.route('/delete/<int:todo_id>')
def delete():
	conn = get_connect()
	cur = conn.cursor(cursor_factory=extras.RealDictCursor)

	cur.execute('delete from todo where id = %s returning *', (id, ))
	user = cur.fetchone()

	print(user)	
	conn.commit()
	cur.close()
	conn.close()

if __name__ == '__main__':
	app.run(debug=True)