# 🎁✨ Analisis Penjualan dan Prediksi Performa Produk Menggunakan Deep Learning pada Coffee Shop ✨🎁

## Deskripsi Project UAP Machine Learning
Proyek ini berfokus pada pengembangan aplikasi berbasis web untuk analisis data penjualan dan prediksi performa produk di **Coffee Shop Maven Roasters** yang beroperasi di tiga lokasi New York City. Dashboard interaktif ini dirancang menggunakan Streamlit dan mengintegrasikan berbagai algoritma machine learning serta deep learning untuk mendukung pengambilan keputusan berbasis data. Dashboard ini dirancang khusus untuk manajer penjualan atau analis data guna meningkatkan efisiensi operasional dan strategi pemasaran.

### Tujuan Proyek
1. **Memahami pola penjualan** melalui analisis data, seperti distribusi penjualan dan tren bulanan.
2. **Membangun model klasifikasi** untuk memprediksi performa produk berdasarkan data historis.
3. **Menyediakan interpretasi hasil prediksi** menggunakan framework SHAP untuk transparansi model yang telah dilatih.

Dataset yang digunakan dapat ditemukan di [Kaggle](https://www.kaggle.com/datasets/ahmedabbas757/coffee-sales).

---

## 🔹 Langkah Instalasi
Ikuti langkah-langkah berikut untuk menginstal dan menjalankan aplikasi:

1. **Buat folder baru**
   Buat direktori proyek baru di perangkat Anda.

2. **Buka folder di Visual Studio Code (VSCode)**
   Buka direktori menggunakan VSCode untuk kemudahan pengembangan.

3. **Buat lingkungan virtual**
   Jalankan perintah berikut di terminal:
   ```bash
   python -m venv myenv
   ```

4. **Aktifkan lingkungan virtual**
   ```bash
   myenv\Scripts\activate
   ```

5. **Inisialisasi PDM (Python Dependency Manager)**
   ```bash
   pdm init
   ```
   Pilih opsi default dengan menekan `y` atau `enter` hingga selesai.

6. **Instal pustaka yang dibutuhkan**
   Jalankan perintah berikut untuk menginstal semua dependencies:
   ```bash
   pdm install
   ```

7. **Masuk ke direktori aplikasi**
   ```bash
   cd src/<nama-directory>
   ```

8. **Jalankan aplikasi**
   Jalankan file `app.py` menggunakan perintah berikut:
   ```bash
   pdm run streamlit run app.py
   ```

Aplikasi dashboard interaktif kini siap digunakan. Akses melalui URL yang muncul di terminal Anda.

---

## 🔹 Langkah Preprocessing

Agar model machine learning dapat bekerja secara optimal, data harus melalui proses preprocessing yang mencakup langkah-langkah berikut:

### 1. Penanganan Missing Values
- **Kolom numerik:** Nilai yang hilang diisi dengan rata-rata (mean) menggunakan `SimpleImputer`.
- **Kolom kategori:** Data kategori yang kosong dienkode sebagai kategori baru atau diubah menjadi string untuk menghindari error.

### 2. Encoding Data Kategorikal
- Kolom kategori dikonversi menjadi nilai numerik menggunakan `LabelEncoder`, memungkinkan model machine learning memproses data kategorikal secara efektif.

### 3. Normalisasi Data
- Kolom numerik diskalakan menggunakan `StandardScaler` agar memiliki mean 0 dan standar deviasi 1. Langkah ini penting untuk model seperti Logistic Regression, Neural Network, dan SVM.

### 4. Pemisahan Fitur dan Target
- Dataset dipisahkan menjadi kolom fitur (independen) dan target (dependen). Pengguna dapat memilih fitur dan target secara manual melalui antarmuka aplikasi.

### 5. Split Data untuk Pelatihan dan Pengujian
- Data dibagi menjadi data pelatihan (80%) dan data pengujian (20%) menggunakan `train_test_split` untuk mengevaluasi performa model secara obyektif.

### 6. Optimasi TabNet
- Data diubah menjadi array NumPy agar kompatibel dengan framework PyTorch yang digunakan oleh TabNet.

Preprocessing yang tepat memastikan kualitas data yang optimal, meningkatkan akurasi, dan ketahanan model terhadap tantangan data.

---

## 🔹 Deskripsi Model
Proyek ini menggunakan berbagai algoritma machine learning dan deep learning, antara lain:

1. **Logistic Regression**
   - Model dasar untuk klasifikasi yang bekerja baik pada data dengan distribusi linear.

2. **Decision Tree**
   - Model non-linear yang memberikan representasi keputusan yang mudah dipahami.

3. **Random Forest**
   - Teknik ensemble yang menggabungkan banyak decision tree untuk meningkatkan akurasi prediksi dan mengurangi overfitting.

4. **Support Vector Machine (SVM)**
   - Algoritma yang membangun hyperplane untuk memisahkan kelas-kelas dalam data secara optimal.

5. **Neural Network (MLP)**
   - Model deep learning dengan lapisan tersembunyi untuk menangani kompleksitas data yang tinggi.

6. **TabNet**
   - Model deep learning khusus untuk data tabular yang memanfaatkan sparsity dan memberikan interpretasi bawaan terhadap fitur.

### Evaluasi Performa Model
Model dievaluasi menggunakan beberapa metrik berikut:

1. **Accuracy**
   - Persentase data yang diprediksi dengan benar.

2. **Confusion Matrix**
   - Matriks yang menampilkan prediksi benar dan salah untuk setiap kelas.

3. **Classification Report**
   - Tabel yang mencakup precision, recall, dan F1-score untuk setiap kelas.

---

## 🔹 Hasil dan Analisis
Hasil evaluasi menunjukkan bahwa **Random Forest** dan **TabNet** memberikan akurasi tertinggi di antara semua model yang digunakan. Berikut adalah temuan utama:

1. **Akurasi Model**
   - Random Forest dan TabNet konsisten memberikan akurasi di atas 90% pada dataset pengujian.
   - Logistic Regression bekerja baik pada data dengan distribusi linear, namun kurang optimal pada data kompleks.

2. **Visualisasi Confusion Matrix**
   - Confusion Matrix memberikan gambaran tentang seberapa baik model mengklasifikasikan data, termasuk kesalahan prediksi pada setiap kelas.

3. **Grafik dan Tabel Evaluasi**
   - Classification Report menyajikan metrik evaluasi secara rinci, membantu pengguna memahami kekuatan dan kelemahan model.

---

🙌👋🙏Sekian Terimakasih🙏👋🙌
Semoga proyek ini membantu Anda dalam menganalisis data penjualan dan membuat keputusan yang lebih baik berdasarkan data😊

