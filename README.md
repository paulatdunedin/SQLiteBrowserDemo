# SQLite Web Browser
Uncommenting lines 6&7 in main.sql starts a simple web server that lets you browse the database and produce documentation.

If there are errors in the cgi-scripts they will be logged in the file WEB/logfile.txt

If the Python/SQLite commands generate any errors they will be displayed in the web page.

To add the web interface to an existing repl, copy the entire WEB folder and lines 6&7 from main.sql

Notes:
1) The database must have a filename that ends .sqlite and be in the same folder as main.sql. You can change this by editing the code in the WEB folder.
2) The query panel prevents CREATE, DROP and ALTER commands.
3) Comment out line 73 in WEB/cgi-bin/execsql.py if you want to prevent the user from committing changes to the database via the web interface. 
