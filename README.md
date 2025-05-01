# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi baik dalam mencetak lulusan berkualitas. Namun, akhir-akhir ini mereka menghadapi tantangan serius, yaitu tingginya angka dropout siswa. Fenomena ini berpotensi merusak citra institusi, mengurangi jumlah lulusan, dan menyebabkan kerugian finansial.

Pihak institusi ingin melakukan deteksi dini terhadap siswa yang berisiko dropout, agar dapat memberikan intervensi atau bimbingan khusus sedini mungkin. Oleh karena itu, mereka ingin membangun sistem deteksi berbasis machine learning serta menyediakan dashboard monitoring siswa agar pihak pengelola dapat memantau performa siswa secara visual.

### Permasalahan Bisnis
- Banyaknya jumlah siswa yang dropout.
- Tidak ada sistem peringatan dini untuk siswa yang akan dropout.
- Tidak ada visualisasi data visualisasi data untuk menampilkan grafik siswa yang membuat pihak pengelola tidak dapat mengambil keputusan tepat waktu

### Cakupan Proyek
- Melakukan eksplorasi dan data analisis dataset performa siswa.
- Pembuatan model machine learning untuk memprediksi peringatan dini untuk siswa yang akan dropout.
- Pembuatan business dashboard yang menampilkan grafik siswa dan prediksi risiko dropout.
- Penyusunan rekomendasi berbasis data untuk mengurangi angka dropout.

### Persiapan

Sumber data: [Link Dataset - Students Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv
)

Setup environment:
```
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

## Business Dashboard

Marital Status vs Dropout
- Mahasiswa single mendominasi jumlah dropout.

- Mahasiswa married dan divorced juga ada yang dropout, tetapi jauh lebih sedikit.

- Bisa diasumsikan bahwa status single lebih berisiko terhadap dropout, mungkin karena beban tanggung jawab berbeda atau kurang motivasi sosial. Meskipun begitu Mahasiswa yang berstatus married 50% berkemuningkan melakukan dropout.

Course vs Dropout
- Jurusan Nursing memiliki jumlah dropout tertinggi.

- Jurusan seperti Informatics Engineering, Management, dan Communication Design juga menunjukkan dropout tinggi.

- Jurusan dengan angka dropout kecil: Equiculture, Oral Hygiene, Basic Education.

 Age at Enrollment
- Dropout terbanyak terjadi di usia 18-22 tahun.

- Usia yang lebih tua (30+ tahun) relatif lebih sedikit dropout, tapi populasinya juga lebih kecil.

Daytime vs Evening Attendance
- Siswa evening class punya tingkat dropout lebih tinggi dibandingkan daytime class (rasio antara jumlah total dan dropout-nya terlihat signifikan).

- Evening class bisa jadi berisi mahasiswa pekerja atau non-tradisional yang lebih rentan karena tekanan waktu.

Debtor Status
- Siswa yang punya utang (Yes) memiliki proporsi dropout yang jauh lebih tinggi dibandingkan yang tidak punya utang.

- Ini mengindikasikan faktor keuangan adalah salah satu pemicu utama dropout.

Scholarship Holder
- Mahasiswa tanpa beasiswa menunjukkan jumlah dropout yang tinggi.

- Artinya, beasiswa membantu menurunkan angka dropout, bisa karena motivasi atau dukungan ekonomi.



## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```
source venv/bin/activate

streamlit run app.py

```

Jika tidak ingin menjalankan secara lokal, bisa mengakses versi web: [Prototype Prediksi Dropout Siswa](link disini)

## Conclusion
Mahasiswa single, tanpa beasiswa, memiliki utang, dan berkuliah malam berisiko lebih tinggi untuk dropout.

Jurusan tertentu seperti Nursing dan Informatics Engineering menunjukkan tingkat dropout sangat tinggi.

Usia muda (18–22) menjadi usia yang paling rentan terhadap dropout.

### Rekomendasi Action Items
1. Program Intervensi Dini
Bangun sistem alert berbasis ML yang mendeteksi risiko dropout dari kombinasi fitur: usia, status marital, status utang, jadwal kuliah, dan jurusan.

Mahasiswa dengan skor risiko tinggi harus mendapatkan bimbingan akademik dan psikologis lebih awal.

2. Ekspansi Beasiswa
Tawarkan lebih banyak program beasiswa untuk mahasiswa rentan (single, non-tradisional, pekerja).

Kembangkan sistem seleksi beasiswa otomatis dari skor risiko dropout.

3. Pengembangan Dashboard Interaktif
Buat dashboard yang realtime dan terhubung langsung dengan database kampus.

Tambahkan filter dinamis agar pengelola bisa melihat berdasarkan jurusan, tahun masuk, status beasiswa, dll.

4. Evaluasi Program Kelas Malam
Perlu diadakan peninjauan sistem pengajaran malam, termasuk durasi kuliah, fleksibilitas tugas, dan konseling tambahan.

Mungkin cocok diberikan model hybrid / online class.

5. Komunikasi Proaktif ke Mahasiswa Rentan
Kirimkan notifikasi (email atau via sistem akademik) ke mahasiswa dengan status rawan dropout.

Berikan info terkait layanan bantuan seperti beasiswa, konseling, atau fleksibilitas akademik.
