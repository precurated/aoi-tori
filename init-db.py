# create sample db structure

import sqlite3

db = sqlite3.connect('database.db')

#twitter_account password,email etc. is just FYI, never use it in the app.
db.executescript("""
    PRAGMA foreign_keys = ON;

    DROP TABLE IF EXISTS twitter_global_rules;
    CREATE TABLE twitter_global_rules (
        twitter_global_rules_id INTEGER PRIMARY KEY NOT NULL,
        twitter_global_rules_exclude_words_global TEXT,
        twitter_global_rules_exclude_domains_global TEXT,
        twitter_global_rules_replace_string_in_url TEXT,
        twitter_global_rules_replace_string_in_title TEXT
        );

    DROP TABLE IF EXISTS twitter_app;
    CREATE TABLE twitter_app (
        twitter_app_id INTEGER PRIMARY KEY NOT NULL,
        twitter_app_name TEXT,
        twitter_app_access_token TEXT,
        twitter_app_access_secret TEXT
        );

    DROP TABLE IF EXISTS twitter_group;
    CREATE TABLE twitter_group (
        twitter_group_id INTEGER PRIMARY KEY NOT NULL,
        twitter_group_proxy TEXT,
        twitter_group_twitter_app_id INTEGER REFERENCES twitter_app(twitter_app_id)
        );

    DROP TABLE IF EXISTS twitter_account;
    CREATE TABLE twitter_account (
        twitter_account_id INTEGER PRIMARY KEY NOT NULL,
        twitter_account_name TEXT,
        twitter_account_email TEXT,
        twitter_account_password TEXT,
        twitter_account_note TEXT,
        twitter_account_consumer_key TEXT,
        twitter_account_consumer_secret TEXT,
        twitter_account_hashtags TEXT,
        twitter_account_subreddits TEXT,
        twitter_account_exclude_words_local TEXT,
        twitter_account_exclude_domains_local TEXT,
        twitter_account_replace_string_in_url TEXT,
        twitter_account_replace_string_in_title TEXT,
        twitter_account_self_posts INTEGER DEFAULT 0,
        twitter_account_twitter_group_id INTEGER REFERENCES twitter_group(twitter_group_id) DEFAULT 1
        );

    DROP TABLE IF EXISTS twitter_status;
    CREATE TABLE twitter_status (
        twitter_status_id INTEGER PRIMARY KEY NOT NULL,
        twitter_status_url TEXT,
        twitter_status_source_time TEXT,
        twitter_status_post_date TEXT,
        twitter_status_twitter_account_id INTEGER REFERENCES twitter_account(twitter_account_id),
        twitter_status_recurrent_interval INTEGER DEFAULT 0,
        twitter_status_text TEXT,
        twitter_status_posted INTEGER DEFAULT 0,
        twitter_status_hashtags TEXT
        );

    """)

db.executescript("""

    INSERT INTO twitter_global_rules (twitter_global_rules_id, twitter_global_rules_exclude_domains_global, twitter_global_rules_exclude_words_global)
        VALUES (1, 'reddit.com;', '');

    INSERT INTO twitter_status (
    	twitter_status_id, 
    	twitter_status_text
    	)
		VALUES (13, 'test');

    INSERT INTO twitter_status (
    	twitter_status_id, 
    	twitter_status_text
    	)
		VALUES (1, 'lorem');

    INSERT INTO twitter_status (
    	twitter_status_id, 
    	twitter_status_text
    	)
		VALUES (177, 'ipsum');

	INSERT INTO twitter_app (
		twitter_app_id,
		twitter_app_name,
		twitter_app_access_token,
		twitter_app_access_secret
		)
		VALUES (1, 'test43211234', 'XvAC93dSzfnp5nbz9kVmrzYSc', '5Pm5iVLXttKMitCseOExeC4gOmkAyDXG8xRMRuLxLPL1KB8yd4');

	INSERT INTO twitter_group (twitter_group_id, twitter_group_proxy, twitter_group_twitter_app_id)
	VALUES (1, ' ', 1);
	
    INSERT INTO twitter_account (twitter_account_id,
    	twitter_account_name, 
    	twitter_account_password,
    	twitter_account_email, 
    	twitter_account_subreddits,
    	twitter_account_consumer_key,
    	twitter_account_consumer_secret,
    	twitter_account_hashtags,
    	twitter_account_note
    	)
        VALUES (
        1, 
        'ruchaczmarek',
        'asdasd1',
        'xelnyq+marek@gmail.com',
        'photography',
        'XvAC93dSzfnp5nbz9kVmrzYSc',
        '5Pm5iVLXttKMitCseOExeC4gOmkAyDXG8xRMRuLxLPL1KB8yd4',
        'sony;canon;nikon;pentax;olympus;leica',
        'na tym koncie jest utworzona appka i podpieta');
	
    INSERT INTO twitter_account (twitter_account_id,
    	twitter_account_name, 
    	twitter_account_password,
    	twitter_account_email, 
    	twitter_account_subreddits,
    	twitter_account_consumer_key,
    	twitter_account_consumer_secret,
    	twitter_account_hashtags,
    	twitter_account_note
    	)
        VALUES (
        2, 
        'jacekhola',
        'asdasd1',
        'xelnyq+hola@gmail.com',
        'technology;google;apple;android',
        '',
        '',
        'microsoft;intel;google;apple;amd',
        'to konto nie jest podpiete pod appke jeszcze');

    """)

db.commit()