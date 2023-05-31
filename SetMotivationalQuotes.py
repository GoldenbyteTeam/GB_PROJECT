#!/usr/bin/python3

"""
Write motivational quotes.

Crontab Job at 00.00 every day

Doc https://github.com/GoldenbyteGH/PickMotivationalQuotes

"""
import os
from pathlib import Path
import psycopg2
from psycopg2 import Error
import configparser
import sys,random

BASE_DIR = Path(__file__).resolve().parent
RangeIndex = []			# quote's index list
Categories = ['change','computers','courage','failure','fear','inspirational','learning']

# Connect to DB
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR,'quotes_config.ini'))                       #Read DB settings

try:
    conn = psycopg2.connect(user=config['postgres']['user'],
                     password=config['postgres']['psw'],
                     host=config['postgres']['host'],
                     port="5432",
                     database=config['postgres']['db'])

except (Exception, Error) as error:
    print(f"Error connecting to DB: {error}")
    sys.exit(1)


# Get Cursor
cur = conn.cursor()

RandomCategory = random.choice(Categories)

query = ("(SELECT id FROM motquotes WHERE category =  '"+RandomCategory+"' order by id ASC LIMIT 1)UNION(SELECT id FROM motquotes WHERE category =  '"+RandomCategory+"' order by id DESC LIMIT 1)")

cur.execute(query)
myresult = cur.fetchall()
print(myresult)
for x in myresult:
  RangeIndex.append(x[0])   # 'cur' return a tuple of 2 elements, the value and an empty element (es. [(7608,), (7873,)])
print(RangeIndex)
IDQuote = random.randint(RangeIndex[0],RangeIndex[1])

query = 'SELECT quotes,author FROM motquotes WHERE id = '+str(IDQuote)
cur.execute(query)
myresult = cur.fetchall()

f_quote  = open(os.path.join(BASE_DIR,"templates/pages/quotes.html"), "w")
f_author = open(os.path.join(BASE_DIR,"templates/pages/author.html"), "w")
f_quote.write(str(myresult[0][0]))
f_author.write(str(myresult[0][1]))
f_quote.close()
f_author.close()

cur.close()
conn.close()

#Restart Gunicorn
os.system("sudo /bin/systemctl restart gunicorn")