import numpy as np
import matplotlib.pyplot as plt

def simulate_central_limit_theorem(num_samples=1000, sample_size=50, distribution_mean=0, distribution_std=1):
    # Générer les échantillons
    samples = np.random.normal(distribution_mean, distribution_std, (num_samples, sample_size))

    # Calculer les moyennes des échantillons
    sample_means = np.mean(samples, axis=1)

    # Tracer la distribution des moyennes des échantillons
    plt.figure(figsize=(10, 6))
    plt.hist(sample_means, bins=30, edgecolor='black', density=True, alpha=0.6, color='g')
    plt.title('Distribution des Moyennes des Échantillons')
    plt.xlabel('Moyenne des Échantillons')
    plt.ylabel('Densité')

    # Superposer la courbe de densité normale théorique
    x = np.linspace(min(sample_means), max(sample_means), 100)
    plt.plot(x, 1/(np.sqrt(2*np.pi/sample_size)) * np.exp(-(x-distribution_mean)**2 / (2*distribution_std**2/sample_size)), 'r', linewidth=2, label='Courbe Normale Théorique')

    # Ajouter des annotations des paramètres en dessous de l'axe des x
    plt.text(0.1, -0.1, f'Nombre d\'échantillons = {num_samples}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
    plt.text(0.1, -0.15, f'Taille des échantillons = {sample_size}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
    plt.text(0.1, -0.2, f'Moyenne = {distribution_mean}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
    plt.text(0.1, -0.25, f'Écart-type = {distribution_std}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

    plt.grid(True)
    plt.legend()
    plt.show()
