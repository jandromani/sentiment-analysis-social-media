import pandas as pd

# Lectura del archivo CSV preprocesado
data = pd.read_csv("tweets_preprocesados.csv", header=None, names=["fecha", "usuario", "tweet"])

from textblob import TextBlob

def calcular_polaridad(tweet):
    return TextBlob(tweet).sentiment.polarity


    # Cálculo de la polaridad de cada tweet
    data["polaridad"] = data["tweet"].apply(calcular_polaridad)

    # Agregación de una nueva columna con el sentimiento
    data["sentimiento"] = ""
    data.loc[data["polaridad"] > 0, "sentimiento"] = "positivo"
    data.loc[data["polaridad"] < 0, "sentimiento"] = "negativo"
    data.loc[data["polaridad"] == 0, "sentimiento"] = "neutral"
