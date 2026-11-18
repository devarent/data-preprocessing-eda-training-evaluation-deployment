# 📊 MATERI SLIDE PRESENTASI VIDEO (CANVA / PPT / GOOGLE SLIDES)
## SIKLUS PENGEMBANGAN MACHINE LEARNING KEAMANAN SISTEM
### Alur: 1. Preprocessing ➔ 2. EDA ➔ 3. Training ➔ 4. Testing ➔ 5. Deployment ➔ 6. Inference

---

## SLIDE 1: JUDUL & IDENTITAS
- **Judul:** Dari Deteksi Statis Menuju Pertahanan Adaptif: Peran AI dalam Keamanan Siber
- **Studi Kasus:** Network Intrusion Detection System (NIDS) Menggunakan Random Forest Classifier
- **Alur Siklus:** Preprocessing ➔ EDA ➔ Training ➔ Testing ➔ Deployment ➔ Inference
- **Mata Kuliah:** Keamanan Siber Berbasis Sistem Cerdas
- **Presenter:** [Nama Mahasiswa] - NIM: [Nomor Induk Mahasiswa]

---

## SLIDE 2: LATAR BELAKANG & REVIEW MATERI UTS
### Mengapa Kita Membutuhkan AI dalam Keamanan Siber?
1. **Ancaman Bersifat Dinamis:** Serangan DoS SYN Flood dan Port Scanning berevolusi sangat cepat.
2. **Keterbatasan Keamanan Tradisional:** Metode *Rule-based* / *Signature-based* bersifat **statis** dan gagal mendeteksi serangan varian baru / *zero-day*.
3. **Kebutuhan Sistem Cerdas (AI/ML):** Mampu belajar dari data perilaku (*behavior-based*), beradaptasi, dan merespons ancaman secara *real-time*.
4. **Prinsip Utama:** Kualitas Data > Kuantitas Data (*Garbage In, Garbage Out*).

---

## SLIDE 3: DIAGRAM ALUR SIKLUS PROYEK (6 TAHAPAN LENGKAP)
```
+---------------------------------------------------------------------------------+
|             SIKLUS PENGEMBANGAN MACHINE LEARNING KEAMANAN SIBER                 |
+---------------------------------------------------------------------------------+
|                                                                                 |
|  [1. PREPROCESSING]                                                             |
|  - Handling Missing Values (Mean/Median Imputation)                             |
|  - Dealing with Outliers (Metode IQR: Q1, Q3, Capping)                          |
|  - Feature Extraction (byte_ratio, srv_concentration)                           |
|  - Categorical Encoding (Frequency & One-Hot Encoding)                          |
|  - Feature Selection (Correlation Matrix)                                       |
|  - Feature Scaling (StandardScaler) & Balancing (SMOTE)                         |
|                                     │                                           |
|                                     ▼                                           |
|  [2. EDA (EXPLORATORY DATA ANALYSIS)]                                           |
|  - Univariate Analysis (Histogram durasi, Bar plot label)                       |
|  - Bivariate Analysis (Box plot label vs count & diff_srv_rate)                 |
|  - Multivariate Analysis (Correlation Heatmap multi-fitur)                      |
|                                     │                                           |
|                                     ▼                                           |
|  [3. TRAINING]                                                                  |
|  - Pelatihan Random Forest Classifier (100 Trees, max_depth=12)                 |
|                                     │                                           |
|                                     ▼                                           |
|  [4. TESTING & EVALUATION]                                                      |
|  - Accuracy, Precision, Recall, Macro F1-score                                  |
|  - Confusion Matrix & Analisis Kritis: False Positive vs False Negative         |
|  - Explainable AI: Feature Importance                                           |
|                                     │                                           |
|                                     ▼                                           |
|  [5. DEPLOYMENT]                                                                |
|  - Packaging artefak model (`.pkl`, scaler, feature list)                      |
|  - Integrasi ke Next-Gen AI Firewall Engine                                     |
|                                     │                                           |
|                                     ▼                                           |
|  [6. INFERENCE]                                                                 |
|  - Menerima log paket live baru secara real-time                                |
|  - Menghasilkan prediksi & respon mitigasi adaptif otomatis (IPTables DROP)     |
+---------------------------------------------------------------------------------+
```

