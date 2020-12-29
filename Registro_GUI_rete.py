import datetime

#Percorso file registro

registro = 'Z:\\Scambio\\registro.csv'

#Imposta l'ufficio
import socket
ufficio=socket.gethostname()

#Definisci interfaccia grafica
import PySimpleGUI as GUI

layout = [[GUI.Text("Cognome e Nome visitatore")],
          [GUI.Input(key='-inputname-',do_not_clear=False)],
          [GUI.Text("Recapito")],
          [GUI.Input(key='-inputrecapito-',do_not_clear=False)],
          [GUI.Button('OK'), GUI.Button('Esci')]]
window = GUI.Window('Monitoraggio visitatori',layout)

#Inizia il loop di inserimento
while True:
        event, values = window.read()
        print (event,values)
        
        if event == GUI.WINDOW_CLOSED or event == 'Esci':
                break
        
        if event == 'OK':
	        #imposto la riga del file
                riga = '\n'+str(datetime.datetime.now())+';'+ufficio+';'+values['-inputname-']+';'+values['-inputrecapito-']
                #scrivo la riga
                file=open(registro,"a")
                file.write(riga)
                file.close()
        window['-inputname-'].SetFocus(force=True)
        

                          
window.close()
