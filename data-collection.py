import tweepy
import csv

# Credenciales de acceso a la API de Twitter
consumer_key = "tu_consumer_key"
consumer_secret = "tu_consumer_secret"
access_token = "tu_access_token"
access_token_secret = "tu_access_token_secret"

# Autenticación de la API de Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creación del objeto API
api = tweepy.API(auth)

# Palabras clave a buscar en los tweets
query = ["Python", "Data Science", "Machine Learning"]

# Número máximo de tweets a obtener
max_tweets = 100

# Archivo donde se guardarán los tweets
csv_file = open("tweets.csv", "w", encoding="utf-8")
csv_writer = csv.writer(csv_file)

# Obtención de los tweets
for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en").items(max_tweets):
    csv_writer.writerow([tweet.created_at, tweet.user.screen_name, tweet.text])

# Cierre del archivo CSV
csv_file.close()
