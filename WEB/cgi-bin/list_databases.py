#!/usr/bin/python3
import os
# Output web server response and headers - the blank line is needed
print('''Content-type:text/html

<!doctype html>
<html>
<head>
  <title>Databases Available</title>
    <style>
      table {border:0;border-collapse:collapse;}
      td {border:1px solid}
      th {border:0px solid; text-align:left;}
    </style>
</head>
<body>
<h1>Databases Available</h1>
<ul>''')

files = [f for f in os.listdir('../') if (os.path.isfile(os.path.join('../',f)) and f.endswith('.sqlite'))]
for f in files:
  print(f"<li><a href='/cgi-bin/list_tables.py/?dbname={f}'>{f}</a>")

print('''</ul>
<h4><a href='../index.html'>Back to home page</a></h4>  
</body>
</html>''')
