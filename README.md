# news
### A simple Python based reporting tool for a PostgreSQL database

#### Prerequisites for running the reporting tool for the newsdata database
1. Install [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
2. Install [Vagrant](https://www.vagrantup.com/downloads.html).
3. Download and unzip [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) into */a_folder_of_your_choice/*.
4. cd into */a_folder_of_your_choice/FSND-Virtual-Machine/vagrant/*.
5. Start your VM by `vagrant up`.
6. Use `vagrant ssh` to ssh into your VM.
7. Install [psycopg2](http://initd.org/psycopg/) in your Python environment in the VM.

#### Instructions for running the reporting tool for the newsdata database
1. Download/unzip [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and [news.py](/news.py) to */a_folder_of_your_choice/FSND-Virtual-Machine/vagrant/*.
2. cd into */a_folder_of_your_choice/FSND-Virtual-Machine/vagrant/*.
3. If not already running, start your VM (`vagrant up`) and ssh into it (`vagrant ssh`).
4. cd into */vagrant*.
5. Use `psql -d news -f newsdata.sql` in the command line to create tables in the database.
6. Run the [news.py](/news.py) script using `python3 news.py`.

#### Design of the reporting tool:
The reporting tool was coded using [Python3](https://www.python.org/) . The [psycopg2](http://initd.org/psycopg/) library is used to connect to the
newsdata database. Three questions, namely
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

are answered using three individual SQL querys. The query results are collected and
printed as formatted text into the command line.
