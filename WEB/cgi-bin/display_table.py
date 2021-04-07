#!/usr/bin/python3
import cgi, sqlite3, os, re

#connect to the database 
if 'REQUEST_METHOD' in os.environ:
  data = cgi.FieldStorage()
  table = data["table"].value
  dbname = data["dbname"].value
  connection = sqlite3.connect("../"+dbname)
else:
    print("This script can only be run as a cgi script")
    exit()
#create a 'cursor' object to pass the query to the
#database and return the results
curs = connection.cursor()
#setup the SQL for the query and execute the query
curs.execute("SELECT * FROM '{}'".format(table))
#fetch all the results into a list (of tuples)
rows = curs.fetchall()
# Output web server response and headers - the blank line is needed
print(f'''Content-type:text/html

<!doctype html>
<html>
<head>
<title>{table}</title>
<style>
table {{border:0;border-collapse:collapse;}}
td {{border:1px solid}}
th {{border:1px solid; text-align:left;}}
</style>
</head>
<body>
<h1>{table}</h1>''')

if len(rows)==0:
  print("Empty table<br>")
else:
  print("<table border=1>")
  cols = [description[0] for description in curs.description]
  for col in cols:
      print(f"<td><b>{col}</b></td>")
  for row in rows:
    print("<tr>")
    #for each item in the tuple
    for item in row:
      if item == None:
        print("<td>(null)</td>")
      else:  
        print(f"<td>{item}</td>")
    print("</tr>")
  print("</table>")
print(f"<a href='/cgi-bin/list_tables.py?dbname={dbname}'><h4>Back to list of tables</h4></a>")
print("</body>")
print("</html>")
#close the connection to the database
connection.close()
