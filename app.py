from bottle import route, run, template, debug, static_file

import sqlite3

@route('/')
def show_db():
	db = sqlite3.connect('aoi-tori.db')
	c = db.cursor()
	c.execute("SELECT twitter_account.id, twitter_account.name, subreddit.name FROM twitter_account INNER JOIN subreddit on twitter_account.id = subreddit.account_id")
	data = c.fetchall()
	c.close()
	output = template('database_view', rows=data)
	return output

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

debug(True)
run(host='0.0.0.0', port=8080, reloader=True)