import math
import random
from datetime import datetime
import requests

# 1. Cek status code dan isi dari halaman GitHub
try:
    url = "https://github.com/agusnarzo22-create/LK-Control-Flow"
    response = requests.get(url)
    print("Status Code:", response.status_code)
except Exception as e:
    print("Terjadi kesalahan koneksi:", e)

# 2. Math dan Random
print("Akar 16:", math.sqrt(16))
print("Nilai Pi:", math.pi)
angka = random.randint(1, 10)
print("Angka acak:", angka)

# 3. Waktu
sekarang = datetime.now()
print("Waktu sekarang:", sekarang)

# 4. Materi Control Flow
nilai = random.randint(50, 100)
print("Nilai:", nilai)
if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")

# Bagian ini hanya untuk Web Server Django, bukan script biasa
# from django.shortcuts import render
# def home(request):
#     return render(request, 'home.html')
