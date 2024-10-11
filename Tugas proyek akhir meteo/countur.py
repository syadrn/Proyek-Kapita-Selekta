import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.interpolate import griddata

# Load data
file_path ='Tugas Kelompok/data_kalimantan/hasil.xlsx'
df = pd.read_excel(file_path)

# Pastikan format tanggal sesuai dengan format di Excel
date = '30-06-2023'

# Ekstrak data
latitudes = df['latitude']
longitudes = df['longitude']
temperatures = df[date]
station_name = df['station_name']

# Konversi ke array numpy
lat = np.array(latitudes)
lon = np.array(longitudes)
tavg = np.array(temperatures)
stat = np.array(station_name)

# Hapus data dengan NaN pada suhu, latitude, atau longitude
valid_indices = ~np.isnan(tavg) & ~np.isnan(lat) & ~np.isnan(lon)
lat = lat[valid_indices]
lon = lon[valid_indices]
tavg = tavg[valid_indices]
stat = stat[valid_indices]

# Membuat grid untuk interpolasi
grid_x, grid_y = np.mgrid[min(lon):max(lon):100j, min(lat):max(lat):100j]

# Interpolasi data menggunakan metode 'linear' untuk mencegah error
grid_tavg = griddata((lon, lat), tavg, (grid_x, grid_y), method='linear')

# Plot data
plt.figure(figsize=(20, 8))
plt.pcolormesh(grid_x, grid_y, grid_tavg, shading='auto', cmap='coolwarm')
plt.colorbar(label='Temperature (°C)')
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f'Temperature Distribution on {date}')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

