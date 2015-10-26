#create sample db structure

import sqlite3

db = sqlite3.connect('aoi-tori.db')

db.execute("DROP TABLE IF EXISTS twitter_account")
db.execute("DROP TABLE IF EXISTS tweet")
db.execute("DROP TABLE IF EXISTS subreddit")

db.execute("CREATE TABLE twitter_account (id INTEGER PRIMARY KEY, name CHAR(100), followers INTEGER)")
db.execute("CREATE TABLE tweet (id INTEGER PRIMARY KEY, text CHAR(1000), hashtags CHAR(1000), account_id INTEGER, FOREIGN KEY(account_id) REFERENCES twitter_account(id))")
db.execute("CREATE TABLE subreddit (id INTEGER PRIMARY KEY, name CHAR(100), include_self_posts INTEGER, exclude_domains CHAR(1000), exclude_words CHAR(1000), account_id INTEGER, FOREIGN KEY(account_id) REFERENCES twitter_account(id))")

db.execute("INSERT INTO twitter_account (id, name, followers) VALUES (1, 'test_name', 5000)")
db.execute("INSERT INTO twitter_account (id, name, followers) VALUES (2, 'test_name2', 20000)")
db.execute("INSERT INTO tweet (id, text, hashtags, account_id) VALUES (1, 'new apple computer', 'apple;computer', 1)")
db.execute("INSERT INTO tweet (id, text, hashtags, account_id) VALUES (2, 'new lightsaber shop', 'lightsaber;shop', 2)")
db.execute("INSERT INTO subreddit (id, name, include_self_posts, account_id) VALUES (1, 'apple', 0, 1)")
db.execute("INSERT INTO subreddit (id, name, include_self_posts, account_id) VALUES (2, 'starwars', 0, 2)")
db.execute("INSERT INTO subreddit (id, name, include_self_posts, account_id) VALUES (3, 'ironman', 0, 2)")

db.commit()