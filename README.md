# 🎁✨ **Analisis Penjualan & Prediksi Performa Produk Menggunakan Deep Learning pada Coffee Shop** ✨🎁

---

## 🎨 **Deskripsi Proyek UAP Machine Learning**

Coffee Shop Maven Roasters adalah bisnis lokal yang beroperasi di tiga lokasi strategis di New York City. Sebagai salah satu coffee shop yang sedang berkembang, Maven Roasters ingin meningkatkan pengalaman pelanggan sekaligus mengoptimalkan operasional bisnis melalui pemanfaatan teknologi modern. Dalam era persaingan bisnis yang ketat, pengambilan keputusan berbasis data menjadi kunci untuk menjaga keberlanjutan dan pertumbuhan usaha. Proyek ini bertujuan untuk menciptakan **dashboard interaktif berbasis web** yang didukung oleh teknologi **Machine Learning (ML)** dan **Deep Learning (DL)**. Dashboard ini dirancang untuk membantu manajer operasional dan analis data Maven Roasters dalam memahami dan mengelola berbagai aspek bisnis mereka, termasuk:

- ☑️ **Memahami pola penjualan** Mengidentifikasi tren penjualan bulanan untuk setiap lokasi. Dengan analisis ini, manajer dapat mengetahui waktu puncak penjualan, produk terlaris, serta pola perilaku konsumen.
- 🔍 **Memprediksi performa produk** Menggunakan model prediksi berbasis data historis, dashboard ini memungkinkan pengguna untuk memproyeksikan kinerja produk tertentu.
- 💡 **Memberikan insight transparan** Proyek ini juga memanfaatkan framework interpretasi model seperti **SHAP (SHapley Additive exPlanations)** untuk memberikan penjelasan mendalam tentang keputusan model. Hal ini penting agar rekomendasi atau prediksi yang diberikan oleh sistem dapat dipahami secara jelas oleh manajer non-teknis.

