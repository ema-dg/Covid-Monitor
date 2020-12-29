import datetime

#Percorso file registro

registro = 'Z:\\Scambio\\registro.csv'

#Imposta l'ufficio
import socket
ufficio=socket.gethostname()

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
