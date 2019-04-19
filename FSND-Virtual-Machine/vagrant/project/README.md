# Log Analysis

This is a python script that will query a newspaper's database and produce a text file report of the site's webtraffic and log data. The text file will show most popular article, author, and traffic error (404). 

## Install

Fork repo from git@github.com:haitanle/python-db-api.git

## Running

ssh into vagrant:
```sh
vagrant up
vagrant ssh
```

execute command from project /vagrant/project folder:
```sh
python query-log.py
```

## Results

query-log.py will produce a report.txt of analysis from newspaper's website traffic data and log data. 

2 views are created by query-log.py (top3 and logDate) to assist with the query analysis. 

