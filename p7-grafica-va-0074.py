import numpy as np
import matplotlib.pyplot as plt
# Jaquez Andres NC 0074
no_lista = [1,2,3,17,48]
califa_ml = [20,30,85,100,90]
califa_va = [70,90,60,90,100]
plt.plot(no_lista,califa_ml, label ="Califas_ml")
plt.plot(no_lista,califa_va, label ="Califas_VA")

plt.title("Calificaciones materias 0074")
plt.xlabel("Numero de lista")
plt.ylabel("Calificacion")

plt.legend()
plt.show()