# 🎁✨ **Analisis Penjualan & Prediksi Performa Produk Menggunakan Deep Learning pada Coffee Shop** ✨🎁

---

## 🎨 **Deskripsi Proyek UAP Machine Learning**

Proyek ini bertujuan untuk menciptakan **dashboard interaktif berbasis web** yang dirancang khusus untuk **Coffee Shop Maven Roasters**. Coffee shop ini beroperasi di tiga lokasi strategis di New York City. Dengan teknologi **Machine Learning (ML)** dan **Deep Learning (DL)**, dashboard ini membantu manajer dan analis data dalam:

- ☑️ **Memahami pola penjualan** melalui visualisasi data.
- 🔍 **Memprediksi performa produk** berdasarkan tren historis.
- 💡 **Memberikan insight transparan** menggunakan framework interpretasi model seperti **SHAP**.

📊 **Dataset:** Tersedia di [Kaggle](https://www.kaggle.com/datasets/ahmedabbas757/coffee-sales).

---

## 🚀 **Tujuan Utama Proyek**

1. 🔄 **Analisis Data:** Mengidentifikasi tren bulanan, distribusi penjualan, dan insight lain.
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

Proyek ini memanfaatkan kombinasi algoritma **Machine Learning** dan **Deep Learning**:

### 🎉 **Algoritma yang Digunakan**
1. **Logistic Regression** (📊 Simple dan Efektif)
2. **Decision Tree** (🕵️‍♂️ Interaktif dan Transparan)
3. **Random Forest** (🎨 Kombinasi Hebat dari Banyak Pohon)
4. **Support Vector Machine (SVM)** (⚖️ Pemisahan Optimal Antar Kelas)
5. **Neural Network (MLP)** (🤖 Model Deep Learning untuk Data Kompleks)
6. **TabNet** (🎡 Spesialisasi Data Tabular)

### 📊 **Evaluasi Model**
Model dievaluasi menggunakan:

1. **Accuracy** 🚜 Persentase prediksi benar.
2. **Confusion Matrix** 🔄 Menampilkan prediksi benar dan salah untuk tiap kelas.
3. **Classification Report** 🌐 Metrik precision, recall, dan F1-score.

---

## 🌸 **Hasil & Analisis**

🌈 **Insight Utama:**
- **Random Forest** dan **TabNet** menunjukkan performa terbaik dengan akurasi di atas **90%**.
- **Logistic Regression** efektif untuk data linear tetapi kurang optimal untuk data kompleks.

### 🎨 **Visualisasi Hasil**
#### 📊 Confusion Matrix
Berikut adalah **Confusion Matrix** hasil evaluasi untuk model **Random Forest**:
![Confusion Matrix Random Forest](https://drive.google.com/uc?id=1tzMRNrJYJt4BxMuvwrNMIpEc_o03Jjcg)

#### 🌐 Classification Report
Berikut adalah **Classification Report** hasil evaluasi untuk model **Random Forest**:
|  **Kelas**   | **Precision** | **Recall** | **F1-Score** | **Support** |
|:-------------|------------:  |---------:  |-----------:  |----------:  |
| 0            |           1   |        1   |          1   |      3390   |
| 1            |           1   |        1   |          1   |      3322   |
| 2            |           1   |        1   |          1   |      4210   |
| 3            |           1   |        1   |          1   |      5070   |
| 4            |           1   |        1   |          1   |      6789   |
| 5            |           1   |        1   |          1   |      7043   |
| accuracy     |           1   |        1   |          1   |         1   |
| macro avg    |           1   |        1   |          1   |     29824   | 
| weighted avg |           1   |        1   |          1   |     29824   |

#### 📊 Confusion Matrix
Berikut adalah **Confusion Matrix** hasil evaluasi untuk model **TabNet**:
![Confusion Matrix TabNet](https://drive.google.com/uc?id=1SYvIFdHT0tBJzetaiNUs9MmfRX_n7rmN)

#### 🌐 Classification Report
Berikut adalah **Classification Report** hasil evaluasi untuk model **TabNet**:
|  **Kelas**       | **Precision** | **Recall**|**F1-Score**|**Support**|
|------------------|---------------|-----------|------------|-----------|
| **0**            | 1.000         | 1.000     | 1.000      | 3390      |
| **1**            | 1.000         | 0.966     | 0.983      | 3322      |
| **2**            | 0.974         | 0.992     | 0.983      | 4210      |
| **3**            | 0.961         | 1.000     | 0.980      | 5070      |
| **4**            | 0.984         | 0.948     | 0.966      | 6789      |
| **5**            | 0.974         | 0.985     | 0.980      | 7043      |
| **Accuracy**     |               |           | 0.980      |           |
| **Macro Avg**    | 0.982         | 0.982     | 0.982      | 29824     |
| **Weighted Avg** | 0.980         | 0.980     | 0.980      | 29824     |

---

## 🙏 **Kesimpulan**
Proyek ini berhasil mengintegrasikan **analisis data**, **model prediksi**, dan **dashboard interaktif** untuk meningkatkan pengambilan keputusan berbasis data di Coffee Shop Maven Roasters.

💖 **Terima kasih telah membaca! Semoga proyek ini membantu Anda membuat strategi penjualan yang lebih efektif!** 🌟

