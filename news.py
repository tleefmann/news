#!/usr/bin/env python3
#
# A reporting tool for the NEWS database

import psycopg2

DBNAME = "news"

db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# sql query for answering question 1
query = """SELECT title, count(*) AS views FROM authors
            JOIN (
                SELECT author, title FROM log, articles
                    WHERE log.path=CONCAT('/article/',articles.slug)
                ) AS subq
            ON authors.id=subq.author
        GROUP BY title
        ORDER BY views DESC
        LIMIT 3"""
c.execute(query)
# print results
print("\nWhat are the most popular three articles of all time?")
for title, views in c.fetchall():
    print(" -", title, " --views:", views)

# sql query for answering question 2
query = """SELECT name, count(*) AS views FROM authors
            JOIN (
                SELECT author, title FROM log, articles
                    WHERE log.path=CONCAT('/article/',articles.slug)
                ) AS subq
            ON authors.id=subq.author
            GROUP BY name
            ORDER BY views DESC"""
c.execute(query)
# print results
print("\nWho are the most popular article authors of all time?")
for name, views in c.fetchall():
    print(" -", name, " --views:", views)

# sql query for answering question 3
query = """SELECT TO_CHAR(subq1.date, 'Mon DD, YYYY'), CAST(100*CAST
           (req_error AS float)/CAST(req_ok AS float)
           AS decimal(4,1)) AS error_percentage FROM (
            SELECT DATE(time), count(*) AS req_error FROM log
                WHERE status='404 NOT FOUND'
                group by DATE(time)
            ) AS subq1
           JOIN (
            SELECT DATE(time), count(*) AS req_ok FROM log
                WHERE status='200 OK' group by DATE(time)
            ) AS subq2
           ON subq1.date=subq2.date
           WHERE CAST(req_error AS float)/CAST(req_ok AS float)>0.01;"""
c.execute(query)
# print results
print("\nOn which days did more than 1% of requests lead to errors?")
for date, error_percentage in c.fetchall():
    print(" -", date, "  -- ", error_percentage, "%", " errors")

db.close()
