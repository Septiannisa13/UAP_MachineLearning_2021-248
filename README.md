# 🎁✨Analisis Penjualan dan Prediksi Performa Produk Menggunakan Deep Learning pada Coffee Shop✨🎁#

## Deskripsi Project UAP Machine Learning
Proyek ini berfokus pada pengembangan aplikasi berbasis web untuk analisis data penjualan dan prediksi performa produk di Coffee Shop Maven Roasters yang beroperasi di tiga lokasi New York City. Dashboard interaktif ini telah dirancang menggunakan Streamlit dan menggabungkan berbagai algoritma machine learning serta deep learning untuk mendukung pengambilan keputusan berbasis data. Dashboard ini cocok digunakan oleh manajer penjualan atau analis data untuk meningkatkan efisiensi operasional dan strategi pemasaran. Tujuan utama dari proyek ini meliputi:
1. Memahami pola penjualan melalui analisis data, seperti distribusi penjualan dan tren bulanan.
2. Membangun model klasifikasi untuk memprediksi performa produk berdasarkan data historis.
3. Menyediakan interpretasi hasil prediksi menggunakan framework SHAP untuk transparansi model yang telah dilatih.

***Link Dataset yang digunakan: https://www.kaggle.com/datasets/ahmedabbas757/coffee-sales***

## Langkah Instalasi
1. Membuat folder baru
2. Membuka folder tersebut di VsCode
3. Membuka terminal dengan menginputkan command "python -m venv myenv"
4. Setelah muncul myenv, menginputkan command "myenv/Scripts/activate"
5. Kemudian install pdm init dengan menginputkan command "install pdm ini"
6. Klik piliham y lalu enter terus sampai default
7. Kemudian install seluruh pustaka yang dibutuhkan
8. Kemudian masuk pada directory src dengan menginputkan command "cd src/nama directory"
9. Kemudian membuat dashboard iteraktif yang di inginkan
10. Setelah seluruh fitur sudah dibuat sesuai dengan kreativitas masing-masing. Selanjutnya jalankan file app.py menggunakan command "pdm run start run app.py" atau "pdm run streamlit run app.py"
11. Dashbard iteratif sudah siap untuk dijalankan

## Langkah Preprocessing
Langkah-langkah ini dirancang untuk memastikan kualitas data yang optimal sebelum digunakan untuk pelatihan model. Dengan preprocessing yang tepat, model machine learning dapat bekerja lebih akurat dan robust terhadap tantangan dalam data.
1. Penangann Missing Values
   - Kolom numerik: Nilai yang hilang diisi dengan rata-rata (mean) dari kolom tersebut menggunakan SimpleImputer.
   - Kolom kategori: Data kategori yang kosong dienkode sebagai kategori baru atau diubah ke format string untuk menghindari error.
2. Encoding Data Katagorikal
3. Kolom kategori dikonversi menjadi nilai numerik menggunakan LabelEncoder. Hal ini memungkinkan model machine learning memproses data kategorikal secara efektif.
4. Normalisasi Data
   Kolom numerik diskalakan menggunakan StandardScaler agar memiliki mean 0 dan standar deviasi 1. Langkah ini penting untuk memastikan model seperti Logistic Regression, Neural Network, dan SVM bekerja optimal.
5. Pemisahan Fitur dan Target
   Dataset dipisahkan menjadi kolom fitur (independen) dan target (dependen). Pengguna dapat memilih fitur dan target secara manual melalui antarmuka aplikasi.
6. Split Data untuk Pelatihan dan Pengujian
   Data dibagi menjadi data pelatihan (80%) dan data pengujian (20%) menggunakan train_test_split. Hal ini dilakukan untuk mengevaluasi performa model secara obyektif.
7. Optimasi Tabnet
    Untuk model TabNet, data diubah menjadi array NumPy agar kompatibel dengan framework PyTorch yang digunakan oleh TabNet.

