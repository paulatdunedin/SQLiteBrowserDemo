#!/usr/bin/python3
import cgi, sqlite3, os, re
import cgitb
cgitb.enable()
import urllib.parse

#connect to the database 
if 'REQUEST_METHOD' in os.environ:
  data = cgi.FieldStorage()
  query = data["query"].value
  dbname = data["dbname"].value
  #urllib.parse.unquote(query)
  connection = sqlite3.connect("../"+dbname)
  #turn on integrity rules for possible DDL statments
  connection.execute("PRAGMA foreign_keys = 1")
else:
    print("This script can only be run as a cgi script")
    exit()
#create a 'cursor' object to pass the query to the
#database and return the results
curs = connection.cursor()
# Output web server response and headers - the blank line is needed
print(f'''Content-type:text/html

<!doctype html>
<html>
<head>
<title>{query}</title>
<style>
table {{border:0;border-collapse:collapse;}}
td {{border:1px solid}}
th {{border:1px solid; text-align:left;}}
</style>
</head>
<body>
<h2>{query}</h2>''')
#setup the SQL for the query and execute the query
try:
  curs.execute(query)
  #fetch all the results into a list (of tuples)
  rows = curs.fetchall()
  if curs.rowcount>0:
    print(f"{curs.rowcount} row(s) affected<br>")
  elif len(rows)==0:
    print("No rows returned<br>")
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
except sqlite3.Error as err:
  print(f'<h2>Error: {err} </h2>')
print('<br><button onclick="window.history.back()">Go Back</button>')
print("</body>")
print("</html>")
#commit any changes and close the connection to the database
connection.commit()
connection.close()
