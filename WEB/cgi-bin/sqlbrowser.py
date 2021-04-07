#!/usr/bin/python3
import cgi, sqlite3, os, re

#connect to the database 
if 'REQUEST_METHOD' in os.environ:
  data = cgi.FieldStorage()
  dbname = data["dbname"].value
  connection = sqlite3.connect("../"+dbname)
else:
    print("This script can only be run as a cgi script")
    exit()

# Output web server response and headers - the blank line is needed
print('''Content-type:text/html

<!doctype html>
<html>
<head>''')
print(f"<title>SQL query panel</title>")
print('''<style>
table {border:0;border-collapse:collapse;}
td {border:1px solid}
th {border:1px solid; text-align:left;}
</style>
<script>
function goThen(query) {
  let tempQuery = query.split('\\n').join(' ');
  if (tempQuery){''')
print(f'window.location.href="/cgi-bin/execsql.py?dbname={dbname}&query="+encodeURIComponent(tempQuery)')
print('''}}
</script>
</head>
<body>''')
print(f"<h1>SQL Query Panel</h1>")
#setup the SQL for the query and execute the query
print('<textarea id="SQLquery" cols="50" rows="10"></textarea><br>')
print('<button onclick=goThen(SQLquery.value)>')
print('Execute</button>')
print(f"<a href='/cgi-bin/list_tables.py?dbname={dbname}'><h4>Back to list of tables</h4></a>")
print("</body>")
print("</html>")
#close the connection to the database
connection.close()
