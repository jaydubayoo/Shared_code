from push_SQL import push_sql


"""this will be assigned by the great leader KEVIN MAURO"""
user= "enter user here"
password= "enter passowrd here"



"""Shows all the Databases"""
command = "show databases;"; 
print(push_sql(command,user,password))
#if you are curiouse what is happening in push_sql(command,user,passowrd), open up 
#push_SQL



"""Shows tables in a database, In this example githubs is the database"""
command= "show tables from bitfinex"
#where bitfinex is the database
print(push_sql(command,user,password))



"""Edit 07/4/17"""
"""Once you get familiar with the structures of our database, you can collect data as such """


'Select Data (AKA table), where orderbook_BTC_USDT is the table and, * , tells mysql to choos all the data ' 
command = ' select * from bitfinex.orderbook_BTC_USDT' 
#where bitfinex is the database
#and orderbook_BTC_USDT is the table
data=push_sql(command,user,password)
#  'data' will be of type dictionary, hopefully our great leader KEVIN MAURO, can teach you how to use this



' if you want to select the first X (100 in our example) rows of the Data, we exectute '
command = ' Select * from bitfinex.orderbook_BTC_USDT LIMIT 100'
data=push_sql(command,user,password)
#again, 'data' will be of type dictionary

'if you want to select data that meets certain requirements, for example, we want data that happend after timestamp 140116800 '
' and before timestamp 141116800 '
command ='Select * from bitfinex.orderbook_BTC_USDT where timestamp >140116800 and timestamp<141116800 '
data=push_sql(command,user,password)
print ('finish')



"""here is a cheat sheet of other MYSQL Syntax"""
"""
http://cse.unl.edu/~sscott/ShowFiles/SQL/CheatSheet/SQLCheatSheet.html
"""







