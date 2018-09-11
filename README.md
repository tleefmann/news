This tool is used to access the newsdata database and create reports from the database 



Prerequisites for running the reporting tool for the newsdata database:

(1) You need to have Python 3 installed on your machine.
(2) You need to have the Python library "psycopg2" installed in your Python environment.
(3) You need to have the psql command line tool installed on your machine.



Instructions for running the reporting tool for the newsdata database:

(1) Copy the database(newsdata.sql) and the reporting tool (news.py) in the same directory
(2) Using a terminal cd into the directory where you copied the files
(3) Run "psql -d news -f newsdata.sql" in the command line to create tables in the database
(4) Run the news.py script using "python3 news.py"



Design of the reporting tool:

The reporting tool was coded using Python3. The "psycopg2" library is used to connect to the
newsdata database. Three question, namely

(1) What are the most popular three articles of all time?
(2) Who are the most popular article authors of all time?
(3) On which days did more than 1% of requests lead to errors?

are answered using three individual SQL querys. The query results are collected and
printed as formated text into the command line.