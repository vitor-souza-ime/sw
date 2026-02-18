import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro, probplot

# 1. Gerar dados sintéticos
np.random.seed(42)  # Para reprodutibilidade

# Gaussiana
gaussian_data = np.random.normal(loc=0, scale=1, size=100)

# Não gaussiana (exponencial)
non_gaussian_data = np.random.exponential(scale=1, size=100)

# 2. Teste de Shapiro-Wilk
def shapiro_test(data, name):
    W, p = shapiro(data)
    print(f"\n{name} - Shapiro-Wilk Test:")
    print(f"W = {W:.4f}, p = {p:.4f}")
    if p > 0.05:
        print("Resultado: Os dados parecem seguir uma distribuição normal")
    else:
        print("Resultado: Os dados NÃO parecem seguir uma distribuição normal")

shapiro_test(gaussian_data, "Dados Gaussianos")
shapiro_test(non_gaussian_data, "Dados Não Gaussianos")

# 3. Visualização
def plot_data(data, name):
    plt.figure(figsize=(12,5))
    
    # Histograma
    plt.subplot(1,2,1)
    plt.hist(data, bins=15, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title(f"Histograma - {name}")
    
    # Q-Q Plot
    plt.subplot(1,2,2)
    probplot(data, dist="norm", plot=plt)
    plt.title(f"Q-Q Plot - {name}")
    
    plt.show()

plot_data(gaussian_data, "Gaussianos")
plot_data(non_gaussian_data, "Não Gaussianos")
