import pandas as pd

# Lectura del archivo CSV
data = pd.read_csv("tweets.csv", header=None, names=["fecha", "usuario", "tweet"])

import re

def limpiar_tweet(tweet):
    # Eliminación de caracteres especiales
    tweet = re.sub(r"[^a-zA-Z0-9]", " ", tweet)
    
    # Eliminación de URLs
    tweet = re.sub(r"http\S+", "", tweet)
    
    return tweet


def convertir_a_minusculas(tweet):
    return tweet.lower()

# Aplicación de las funciones de preprocesamiento
data["tweet"] = data["tweet"].apply(limpiar_tweet)
data["tweet"] = data["tweet"].apply(convertir_a_minusculas)

# Guardado del archivo CSV preprocesado
data.to_csv("tweets_preprocesados.csv", index=False)
