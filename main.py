# Utilise les bibliothèques logicielles NumPy et matplotlib our le traçage des courbes et les tableaux de valeurs
# Peut être éxécuté sans télécharements sur https://hub.gke2.mybinder.org/user/jupyterlab-jupyterlab-demo-m3g0d66j/lab sinon télécharger Python
# si possible avec Anaconda ou Miniconda
# si Python est installé, tester `pip install numpy matplotlib`
# si Miniconda est installé, tester `conda install numpy matplotlib`
# si Anaconda est installé, numpy et matplotlib seront installés par défaut

import numpy as np
import matplotlib.pyplot as plt

f = lambda x: -2*x**2 + 320 * x # Soit f la fonction tel que f: x -> -2*x² + 320 * x

El = [*range(0, 161)] # Soit El l'ensemble des nombres entiers situés dans l'intervalle [0;161[ représentant l'ensemble des largeurs possibles. El = [0;161[ ∩ N
y = np.array([f(x) for x in El]) # Soit y l'ensemble des images de x par f pour x appartentant à El. y = f(x) pour x ∈ El

plt.xlabel("f(l) = aire (m²")
plt.ylabel("largeur (m)")

plt.plot(y) # Créer le graphique correspondant aux valeurs de y c'est-à-dire à f(x) pour x appartenant à El.
#           # f(x) pour x ∈ El sur l'axe des ordonnées  et x pour x ∈ El sur celui des abscisses
plt.show() # Trace le graphique à l'écran 
plt.close()
