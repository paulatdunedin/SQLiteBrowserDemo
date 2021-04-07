#!/usr/bin/python3
import sqlite3, os, re, cgi
if 'REQUEST_METHOD' in os.environ:
  data = cgi.FieldStorage()
  dbname = data["dbname"].value
  #connect to the database 
  connection = sqlite3.connect("../"+dbname)
else:
  print("This script can only run as a cgi script")
  exit()
#create a 'cursor' object to pass the query to the
#database and return the results
curs = connection.cursor()
#setup the SQL for the query and execute the query
curs.execute("SELECT name, sql FROM sqlite_master WHERE type='table'")
#fetch all the results into a list (of tuples)
rows = curs.fetchall()
# Output web server response and headers - the blank line is needed
print('''Content-type:text/html

<!doctype html>
<html>
<head>
<title>Database Tables</title>
<style>
h2 {margin:5px;}
table {border:0;border-collapse:collapse; margin:0px;}
td {border:1px solid;}
th {border:0px solid; text-align:left;}
</style>
</head>
<body>
<table>''')
#for each tuple in the  list
if len(rows)==0:
  print("Empty database<br>")
print(f'<h2>{dbname}</h2>')
print(f'<h2>Tables</h2>')
for row in rows:
  #for each item in the tuple
  table_name,sqlstring = row[0],row[1]
  print(f"<th colspan=2><a href='/cgi-bin/display_table.py?dbname={dbname}&table={table_name}'><h2>{table_name}</h2></a></th>")
  print("<tr> <td>COLUMN</td><td>DESCRIPTION</td></tr>")
  # split SQL into sections
  # remove trailing )
  sqlstring = re.sub("\)$","",sqlstring)
  # replace multiple whitespace with single space
  sqlstring = ' '.join(sqlstring.split())
  # remove opening 'create table ('
  sqlstring = sqlstring.split('(',1)[1]
  # temporarily replace commas in any (...,...,..) with ;
  sqlstring = re.sub(r"\([^\(\)]+\)", lambda x: x.group(0).replace(",",";"), sqlstring)
  # splite SQL into single lines
  sqlstrings = sqlstring.split(',')
  # for each line
  for sqlstring in sqlstrings:
    # split fieldname from attributes
    # first case handles fields with no data type
    if len(sqlstring.lstrip().split(' ',1))==1:
      field = sqlstring
      desc  = ''
    else:
      field, desc = sqlstring.lstrip().split(' ',1)
    # put the commas back in the (...;...;...) entries
    desc = re.sub(r"\([^\(\)]+\)", lambda x: x.group(0).replace(";",","), desc)
    # write to the HTML table
    print(f"<tr><td>{field}</td><td>{desc}</td></tr>")
print("</table><br>")

curs.execute("SELECT name, sql FROM sqlite_master WHERE type='view'")
#fetch all the results into a list (of tuples)
rows = curs.fetchall()
print('<h2>Views</h2>')
print('<table>')
#for each tuple in the  list
if len(rows)==0:
  print("No Views<br>")
for row in rows:
  #for each item in the tuple
  table_name,sqlstring = row[0],row[1]
  print(f"<tr><th colspan=2><a href='/cgi-bin/display_table.py?dbname={dbname}&table={table_name}'><h2>{table_name}</h2></a></th></tr>")
  print("<tr> <td>VIEW NAME</td><td>DEFINITION</td></tr>")
  # split SQL into sections
  # remove trailing )
  sqlstring = re.sub("\)$","",sqlstring)
  # replace multiple whitespace with single space
  sqlstring = ' '.join(sqlstring.split())
  # remove opening 'create table ('
  # sqlstring = sqlstring.split('as',1)[1]
  # changed line above to handle AS or as in create view...
  sqlstring = sqlstring[sqlstring.lower().index('as')+2:]
  print(f"<tr><td>{table_name}</td><td>{sqlstring}</td></tr>")
print("</table>")


print(f"<a href='/cgi-bin/sqlbrowser.py?dbname={dbname}'><h4>Open SQL query panel</h4></a>")
print("<a href='/cgi-bin/list_databases.py'><h4>Back to list of databases</h4></a>")
print("</body>")
print("</html>")
#close the connection to the database
connection.close()
