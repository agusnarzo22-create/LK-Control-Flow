from flask import Flask, render_template, request

app = Flask(__name__)

# --- 1. HALAMAN UTAMA ---
@app.route('/')
def home():
    return render_template('home.html')

# --- 2. SEKTOR PERIKANAN (Efisiensi Solar & Profit) ---
@app.route('/marine', methods=['GET', 'POST'])
def Marine():
    hasil = None
    if request.method == 'POST':
        try:
            # Mengambil data dari form
            tangkapan = float(request.form.get('tangkapan', 0))
            harga_ikan = float(request.form.get('harga_ikan', 0))
            solar = float(request.form.get('solar', 0))
            harga_solar = 6800  # Harga solar subsidi (bisa diubah sesuai kebijakan)
            
            # Rumus: Pendapatan - Biaya Operasional
            pendapatan = tangkapan * harga_ikan
            biaya_total = solar * harga_solar
            profit = pendapatan - biaya_total
            
            hasil = {
                'pendapatan': pendapatan,
                'biaya': biaya_total,
                'profit': profit,
                'status': "Menguntungkan" if profit > 0 else "Rugi/Impas"
            }
        except ValueError:
            hasil = {'error': "Mohon masukkan angka yang valid."}
            
    return render_template('Marine.html', hasil=hasil)

# --- 3. SEKTOR PERTANIAN (ROI Panen) ---
@app.route('/agro', methods=['GET', 'POST'])
def Agro():
    hasil = None
    if request.method == 'POST':
        try:
            modal = float(request.form.get('modal', 0))
            panen_kg = float(request.form.get('panen_kg', 0))
            harga_jual = float(request.form.get('harga_jual', 0))
            
            pendapatan = panen_kg * harga_jual
            untung_bersih = pendapatan - modal
            roi = (untung_bersih / modal * 100) if modal > 0 else 0
            
            hasil = {
                'untung': untung_bersih,
                'roi': round(roi, 2),
                'pesan': "Sangat Bagus!" if roi > 20 else "Perlu Evaluasi"
            }
        except ValueError:
            hasil = {'error': "Mohon masukkan angka yang valid."}
            
    return render_template('Agro.html', hasil=hasil)

# --- 4. SEKTOR INDUSTRI (Analisis Skalabilitas & Ekspansi) ---
@app.route('/gear', methods=['GET', 'POST'])
def Gear():
    hasil = None
    if request.method == 'POST':
        try:
            # Mengambil data dari form
            modal_ekspansi = float(request.form.get('modal_ekspansi', 0)) # Harga mesin/alat baru
            margin_per_unit = float(request.form.get('margin_per_unit', 0)) # Untung bersih per produk
            tambahan_produksi = float(request.form.get('tambahan_unit', 0)) # Tambahan produk per bulan
            
            # 1. Menghitung Tambahan Keuntungan per Bulan
            profit_tambahan = tambahan_produksi * margin_per_unit
            
            # 2. Menghitung Payback Period (Berapa bulan modal kembali)
            if profit_tambahan > 0:
                payback_period = modal_ekspansi / profit_tambahan
                
                # 3. Penjelasan Logis (Decision Support)
                if payback_period <= 6:
                    saran = "Sangat Layak! Modal kembali dalam waktu singkat. Segera lakukan ekspansi."
                    status_class = "text-success"
                elif payback_period <= 12:
                    saran = "Layak. Risiko moderat, pastikan arus kas stabil selama setahun ke depan."
                    status_class = "text-warning"
                else:
                    saran = "Pertimbangkan Lagi. Waktu balik modal cukup lama, cari efisiensi biaya lain."
                    status_class = "text-danger"
                
                hasil = {
                    'profit_tambahan': profit_tambahan,
                    'payback_period': round(payback_period, 1),
                    'saran': saran,
                    'status_class': status_class
                }
            else:
                hasil = {'error': "Tambahan keuntungan harus lebih besar dari nol untuk menghitung kelayakan."}
                
        except ValueError:
            hasil = {'error': "Mohon masukkan angka yang valid."}
            
    return render_template('Gear.html', hasil=hasil)
# --- 5. SEKTOR KREATOR (Penyusutan Alat) ---
@app.route('/lens', methods=['GET', 'POST'])
def Lens():
    hasil = None
    if request.method == 'POST':
        try:
            harga_alat = float(request.form.get('harga_alat', 0))
            umur_alat = float(request.form.get('umur_alat', 0)) # dalam bulan
            proyek_per_bulan = float(request.form.get('proyek', 0))
            
            # Biaya per proyek agar modal alat kembali saat alat rusak/tua
            if umur_alat > 0 and proyek_per_bulan > 0:
                biaya_per_proyek = harga_alat / (umur_alat * proyek_per_bulan)
                hasil = {
                    'biaya_alat': round(biaya_per_proyek, 2),
                    'total_proyek': umur_alat * proyek_per_bulan
                }
            else:
                hasil = {'error': "Umur alat dan jumlah proyek tidak boleh nol."}
        except ValueError:
            hasil = {'error': "Mohon masukkan angka yang valid."}
            
    return render_template('Lens.html', hasil=hasil)

# --- 6. MORE INFO ---
@app.route('/moreinfo')
def moreinfo():
    return render_template('moreinfo.html')

if __name__ == '__main__':
    app.run(debug=True)