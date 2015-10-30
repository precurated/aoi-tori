from bottle import route, view, run, template, debug, static_file, request
import datetime
import time
import sqlite3

global database_file
database_file = 'database.db'

def database_Connect():
	db = sqlite3.connect(database_file)
	cursor = db.cursor()
	return cursor

def database_TableColumnNames(TableName, cursor):
	cursor.execute("SELECT * FROM " + TableName)
	columns = list(map(lambda x: x[0], cursor.description))
	return columns

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')


@route('/') #index
@view('database_view') #tpl
def show_db():

	cursor = database_Connect()
	cursor.execute("SELECT * FROM global_rules")
	data = cursor.fetchall()

	return {\
	"columns":database_TableColumnNames('global_rules', cursor),\
	"rows":data,\
	"title":"Db view"\
	}

	cursor.close()



debug(True)
run(host='0.0.0.0', port=8080, reloader=True)