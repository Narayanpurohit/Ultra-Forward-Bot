import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "26847865")
    API_HASH = environ.get("API_HASH", "0ef9fdd3e5f1ed49d4eb918a07b8e5d6")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7782443871:AAEC3CMt6JU_6-ZIFXSVhrUcwIRf_ztHBuY") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://1by1themes:3snVjsLPmZ9xcbd3@cluster0.uaazt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5597521952').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002140125423'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "jn_bots") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")
    PORT = environ.get('PORT', '8080')
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 