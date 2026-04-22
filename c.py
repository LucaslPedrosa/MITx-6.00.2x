import numpy as np
import matplotlib.pyplot as plt
import os

files = [
    "linearEx.txt", 
    "quadraticEx.txt", 
    "cubicEx.txt", 
    "logarithmicEx.txt", 
    "exponentialEx.txt"
]

data_path = "data/"

plt.figure(figsize=(10, 6))

for file_name in files:
    full_path = os.path.join(data_path, file_name)
       
    if os.path.exists(full_path):
        data = np.loadtxt(full_path)
        label_name = file_name.replace("Ex.txt", "")
        plt.figure(label=label_name)
        plt.plot(data, label=label_name)

# Configurações do gráfico
plt.title("Comparação de Crescimento Computacional") 
plt.xlabel("Input")
plt.ylabel("Value")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.yscale('log')  # Use escala logarítmica para melhor visualização

# Se quiser ver melhor as outras, você pode limitar o eixo Y:
# plt.ylim(0, 10000) 

plt.show()
