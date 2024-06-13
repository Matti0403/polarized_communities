import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carica il file in un DataFrame
df = pd.read_csv('output.txt', header=None, names=['dataset', 'algoritmi', 'polarità', 'runtime', 'S1', 'S2'])

# Rimuove spazi bianchi iniziali e finali nelle colonne di stringhe
df['dataset'] = df['dataset'].str.strip()
df['algoritmi'] = df['algoritmi'].str.strip()

# Seleziona solo le colonne numeriche per il calcolo delle medie
numerical_columns = ['polarità', 'runtime']
summary = df.groupby(['dataset', 'algoritmi'])[numerical_columns].mean().reset_index()

# Imposta lo stile di Seaborn per i plot
sns.set(style="darkgrid")

# Crea una figura e assi per i due plot
fig, axes = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Plot polarità
sns.barplot(data=summary, x='dataset', y='polarità', hue='algoritmi', ax=axes[0])
axes[0].set_title('')
axes[0].set_ylabel('polarità')
axes[0].set_xlabel('')

# Plot runtime
sns.barplot(data=summary, x='dataset', y='runtime', hue='algoritmi', ax=axes[1])
axes[1].set_title('')
axes[1].set_ylabel('runtime')
axes[1].set_xlabel('')
axes[1].set_yscale('log')

# Ruota le etichette dell'asse x
for ax in axes:
    for label in ax.get_xticklabels():
        label.set_rotation(45)
        label.set_horizontalalignment('right')

# Imposta lo zoom sul plot relativo al runtime
axes[1].set_ylim(0, 1000)  # Imposta i limiti sull'asse y


# Aggiunge una legenda comune
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=len(summary['algoritmi'].unique()))

# Regola i layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Salva la figura in un file
plt.savefig('plot_valori_medi.png')

# Mostra i plot
plt.show()