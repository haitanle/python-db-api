# Log Analysis

This is a python script that will query a newspaper's database and produce a text file report of the site's webtraffic and log data. The text file will show most popular article, author, and traffic error (404). 

## Install

Fork repo from git@github.com:haitanle/python-db-api.git

## Dependencies

psycopg2 - python db-api to connect to Postgres database
```sh
pip install psycopg2
```

## Data Preparation

Download newsdata.sql data file at https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Load the data into the Postgres database with command
```sh
psql -d news -f newsdata.sql
``` 

## Running

ssh into vagrant:
```sh
vagrant up
vagrant ssh
```

execute command from project /vagrant/project folder:
```sh
python2 query-log.py
```

2 views are created by the script (top3 and logDate) to assist with the query analysis. 
No manual view creatino is needed. 


## Results

query-log.py will produce a report.txt of analysis from newspaper's website traffic data and log data. 

