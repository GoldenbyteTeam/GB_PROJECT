"""
Write motivational quotes.

Doc https://github.com/GoldenbyteGH/PickMotivationalQuotes

"""

import psycopg2
from psycopg2 import Error
import configparser
import sys,random

RangeIndex = []			#Lista degli indici da cui verrà pecsato il quote causale
Categories = ['change','computers','courage','failure','fear','inspirational','learning']

# Connect to MariaDB Platform

config = configparser.ConfigParser()
config.read('quotes_config.ini')                       #Read Credentials of DB

try:
    conn = psycopg2.connect(user=config['postgres']['user'],
                     password=config['postgres']['psw'],
                     host=config['postgres']['host'],
                     port="5432",
                     database=config['postgres']['db'])

except (Exception, Error) as error:
    print(f"Error connecting to MariaDB Platform: {error}")
    sys.exit(1)


# Get Cursor
cur = conn.cursor()

RandomCategory = random.choice(Categories)

query = ("(SELECT id FROM motquotes WHERE category =  '"+RandomCategory+"' order by id ASC LIMIT 1)UNION(SELECT id FROM motquotes WHERE category =  '"+RandomCategory+"' order by id DESC LIMIT 1)")

cur.execute(query)
myresult = cur.fetchall()

for x in myresult:
  RangeIndex.append(x[0])

IDQuote = random.randint(RangeIndex[0],RangeIndex[1])

query = 'SELECT quotes,author FROM motquotes WHERE id = '+str(IDQuote)
cur.execute(query)
myresult = cur.fetchall()

f_quote  = open("templates/pages/quotes.html", "w")
f_author = open("templates/pages/author.html", "w")
f_quote.write(str(myresult[0][0]))
f_author.write(str(myresult[0][1]))
f_quote.close()
f_author.close()

cur.close()
conn.close()
