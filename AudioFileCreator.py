import pyodbc

conn = pyodbc.connect(
	'Driver={ODBC Driver 17 for SQL Server};'
	'Server=srvblindmarket.database.windows.net;'
	'PORT=1433;'
	'Database=dbblindmarket;'
	'TrustServerCertificate=no;'
	'UID=userblindmarket;'
	'PWD=#Gfgrupo9;'
	'Authentication=SqlPassword;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM bdblindmarket.Produto')

for row in cursor:
    print(row)