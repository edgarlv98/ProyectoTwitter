from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient

#Aqui se conecto a la base de datos
MONGO_HOST = ''
 
Filtro = ['']
 
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
 
 
class StreamListener(tweepy.StreamListener):    
 
    def on_connect(self):
        print("Conectado")
 
    def on_error(self, status_code):
        print('Error'
        return False
 
    def on_data(self, data):
        try:
            client = MongoClient(MONGO_HOST)

            db = client.TwitterDB

            datajson = json.loads(data)

            created_at = datajson['creado en ']

            print("Tweet guardado " + str(created_at))
            
            #Nombre de la coleccion en la que se guardan los tweets
            db.twitter_NOMBRE_DE_COLECCION.insert(datajson)
            db.Twitter.insert(datajson)
        except Exception as e:
           print(e)
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(Filtro))
streamer.filter(track=Filtro)