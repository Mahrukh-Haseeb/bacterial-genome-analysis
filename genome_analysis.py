import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


bacteria = [
    'Escherichia coli',
    'Staphylococcus aureus',
    'Klebsiella pneumoniae',
    'Bacillus subtilis',
    'Pseudomonas aeruginosa',
    'Mycobacterium tuberculosis',
    'Salmonella enterica',
    'Streptococcus pneumoniae'
]

np.random.seed(42)
genome_lengths = np.random.randint(low=1, high=11, size=len(bacteria))


df = pd.DataFrame({
    'Bacterium': bacteria,
    'Genome_Length_Mbp': genome_lengths
})

print("--- Generated DataFrame (The Data Table) ---")
print(df)


mean_length = df['Genome_Length_Mbp'].mean()
std_dev_length = df['Genome_Length_Mbp'].std()

print("\n--- Summary Statistics ---")
print(f"Mean Genome Length: {mean_length:.2f} Mbp")
print(f"Standard Deviation: {std_dev_length:.2f} Mbp")

# -----------------------------Bar Chart----------------------------------
plt.figure(figsize=(10, 6))
plt.bar(df['Bacterium'], df['Genome_Length_Mbp'], color='teal')
plt.axhline(mean_length, color='red', linestyle='--', linewidth=1, label=f'Mean ({mean_length:.2f} Mbp)')
plt.xticks(rotation=45, ha='right')
plt.title('Hypothetical Bacterial Genome Lengths')
plt.xlabel('Bacterium Species')
plt.ylabel('Genome Length (Mbp)')
plt.legend()
plt.tight_layout()
plt.show() 