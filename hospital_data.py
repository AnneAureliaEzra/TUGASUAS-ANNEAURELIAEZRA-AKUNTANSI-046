import pandas as pd
import matplotlib.pyplot as plt

# Membaca file data
data = pd.read_csv('hospital_data.csv')

# Menampilkan lima baris pertama data
print("Lima baris pertama data:")
print(data.head())

# Menampilkan informasi umum tentang data
print("\nInformasi umum tentang data:")
print(data.info())

# Menampilkan ringkasan statistik tentang data numerik
print("\nRingkasan statistik tentang data:")
print(data.describe())

# Menampilkan jumlah data yang hilang (missing values) dalam setiap kolom
print("\nJumlah data yang hilang dalam setiap kolom:")
print(data.isnull().sum())

# Menampilkan jumlah unik dari setiap nilai dalam suatu kolom
print("\nJumlah nilai unik dalam setiap kolom:")
print(data.nunique())

# Menampilkan tipe data dari setiap kolom
print("\nTipe data dari setiap kolom:")
print(data.dtypes)

# Scatter Plot
plt.subplot(2, 2, 1)
plt.scatter(data['age'], data['salary'], color='blue', alpha=0.5)
plt.title('Scatter Plot')
plt.xlabel('Age')
plt.ylabel('Salary')

# Histogram
plt.subplot(2, 2, 2)
plt.hist(data['salary'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Salary')
plt.xlabel('Salary')
plt.ylabel('Frequency')

# Box Plot
plt.subplot(2, 2, 3)
plt.boxplot(data['age'].dropna())
plt.title('Box Plot of Age')
plt.ylabel('Age')

# Membuat data untuk barplot jenis kelamin
gender_data = ['male', 'female']
count_data = [len(data) // 2] * 2  # Membagi data menjadi dua kelompok

# Membuat barplot
plt.subplot(2, 2, 4)
plt.bar(gender_data, count_data, color=['blue', 'pink'])
plt.title('Barplot of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')

# Menampilkan semua visualisasi dalam satu window
plt.tight_layout()
plt.show()
