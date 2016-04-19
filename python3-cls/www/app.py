from flask import Flask, render_template, request
from datetime import datetime

import uuid
import blog

app = Flask(__name__)

blog = blog.Blog()

@app.route("/")
def index():
	return render_template('index.html', list=blog.get())

@app.route('/new', methods=['GET'])
def create_index():
	return render_template('new.html')

@app.route('/submit', methods=['POST'])
def create_submit():
	dt = datetime.now()
	b = {
		'id': int (dt.strftime("%s")),
		'title': request.form['title'],
		'content': request.form['content'],
		'cd': str(dt)
	}
	blog.new(b)
	return index()

@app.route('/edit/<int:article>', methods=['GET'])
def edit_index(article):
	return render_template('edit.html', article=blog.get(article))

@app.route('/edit_submit', methods=['POST'])
def edit_submit():
	id = int (request.form['id'])
	dt = datetime.now()
	b = {
		'id': id,
		'title': request.form['title'],
		'content': request.form['content'],
		'cd': str(dt)
	}
	blog.edit(b)
	return view(id)

@app.route('/view')
@app.route('/view/<int:article>')
def view(article=None):
	return render_template('view.html', article=blog.get(article))

@app.route('/admin')
def admin():
	return render_template('admin.html')


if __name__ == '__main__':
	app.run()
