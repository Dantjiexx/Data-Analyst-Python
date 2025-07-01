import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Baca data
df = pd.read_csv('data_penjualan.csv')

# ===============================
# 1. Total Penjualan per Kota
# ===============================
penjualan_per_kota = df.groupby('Kota')['Jumlah'].sum().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(data=penjualan_per_kota, x='Kota', y='Jumlah', palette='Set2')
plt.title('Total Penjualan per Kota')
plt.ylabel('Jumlah Penjualan')
plt.xlabel('Kota')
plt.tight_layout()
plt.show()

# ===============================
# 2. Total Penjualan per Produk
# ===============================
penjualan_per_produk = df.groupby('Produk')['Jumlah'].sum().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(data=penjualan_per_produk, x='Produk', y='Jumlah', palette='Set1')
plt.title('Total Penjualan per Produk')
plt.ylabel('Jumlah Penjualan')
plt.xlabel('Produk')
plt.tight_layout()
plt.show()

# ===============================
# 3. Heatmap Penjualan (Kota vs Produk)
# ===============================
pivot = df.pivot_table(index='Kota', columns='Produk', values='Jumlah', aggfunc='sum', fill_value=0)

plt.figure(figsize=(8,5))
sns.heatmap(pivot, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Heatmap Penjualan (Kota vs Produk)')
plt.tight_layout()
plt.show()
