from bottle import route, view, run, template, debug, static_file, request

import sqlite3

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@route('/') #index
@view('database_view') #tpl
def show_db():
	db = sqlite3.connect('aoi-tori.db')
	c = db.cursor()

	c.execute("SELECT twitter_account.id, twitter_account.name, subreddit.name FROM twitter_account INNER JOIN subreddit on twitter_account.id = subreddit.account_id")

	data = c.fetchall()
	c.close()

	return {"rows":data, "title":"Db view", "columns":["account_id","twitter_name","subreddit_name"]}

debug(True)
run(host='0.0.0.0', port=8080, reloader=True)