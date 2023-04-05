import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Lectura del archivo CSV preprocesado
data = pd.read_csv("tweets_preprocesados.csv", header=None, names=["fecha", "usuario", "tweet"])

# Definición de las características y la variable objetivo
X = data["tweet"]
y = data["sentimiento"]

# Tokenización del texto y eliminación de palabras vacías
vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform(X)

# División de los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenamiento del modelo
model = MultinomialNB()
model.fit(X_train, y_train)

# Predicción de los datos de prueba y cálculo de la precisión
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo: {:.2f}%".format(accuracy*100))

