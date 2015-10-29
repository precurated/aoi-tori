#create sample db structure

import sqlite3

db = sqlite3.connect('aoi-tori.db')

db.execute("DROP TABLE IF EXISTS twitter_account")
db.execute("DROP TABLE IF EXISTS group")
db.execute("DROP TABLE IF EXISTS global_rules")
db.execute("DROP TABLE IF EXISTS twitter_app")
db.execute("DROP TABLE IF EXISTS status")

db.execute("CREATE TABLE twitter_account (twitter_account_id INTEGER PRIMARY KEY, twitter_account_name CHAR(100), twitter_account_consumer_key CHAR(1000), twitter_account_consumer_secret CHAR(1000), twitter_account_hashtags CHAR(1000), twitter_account_subreddits CHAR(1000), twitter_account_exclude_words_local CHAR(1000), twitter_account_exclude_domains_local CHAR(1000), twitter_account_self_posts INTEGER,  FOREIGN KEY(twitter_account_group_id) REFERENCES group(group_id))")
db.execute("CREATE TABLE group (group_id INTEGER PRIMARY KEY, group_proxy INTEGER, FOREIGN KEY(group_twitter_app_id) REFERENCES twitter_app(twitter_app_id))")
db.execute("CREATE TABLE global_rules (global_rules_id INTEGER PRIMARY KEY, global_rules_exclude_words_global CHAR(1000), global_rules_exclude_domains_global CHAR(1000))")
db.execute("CREATE TABLE twitter_app (twitter_app_id INTEGER PRIMARY KEY, twitter_app_access_token CHAR(1000), twitter_app_access_secret CHAR(1000)")
db.execute("CREATE TABLE status (status_id INTEGER PRIMARY KEY, status_url CHAR(1000), status_source_time CHAR(1000), status_post_date CHAR(1000), FOREIGN KEY(status_twitter_account_id) REFERENCES twitter_account(twitter_account_id), status_recurrent_interval INTEGER, status_text  CHAR(1000), status_posted INTEGER, status_hashtags CHAR(1000))")


db.commit()