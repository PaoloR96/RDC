import numpy as np
from subprocess import PIPE, run
import os 
import os.path
import glob

def out(command):
 result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
 return result.stdout
 
for filename in os.listdir("/home/so/Scrivania/RDC/cattura paolo/data"):
   temp=str("/home/so/Scrivania/RDC/cattura paolo/data/"+filename)
   path=os.path.join(temp,'risulato_tcp.csv')
   
   path_sni=str(temp+'/risultato_sni.csv') #crea il path di risultato_sni.csv
   
   with open(path, 'r') as file:
    print(file)
	
    lines=file.readlines()
    f=str(str(filename) +'_new_tcp'+ '.csv')
  
    path_2=str("/home/so/Scrivania/RDC/risultati_paolo_tcp/"+f)
  
    new_file = open(path_2,'a')
    new_file.write("Conversations\nFilter:<No Filter>\n                                                           |       <-      | |       ->      | |     Total     |    Relative    |   Duration   |\n                                                           | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |      Start     |              |	DNS SORGENTE, DNS DESTINAZIONE, SNI\n")

    for riga in lines[5 :]:

      riga_fin=riga.split('\n')
      riga_finale= riga_fin[0]

      parola_1=riga.split(' ')
      parola_1_finale=parola_1[0].split(':')

      parola_2=riga.split('>')
      parola_2_temp=parola_2[1].split(':')
      parola_2_finale=parola_2_temp[0].split(' ')
      
      temp_porta_dest=parola_2_temp[1].split(' ')
      porta_sorgente=parola_1_finale[1]

      indirizzo_sorgente= parola_1_finale[0]
      indirizzo_destinazione= parola_2_finale[1]

      comando_1=str('dig -x '+indirizzo_sorgente+" +short")
      eseguito=out(comando_1)
      es=eseguito.split('\n')
      eseguito_1=es[0]

      comando_2=str('dig -x '+indirizzo_destinazione+" +short")
      eseguito=out(comando_2)
      es=eseguito.split('\n')
      eseguito_2=es[0]
      
      with open(path_sni,'r') as file_sni: #apro risultato_sni.csv in lettura
       lines_2=file_sni.readlines() #leggo le righe
      
       for riga_2 in lines_2:	#per ogni riga eseguo
       
        campo_sni=''       #setto il campo_sni ad un carattere vuoto
        temp_sni=riga_2.split('\t') #divido la riga per il carattere di tabulazione
        
        if(len(temp_sni) == 6): #se temp_sni ha 6 campi (ovvero il comando sni ha dato un risultato accettabile) eseguo
        
         sorg_sni=temp_sni[1]	#salvo l'indirizzo sorgente
         dest_sni=temp_sni[2]	#salvo l'indirizzo destinazione
         porta_sorg_sni=temp_sni[3]	#salvo il numero di porta
         temp_campo_sni=temp_sni[5].split('\n')	#salvo il campo sni
        
       	 if (indirizzo_sorgente == sorg_sni and indirizzo_destinazione == dest_sni and porta_sorgente == porta_sorg_sni):	#se viene trovata una corrispondenza tra indirizzo sorgente numero di porta e indirizzo di destinazione tra i biflussi ed ilcampo sni, eseguo 
       	  																																				
       	  campo_sni=temp_campo_sni[0]	#salvo il campo sni
       	  break
       	     
      new_file.write(riga_finale+'\t'+str(eseguito_1)+',\t'+str(eseguito_2)+',\t'+campo_sni+'\n')	#scrivo sul file
   new_file.close()

print('FINE')


