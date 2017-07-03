import urllib2
import json

def removeDatabase(dbName,user,password):
	push_sql("drop database if exists "+dbName+";",user,password);

def push_sql(command,user,password): 

	user=str(user)
	password=str(password)
	# communicating with the sql
	commandArray=command.split(" ");
	output=""
	for i in commandArray:
		output=output+i+"+";


	output=output[0:len(output)-1]


	print ("push output", output)
	url="http://kevin.zapto.org/sqlCommand?sqlCommand="+output+"&user="+user+"&password="+password ;
	response=urllib2.urlopen(url).read();
	response=json.loads(response);

	
	if(response["error"]==True):
			print(response);
			raise Exception("What the fuck")
	return response
	#return; #specified to Kevin's website

