import mysql.connector as msqlc
from datetime import date, datetime
import serial
import time

   
#recupération de la date et l'heure

#temps
now = datetime.now()
ctime = now.strftime("%H:%M:%S")

#date
day = date.today()
nday = day.strftime("%d-%m-%Y")


#création  communication arduino

port = #'spécifier le port ici' COMX pour windoww , devtty/... pour linux ou mac
try :
    comarduino = serial.Serial(port, 9600, timeout=1)
except Exception:
    print(" problème de connexion serie ")





#connection à la base de données
try:
    bd = msqlc.connect(
        host = "localhost",
        port = 3306 ,  #"port par défaut",
        user = "root",
        passwd = "",  #mot de passe par défaut
        database = "projet_scientifique"   #"nom de votre base de données "
    )
except Exception:
    print("erreur de connexion à la base de données")


#ID  = int(input("votre identifiant"))
#Nom = int(input('votre nom'))
#print(ID , Nom)

cursor = bd.cursor()
#query = "INSERT INTO temperature ( date, heure, valeur ) VALUES ( %s,%s ,%s )"
query_agent = "INSERT INTO Agent ( ID, Name,Prenom, Mail,Tel ,date, heure ) VALUES ( %s,%s ,%s,%s,%s,%s,%s )"



while True:

    data = comarduino.readline()
    print(data.decode('utf-8'))
    if  cursor.execute("SELECT * FROM 'Agent' where 'ID'='"+data.decode('utf-8')+"'" ) :
        val_agent = (data.decode('utf-8'),str(nday), str(ctime), )


    else :
        

 
#cursor.execute("SELECT 'Nom' FROM 'Agent' where 'ID'='"+data.decode('utf-8')+"'" ) :
    



    val = (str(nday), str(ctime), data.decode('utf-8'))
    cursor.execute(query, val)
    bd.commit()
    time.sleep(1)





