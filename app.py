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


@route('/')
@view('database_view')
def show_db():

	cursor = database_Connect()
	cursor.execute("SELECT * FROM twitter_status ORDER BY twitter_status_id DESC LIMIT 100 ")

	data = cursor.fetchall()

	return {\
	"columns":database_TableColumnNames('twitter_status', cursor),\
	"rows":data,\
	"title":"Twitter admin"\
	}

	cursor.close()

@route('/accounts')
@view('database_view')
def show_db():

	cursor = database_Connect()
	cursor.execute("SELECT * FROM twitter_account")
	data = cursor.fetchall()

	return {\
	"columns":database_TableColumnNames('twitter_account', cursor),\
	"rows":data,\
	"title":"Twitter admin"\
	}

	cursor.close()


@route('/groups')
@view('database_view')
def show_db():

	cursor = database_Connect()
	cursor.execute("SELECT * FROM twitter_group")
	data = cursor.fetchall()

	return {\
	"columns":database_TableColumnNames('twitter_group', cursor),\
	"rows":data,\
	"title":"Twitter admin"\
	}

	cursor.close()


@route('/rules')
@view('database_view')
def show_db():

	cursor = database_Connect()
	cursor.execute("SELECT * FROM twitter_global_rules")
	data = cursor.fetchall()

	return {\
	"columns":database_TableColumnNames('twitter_global_rules', cursor),\
	"rows":data,\
	"title":"Twitter admin"\
	}

	cursor.close()


@route('/apps')
@view('database_view')
def show_db():

	cursor = database_Connect()
	cursor.execute("SELECT * FROM twitter_app")
	data = cursor.fetchall()

	return {\
	"columns":database_TableColumnNames('twitter_app', cursor),\
	"rows":data,\
	"title":"Twitter admin"\
	}

	cursor.close()

debug(True)
run(host='127.0.0.1', port=8080, reloader=True)