📊 **Dataset:** Tersedia di [Kaggle](https://www.kaggle.com/datasets/ahmedabbas757/coffee-sales).

---

## 🚀 **Tujuan Utama Proyek**

1. 🔄 **Analisis Data:**
  Melakukan analisis mendalam terhadap data penjualan untuk mengidentifikasi:
- Tren bulanan: Pola penjualan berdasarkan bulan yang mencakup produk mana yang paling laris pada periode tertentu.
- Distribusi penjualan antar lokasi: Membandingkan kinerja tiga cabang Coffee Shop Maven Roasters di New York City.
- Insight pelanggan: Memahami preferensi pelanggan berdasarkan kategori produk, waktu pembelian, dan pengaruh promosi.
2. ⚛️ **Prediksi:** Membangun model klasifikasi untuk memprediksi produk dengan performa tinggi.
3. 📊 **Dashboard Interaktif:** Memberikan hasil analisis dalam format visual yang mudah dipahami dan interaktif.

---

## 🔧 **Langkah Instalasi**

Ikuti langkah berikut untuk menginstal dan menjalankan aplikasi:

### 1. 🏡 **Siapkan Proyek**
- Buat folder baru untuk proyek Anda.
- Buka folder menggunakan **Visual Studio Code (VSCode)**.

### 2. 🔧 **Buat Lingkungan Virtual**
```bash
python -m venv myenv
```
Aktifkan lingkungan:
```bash
myenv\Scripts\activate
```

### 3. 📖 **Inisialisasi PDM (Python Dependency Manager)**
```bash
pdm init
```
Ikuti petunjuk dengan menekan `y` atau `enter`.

### 4. 🔍 **Instal Dependencies**
Jalankan perintah berikut untuk menginstal pustaka yang dibutuhkan:
```bash
pdm install
```

### 5. 📙 **Jalankan Aplikasi**
Navigasikan ke direktori aplikasi:
```bash
cd src/<nama-directory>
```
Jalankan aplikasi menggunakan perintah berikut:
```bash
pdm run streamlit run app.py
```

Akses aplikasi melalui URL yang muncul di terminal. 🚀

---

## 🎯 **Langkah Preprocessing**

Untuk memastikan data siap digunakan oleh model machine learning, langkah preprocessing meliputi:

### 1. ❌ **Penanganan Missing Values**
- **Numerik:** Diisi dengan rata-rata menggunakan `SimpleImputer`.
- **Kategorikal:** Diisi dengan kategori baru atau diubah menjadi string.

### 2. 🔢 **Encoding Data Kategorikal**
- Gunakan `LabelEncoder` untuk mengonversi kategori menjadi nilai numerik.

### 3. 🔄 **Normalisasi Data**
- Gunakan `StandardScaler` untuk memastikan distribusi numerik memiliki **mean=0** dan **standar deviasi=1**.

### 4. 🌐 **Pemisahan Fitur dan Target**
- Pilih fitur (independen) dan target (dependen) secara manual melalui antarmuka aplikasi.

### 5. ⚖️ **Split Data**
- Bagi data menjadi **80% data pelatihan** dan **20% data pengujian** menggunakan `train_test_split`.

### 6. 🔍 **Optimasi TabNet**
- Pastikan data dalam format **array NumPy** agar kompatibel dengan PyTorch.

---

## 🌐 **Deskripsi Model**

Proyek ini memanfaatkan kombinasi algoritma **Machine Learning (ML)** dan **Deep Learning (DL)** untuk analisis data penjualan dan prediksi performa produk. Setiap model dipilih berdasarkan kekuatan dan kemampuannya dalam menangani jenis data yang digunakan dalam proyek ini. Berikut adalah algoritma yang digunakan beserta deskripsinya:

### 🎉 **Algoritma yang Digunakan**
1. **📊 Logistic Regression** 
- Sebuah model statistik yang digunakan untuk klasifikasi biner maupun multi-kelas.
- Cocok untuk memprediksi hasil probabilistik, seperti apakah sebuah produk akan masuk dalam kategori "laku tinggi" atau "laku rendah."
- Keunggulan: Mudah diimplementasikan, cepat, dan memberikan interpretasi yang jelas tentang pengaruh variabel input terhadap hasil prediksi.
2. **🕵️‍♂️ Decision Tree** 
- Model berbasis pohon keputusan yang memecah data menjadi subset berdasarkan fitur tertentu hingga mencapai keputusan akhir.
- Cocok untuk memahami pola dalam data dan memberikan insight interpretatif.
- Keunggulan: Sederhana, transparan, dan sangat baik dalam menangkap hubungan non-linear antar fitur.
3. **🎨 Random Forest** 
- Ensambel dari banyak pohon keputusan yang digabungkan untuk meningkatkan akurasi dan stabilitas prediksi.
- Menggunakan teknik bootstrap dan random feature selection untuk menghasilkan model yang lebih tahan terhadap overfitting.
- Keunggulan: Kuat, andal, dan mampu menangani dataset dengan banyak fitur dan korelasi antar variabel.
4. **⚖️ Support Vector Machine (SVM)** 
- Model berbasis margin yang mencari hyperplane optimal untuk memisahkan kelas-kelas dalam data.
- Cocok untuk dataset dengan dimensi tinggi atau hubungan yang kompleks antar fitur.
- Keunggulan: Kemampuan generalisasi yang baik, bahkan pada dataset yang kecil namun kompleks.
5. **🤖 Neural Network (MLP)** 
- **Multi-Layer Perceptron (MLP)** adalah arsitektur neural network yang terdiri dari lapisan input, hidden, dan output.
- Cocok untuk menangani data dengan pola yang kompleks, seperti hubungan non-linear atau interaksi antar fitur yang sulit diidentifikasi oleh model tradisional.
- Keunggulan: Kemampuan belajar yang fleksibel dan adaptif dengan data yang besar dan kompleks.
6. **🎡 TabNet** 
- Model deep learning yang dirancang khusus untuk data tabular dengan memanfaatkan teknik perhatian (attention).
- Memadukan kekuatan neural network dan interpretasi yang baik pada data tabular, menjadikannya alternatif modern untuk model tradisional seperti Random Forest.
- Keunggulan: Mendukung interpretasi hasil dan sangat baik dalam menangkap hubungan antar kolom dalam data tabular.

### 📊 **Evaluasi Model**
Model dievaluasi menggunakan:

1. **🚜 Accuracy**  
- Definisi: Persentase prediksi yang benar dari total data yang diuji.
- Kegunaan: Memberikan gambaran umum tentang kinerja model, terutama pada dataset dengan distribusi kelas yang seimbang.
2. **🔄 Confusion Matrix**  
- Definisi: Matriks yang menunjukkan jumlah prediksi benar dan salah untuk setiap kelas.
- Komponen Utama:
  - True Positive (TP): Prediksi benar untuk kelas positif.
  - True Negative (TN): Prediksi benar untuk kelas negatif.
  - False Positive (FP): Prediksi salah untuk kelas positif (false alarm).
  - False Negative (FN): Prediksi salah untuk kelas negatif (missed detection).
- Kegunaan: Membantu memahami jenis kesalahan yang dilakukan model, yang sangat penting untuk aplikasi di mana kesalahan tertentu lebih kritis daripada yang lain.
3. **🌐 Classification Report** 
- Definisi: Laporan yang mencakup metrik-metrik utama seperti precision, recall, dan F1-score untuk setiap kelas.
- Komponen Utama:
  - Precision: Proporsi prediksi positif yang benar (TP / (TP + FP)).
    - Berguna untuk mengukur keandalan prediksi model, terutama dalam kasus false positive yang kritis.
  - Recall (Sensitivity): Proporsi data positif yang benar-benar terdeteksi (TP / (TP + FN)).
    - Penting untuk memastikan model tidak melewatkan data positif (false negative minimal).
  - F1-score: Rata-rata harmonis antara precision dan recall (2 * (Precision * Recall) / (Precision + Recall)).
    - Menggabungkan precision dan recall menjadi satu metrik, terutama berguna jika dataset memiliki ketidakseimbangan kelas.
- Kegunaan: Menyediakan analisis yang lebih komprehensif daripada hanya menggunakan accuracy, terutama untuk dataset dengan distribusi kelas yang tidak merata.

---

## 🌸 **Hasil & Analisis**

🌈 **Insight Utama:**
- **Random Forest** dan **TabNet** menunjukkan performa terbaik dengan akurasi di atas **90%**.
- **Logistic Regression** dan **SVM** efektif untuk data linear tetapi kurang optimal untuk data kompleks.

### 🎨 **Visualisasi Hasil**
#### 📊 Confusion Matrix
Berikut adalah **Confusion Matrix** hasil evaluasi untuk model **Random Forest**:
![Confusion Matrix Random Forest](https://drive.google.com/uc?id=1tzMRNrJYJt4BxMuvwrNMIpEc_o03Jjcg)

#### 🌐 Classification Report
Berikut adalah **Classification Report** hasil evaluasi untuk model **Random Forest**:

|  **Kelas**       | **Precision** | **Recall**|**F1-Score**|**Support**|
|------------------|---------------|-----------|------------|-----------|
| **0**            | 1.000         | 1.000     | 1.000      | 3390      |
| **1**            | 1.000         | 1.000     | 1.000      | 3322      |
| **2**            | 1.000         | 1.000     | 1.000      | 4210      |
| **3**            | 1.000         | 1.000     | 1.000      | 5070      |
| **4**            | 1.000         | 1.000     | 1.000      | 6789      |
| **5**            | 1.000         | 1.000     | 1.000      | 7043      |
| **Accuracy**     |               |           | 1.000      |           |
| **Macro Avg**    | 1.000         | 1.000     | 1.000      | 29824     |
| **Weighted Avg** | 1.000         | 1.000     | 1.000      | 29824     |


#### 📊 Confusion Matrix
Berikut adalah **Confusion Matrix** hasil evaluasi untuk model **TabNet**:
![Confusion Matrix TabNet](https://drive.google.com/uc?id=1SYvIFdHT0tBJzetaiNUs9MmfRX_n7rmN)

#### 🌐 Classification Report
Berikut adalah **Classification Report** hasil evaluasi untuk model **TabNet**:
|  **Kelas**       | **Precision** | **Recall**|**F1-Score**|**Support**|
|------------------|---------------|-----------|------------|-----------|
| **0**            | 1.000         | 1.000     | 1.000      | 3390      |
| **1**            | 1.000         | 0.966     | 0.983      | 3210      |
| **2**            | 0.974         | 0.992     | 0.983      | 4178      |
| **3**            | 0.961         | 1.000     | 0.980      | 5069      |
| **4**            | 0.984         | 0.948     | 0.966      | 6435      |
| **5**            | 0.974         | 0.985     | 0.980      | 6939      |
| **Accuracy**     |               |           | 0.980      |           |
| **Macro Avg**    | 0.982         | 0.982     | 0.982      | 29221     |
| **Weighted Avg** | 0.980         | 0.980     | 0.980      | 29221     |

---

## 🙏 **Kesimpulan**
Proyek ini berhasil mengintegrasikan **analisis data**, **model prediksi**, dan **dashboard interaktif** untuk meningkatkan pengambilan keputusan berbasis data di Coffee Shop Maven Roasters.

💖 **Terima kasih telah membaca! Semoga proyek ini memberikan inspirasi dan membantu Anda dalam mengembangkan strategi penjualan yang lebih efektif dan berorientasi pada pelanggan** 🌟

---
## 📌 **Author**
- Nama: Septiannisa Alya Shinya Purwandhani
- NIM: 202110370311248
- ✉️ alyaseptiannisa@gmail.com 
