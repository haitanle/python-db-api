# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

# POSTS = [("This is the first post.", datetime.datetime.now())]
database = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  conn = psycopg2.connect("dbname="+database)
  cursor = conn.cursor()
  cursor.execute("select content, time from posts order by time desc;")

  results = cursor.fetchall()  #returns list of tuples

  conn.close()

  return results

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  conn = psycopg2.connect("dbname="+database)
  cursor = conn.cursor()

  cursor.execute("insert into posts (content, time ) VALUES (%s, %s)",
  								(bleach.clean(content), datetime.datetime.now()))

  conn.commit()
  conn.close()
  #POSTS.append((content, datetime.datetime.now()))


