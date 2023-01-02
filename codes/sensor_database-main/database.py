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

port = "COM6"
#try :
comarduino = serial.Serial(port, 9600, timeout=1)
#except Exception:
   # print(" problèmez de connexion serie ")





#connection à la base de données
#try:
bd = msqlc.connect(
        host = "localhost",
        port = 3306 ,  
        user = "root",
        passwd = "2468013579Faso#",  
        database = "test_initial_connection_projet_scientifique"   
    )
#except Exception:
    #print("erreur de connexion à la base de données")


cursor = bd.cursor()
query = "INSERT INTO Reccupere ( date, heure, valeur ) VALUES ( %s,%s ,%s )"



while True:

    data = comarduino.readline()
    print(data.decode('utf-8'))
    val = (str(nday), str(ctime), data.decode('utf-8'))
    cursor.execute(query, val)
    bd.commit()
    time.sleep(1)






