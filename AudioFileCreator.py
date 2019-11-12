import pyodbc
import math
import os
from gtts import gTTS

conn = pyodbc.connect(
	'Driver={ODBC Driver 17 for SQL Server};'
	'Server=srvblindmarket.database.windows.net;'
	'PORT=1433;'
	'Database=bdblindmarket;'
	'UID=userblindmarket;'
	'PWD=#Gfgrupo9;'
	'Authentication=SqlPassword;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM Produto')

if not os.path.exists('files'):
    os.makedirs('files')

for row in cursor:
    print(row)

    p_completo = row[2]
    p_decimal, p_inteiro = math.modf(p_completo)

    if p_decimal > 0:
        preco = '{} e {}'.format(int(p_inteiro), int(p_decimal * 100))
    else:
        preco = '{} reais'.format(int(p_inteiro))

    info = row[1]
    info_detalhada = '{}, {}, {}'.format(row[1], preco, row[4])
    
    tts = gTTS(info, lang='pt-br')
    tts.save('files/produto_{}.mp3'.format(row[0]))

    tts = gTTS(info_detalhada, lang='pt-br')
    tts.save('files/produto_detalhado_{}.mp3'.format(row[0]))