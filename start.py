import numpy as np
from subprocess import PIPE, run
import os #estrazione path immagine
import os.path
import glob

def out(command):

 result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

 return result.stdout

#with open("/home/so/Scrivania/RDC/RDC_G4/1/.csv", 'r') as file:
count=0

#path = '/home/so/Scrivania/RDC/RDC_G4/1'
for filename in os.listdir("/home/so/Scrivania/RDC/RDC_G4"):
   attimo=str("/home/so/Scrivania/RDC/RDC_G4/"+filename)
   percorso=os.path.join(attimo,'risulato_tcp.csv')
   with open(percorso, 'r') as file:
    print(file)
	
    lines=file.readlines()
  	
    #pre,ext = os.path.splitext(str(file))
    count=count+1
    f=str(str(count) +'_new'+ '.csv')
  
    path_2=str("/home/so/Scrivania/RDC/risultati_vito_tcp/"+f)
  
    new_file = open(path_2,'a')
    new_file.write("Conversations\nFilter:<No Filter>\n                                                           |       <-      | |       ->      | |     Total     |    Relative    |   Duration   |	<-		|     -> 		|\n                                                           | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |      Start     |              |	DNS		|      DNS      |\n")

    for riga in lines[5 :]:

      riga_fin=riga.split('\n')
      riga_finale= riga_fin[0]

      parola_1=riga.split(' ')
      parola_1_finale=parola_1[0].split(':')

      parola_2=riga.split('>')
      parola_2_temp=parola_2[1].split(':')
      parola_2_finale=parola_2_temp[0].split(' ')

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

      new_file.write(riga_finale+'\t'+str(eseguito_1)+'\t\t\t\t'+str(eseguito_2)+'\n')
   new_file.close()

print('FINE')


