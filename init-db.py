# create sample db structure

import sqlite3

db = sqlite3.connect('database.db')

db.executescript("""
    PRAGMA foreign_keys = ON;

    DROP TABLE IF EXISTS global_rules;
    CREATE TABLE global_rules (
        global_rules_id INTEGER PRIMARY KEY NOT NULL,
        global_rules_exclude_words_global TEXT,
        global_rules_exclude_domains_global TEXT
        );

    DROP TABLE IF EXISTS twitter_app;
    CREATE TABLE twitter_app (
        twitter_app_id INTEGER PRIMARY KEY NOT NULL,
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
        twitter_account_consumer_key TEXT,
        twitter_account_consumer_secret TEXT,
        twitter_account_hashtags TEXT,
        twitter_account_subreddits TEXT,
        twitter_account_exclude_words_local TEXT,
        twitter_account_exclude_domains_local TEXT,
        twitter_account_self_posts INTEGER DEFAULT 0,
        twitter_account_twitter_group_id INTEGER REFERENCES twitter_group(twitter_group_id)
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
    INSERT INTO twitter_account (twitter_account_id, twitter_account_name)
        VALUES (1, 'test_name');
    INSERT INTO global_rules (global_rules_id, global_rules_exclude_domains_global, global_rules_exclude_words_global)
        VALUES (1, 'reddit.com;', 'reddit');
    """)

db.commit()