---

## SLIDE 4: TAHAP 1 - PREPROCESSING (PRA-PEMROSESAN DATA)
### Fondasi Kualitas Data (*Garbage In, Garbage Out*) - Adopsi Metodologi Milla Oktavia (RPubs)
1. **Visualisasi Missing Data (Metode `visdat`):**
   - Mendeteksi persebaran dan pola nilai yang hilang secara visual dengan heatmap matriks.
2. **Analisis Skewness & Handling Missing Values:**
   - **Kaidah Statistik:** Jika data memiliki kemiringan tinggi (*skewed*, $|skew| > 1$), gunakan **Median** (bukan Mean) karena lebih tahan terhadap pencilan (*robust to outliers*).
   - `src_bytes` memiliki skewness $44.61$ ➔ diimputasi dengan **Median**.
   - `dst_bytes` memiliki skewness $0.89$ ➔ diimputasi dengan **Median**.
3. **Dealing with Outliers (Metode IQR):**
   - Menghitung rentang interkuartil: $IQR = Q3 - Q1$.
   - Menentukan ambang batas: $[Q1 - 1.5 \times IQR,\ Q3 + 1.5 \times IQR]$.
   - Menerapkan *capping* (*Winsorization*) pada nilai ekstrim anomali transmisi agar bobot model tidak terdistorsi.
4. **Feature Extraction:**
   - `byte_ratio = src_bytes / (dst_bytes + 1)` (deteksi asimetri flood).
   - `srv_concentration = srv_count / (count + 1)` (deteksi konsentrasi port).
5. **Encoding Categorical Data:** Frequency Encoding & One-Hot Encoding (`protocol_type`, `service`, `flag`).
6. **Feature Selection:** Analisis korelasi terhadap label target untuk memprioritaskan fitur paling informatif.
7. **Scaling & Balancing (SMOTE):** Standarisasi Z-score dan penyeimbangan data latih (serangan siber adalah kejadian langka).

---

## SLIDE 5: TAHAP 2 - EXPLORATORY DATA ANALYSIS (EDA)
### Eksplorasi Karakteristik Data Setelah Pembersihan
1. **Univariate Analysis (Satu Variabel):**
   - Histogram distribusi `duration` (durasi koneksi).
   - Bar plot distribusi kelas target: memperlihatkan proporsi alami 70% Normal, 20% DoS, dan 10% Port Scan.
2. **Bivariate Analysis (Dua Variabel):**
   - Boxplot `label` vs `count`: DoS SYN Flood mengalami lonjakan ratusan paket per 2 detik.
   - Boxplot `label` vs `diff_srv_rate`: Port Scan memiliki rasio mendekati 1.0 (mengetuk banyak port berbeda).
3. **Multivariate Analysis (> Dua Variabel):**
   - Heatmap matriks korelasi untuk memahami relasi simultan antar seluruh fitur numerik jaringan.
   - **Pair Plot Multivariat (Adopsi Paket `psych` di R):** Visualisasi sebaran interaksi antar fitur penting (`duration`, `count`, `diff_srv_rate`, `byte_ratio`) terhadap kelas serangan.

---

## SLIDE 6: TAHAP 3 - TRAINING (PELATIHAN MODEL)
### Mengapa Memilih Random Forest Classifier?
1. **Ensemble Learning (Bagging):** Menggabungkan 100 pohon keputusan independen dengan *majority voting* untuk mereduksi *variance*.
2. **Tahan Overfitting & Noise:** Sangat kokoh dalam memproses data log jaringan yang bervariasi.
3. **Pola Non-Linear:** Handal memetakan relasi kompleks antar flag, durasi, dan byte paket.
4. **Explainable AI (XAI):** Menyediakan skor *Feature Importance* agar analis SOC mengetahui alasan logis di balik pemblokiran paket.

