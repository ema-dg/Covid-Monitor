import datetime
#from pathlib import Path

#Percorso file registro

#folder = Path("z:\Scambio\")

registro = 'Z:\\Scambio\\registro.csv'

#Imposta l'ufficio
import socket
ufficio=socket.gethostname()
#ufficio=input('Nome ufficio: ')

#Inizia il loop di inserimento
while True:
	nome=input('Nome e cognome del visitatore: ')
	recapito=input('Recapito: ')
	data=str(datetime.datetime.now())
	
	#imposto la riga del file
	riga='\n'+data+';'+ufficio+';'+nome+';'+recapito
	
	file=open(registro,"a")
	file.write(riga)
	file.close()
