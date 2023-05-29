path_generale='/home/so/Scrivania/RDC/Elaborato/data'

for f in os.listdir(path_generale):
	full_path= str(path_generale +'/'+f)
	path_traffic=str(full_path+'/traffic.pcap')
	salvare_1=str(path_generale+'/'+f+'/risulato_capinfos.txt')
	
	command_1=str('capinfos '+path_traffic+' > '+salvare_1)
	os.system(command_1)
	
	salvare_2=str(path_generale+'/'+f+'/risulato_tcp.csv')
	command_2=str('tshark -r '+path_traffic+' -q -z conv,tcp > '+salvare_2)
	os.system(command_2)
	
	salvare_3=str(path_generale+'/'+f+'/risulato_udp.csv')
	command_3=str('tshark -r '+path_traffic+' -q -z conv,udp > '+salvare_3)
	os.system(command_3)

	path_dig=str(full_path+'/nslookup.log')
	#print(path_dig)
	salvare_4=str(path_generale+'/'+f+'/risultato_dig.txt')
	

	aperto= open(path_dig,'r')
	lines= aperto.readlines()
	
	command_4_1=str('tshark -r '+path_traffic+" -T fields -e frame.time_epoch -e frame.protocols -e dns.a -e dns.qry.name -Y'(dns.flags.response == 1)' > "+salvare_4 )
	os.system(command_4_1)
	
	for riga in lines:
		word= riga.split('\n')
		comando = str('dig -x' +word[0]+' | tee -a '+salvare_4)
		os.system(comando)
	aperto.close()

	salvare_5=str(path_generale+'/'+f+'/risultato_sni.csv')
	command_5=str('tshark -r '+path_traffic+" -Y 'ssl.handshake.type==1' -T fields -e frame.time_epoch -e ip.src -e ip.dst -ip.proto -e tcp.srcport -e tcp.dstport -e tls.handshake.extensions_server_name > "+salvare_5)
	os.system(command_5)