---

## SLIDE 7: TAHAP 4 - TESTING (PENGUJIAN & EVALUASI)
### Hasil Evaluasi (Data Test Baru 2.000 Sampel):
- **Akurasi & Macro F1-Score:** 100% pada dataset uji.
- **Confusion Matrix:** Presisi dan Recall sempurna pada ketiga kelas.

### ⚠️ Analisis Kritis: False Positive vs False Negative
| Metrik | Definisi di Cybersecurity | Dampak Terhadap Organisasi |
|---|---|---|
| **False Positive (FP)** | Trafik **Normal** dianggap **Serangan** | Menimbulkan *alert fatigue* bagi analis SOC & akses pengguna sah terganggu. Sistem tetap aman. |
| **False Negative (FN)** | **Serangan Siber** dianggap **Normal** | **FATAL! BENCANA BESAR!** Hacker berhasil masuk, server down, malware menyebar, dan pencurian data. |

> **Poin Kunci:** Di bidang Keamanan Siber, meminimalkan **False Negative (memaksimalkan Recall)** adalah prioritas mutlak!

---

## SLIDE 8: TAHAP 5 - DEPLOYMENT (PENERAPAN)
### Memindahkan Model dari Lingkungan Riset ke Produksi
- **Artefak yang Diekspor:**
  - `nids_random_forest.pkl`: Bobot model terlatih.
  - `scaler.pkl`: Objek StandardScaler untuk menstandarisasi paket baru.
  - `feature_columns.pkl`: Struktur kolom fitur yang konsisten.
  - `target_classes.pkl`: Label kategori deteksi.
- **Arsitektur Integrasi:** Model dikemas menjadi modul evaluasi real-time yang tertanam pada *Next-Gen AI Firewall / SIEM*.

---

## SLIDE 9: TAHAP 6 - INFERENCE (PERTAHANAN ADAPTIF OTONOM)
### Menguji Paket Baru Secara Real-Time & Tindakan Otonom:
1. **Paket 1 (HTTP Normal Karyawan):**
   - Hasil AI: `Normal` (Confidence 100%)
   - Respon: `[ALLOWED]` ➔ Diteruskan ke server aplikasi.
2. **Paket 2 (DoS SYN Flood Botnet):**
   - Hasil AI: `DoS_SYN_Flood` (Confidence 99%)
   - Respon: `[CRITICAL ALERT]` ➔ Eksekusi otomatis perintah firewall: `iptables -A INPUT -s [IP_Attacker] -j DROP` & aktifkan kernel SYN Cookies!
3. **Paket 3 (Port Scanning Hacker):**
   - Hasil AI: `Port_Scan` (Confidence 100%)
   - Respon: `[WARNING ALERT]` ➔ Pembatasan kecepatan koneksi (*rate-limiting*) & isolasi port privat.
4. **Paket 4 (Backup SSH Administrator):**
   - Hasil AI: `Normal` (Confidence 100%)
   - Respon: `[ALLOWED]` ➔ Koneksi aman diizinkan lewat.

---

## SLIDE 10: KESIMPULAN & INTISARI MATERI UTS
1. **AI adalah Kebutuhan:** Keamanan statis berbasis signature gagal mendeteksi ancaman baru (*zero-day*); AI memungkinkan deteksi adaptif berbasis perilaku.
2. **Siklus Data Science yang Disiplin:**
   - Preprocessing yang kokoh (imputasi missing values, penanganan outlier IQR, SMOTE) adalah kunci pencegahan *False Negative*.
   - EDA yang terarah (Univariate, Bivariate, Multivariate) memastikan kita memahami pola anomali.
3. **Pertahanan Adaptif:** AI tidak hanya mendeteksi secara pasif, melainkan menjadi agen pertahanan aktif yang memutus rantai serangan siber secara otonom!
