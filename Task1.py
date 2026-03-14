import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)


import math

print(math.sqrt(16))
print(math.pi)  

import random

angka = random.randint(1, 10)
print("Angka acak:", angka)

from datetime import datetime

sekarang = datetime.now()
print("Waktu sekarang:", sekarang)

import random

nilai = random.randint(50, 100)
print("Nilai:", nilai)

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")
