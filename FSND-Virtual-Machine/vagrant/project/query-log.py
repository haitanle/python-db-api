# !/usr/bin/env python

if __name__== "__main__":

import psycopg2

conn = psycopg2.connect("dbname=news")
cur = conn.cursor()


message = "1. What are the most popular three articles of all time? \n\n"

# create top3 views
cur.execute("create or replace view top3 as \
    select path as article_slug, count(*) as viewCount \
    from log where path like '%article%' \
    group by path order by viewCount desc;")

# query to get top3 title
cur.execute("select b.title, a.viewCount from top3 a \
    join articles b \
    on a.article_slug = concat('/article/', b.slug);")

top_titles = cur.fetchall()

for x in range(3):
    result = '"' + top_titles[x][0] + '" --- '
    result += str(top_titles[x][1]) + " views \n"
    message += result


message += "\n2. Who are the most popular article authors of all time? \n\n"
# query to get top authors
cur.execute("select c.name, count(*) from (\
    select substring(path from position('article/' in path)+8) \
    as article_slug from log) as a \
    join articles b on a.article_slug = b.slug \
    join authors c on b.author = c.id \
    group by c.name order by count desc;")

top_authors = cur.fetchall()

for author in top_authors:
    result = author[0] + " -- " + str(author[1]) + " views \n"
    message += result


message += "\n3. On which days did more than 1% \
of requests lead to errors? \n\n"

# create view for log data
cur.execute("create or replace view logdate \
    as select date(time) as date, status, count(*) \
    from log group by date, status;")

# query to get day's error percentage
cur.execute("select date, error_percent from \
    (select a.date, cast( \
        (cast(b.count as numeric)/(b.count+a.count)) *100 as numeric(6,2))\
        as error_percent \
        from logdate as a, logdate as b \
        where a.date = b.date and a.status < b.status order by a.date ) \
    as error where error_percent > 1;")
day_errors = cur.fetchall()

for error in day_errors:
    result = str(error[0]) + " -- " + str(error[1]) + "% errors"
    message += result

print(message)

f = open('report.txt', 'w')
f.write(message)
f.close()

cur.close()
conn.close()
