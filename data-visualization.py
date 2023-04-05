import matplotlib.pyplot as plt

# Resultados del análisis lexicon-based y machine-learning
lexicon_results = {'positivo': 20, 'negativo': 10, 'neutral': 5}
machine_learning_results = {'positivo': 25, 'negativo': 5, 'neutral': 5}

# Creación del gráfico de barras
fig, ax = plt.subplots(figsize=(8, 6))
bar_width = 0.35
opacity = 0.8
rects1 = ax.bar(lexicon_results.keys(), lexicon_results.values(), bar_width, alpha=opacity, color='b', label='Lexicon-based')
rects2 = ax.bar([x + bar_width for x in machine_learning_results.keys()], machine_learning_results.values(), bar_width, alpha=opacity, color='r', label='Machine learning')

# Configuración del gráfico
ax.set_xlabel('Sentimiento')
ax.set_ylabel('Número de textos')
ax.set_title('Comparación de análisis de sentimiento')
ax.set_xticks([x + bar_width / 2 for x in range(len(lexicon_results))])
ax.set_xticklabels(lexicon_results.keys())
ax.legend()

# Mostrado del gráfico
plt.show()
