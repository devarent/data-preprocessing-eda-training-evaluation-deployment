# 🎬 NASKAH LENGKAP VIDEO YOUTUBE: TUGAS BESAR KEAMANAN SIBER BERBASIS SISTEM CERDAS

> **Topik:** Dari Deteksi Statis Menuju Pertahanan Adaptif: Peran AI dalam Keamanan Siber  
> **Studi Kasus:** Network Intrusion Detection System (NIDS) untuk Deteksi Serangan DoS SYN Flood & Port Scan  
> **Model AI:** Random Forest Classifier (Supervised Ensemble Learning)  
> **Urutan Alur Siklus:** **Preprocessing ➔ EDA ➔ Training ➔ Testing ➔ Deployment ➔ Inference**  
> **Estimasi Durasi:** 12 - 15 Menit  
> **Format:** Presentasi Slide Konsep + Screen Recording Kodingan (Jupyter Notebook / Terminal)

---

## ⏱️ RUNDOWN VIDEO & TAMPILAN LAYAR

| Menit | Segmen | Tampilan Layar (Visual) | Fokus Pembahasan |
|---|---|---|---|
| **00:00 - 01:30** | Opening & Latar Belakang | Slide 1-2 + Kamera Wajah | Pengenalan diri, urgensi AI vs keamanan tradisional statis (*rule/signature-based*). |
| **01:30 - 03:00** | Alur Siklus Proyek (6 Tahap) | Slide 3 (Diagram Alur) | Menjelaskan urutan baku: Preprocessing ➔ EDA ➔ Training ➔ Testing ➔ Deployment ➔ Inference. |
| **03:00 - 05:30** | Tahap 1: Preprocessing | Notebook / Code Tahap 1 | Missing values (mean/median), Outlier IQR, Feature Extraction, Encoding, Selection, Scaling & SMOTE. |
| **05:30 - 07:30** | Tahap 2: EDA | Grafik EDA di Notebook/Plots | Univariate (Histogram), Bivariate (Boxplot label vs fitur), Multivariate (Correlation Heatmap). |
| **07:30 - 09:30** | Tahap 3: Training | Notebook / Code Tahap 3 | Pelatihan Random Forest Classifier (100 Trees), alasan pemilihan ensemble bagging. |
| **09:30 - 11:30** | Tahap 4: Testing & Evaluasi | Confusion Matrix & Metrik | Akurasi, Precision, Recall, F1, analisis kritis **False Positive vs False Negative** dalam cybersecurity. |
| **11:30 - 12:30** | Tahap 5: Deployment | Artefak `.pkl` & Struktur Folder | Pengemasan model untuk lingkungan produksi Next-Gen AI Firewall. |
| **12:30 - 14:15** | Tahap 6: Inference & Respon Adaptif | Demo Terminal / Real-time Alert | Simulasi paket live, prediksi real-time, auto-blocking IP penyerang via IPTables & rate-limiting. |
| **14:15 - 15:00** | Kesimpulan & Closing | Slide Kesimpulan + Kamera Wajah | Rekapitulasi intisari UTS dan penutup. |

---

## 🎙️ NASKAH KATA-DEMI-KATA (SPEECH SCRIPT)

### 📌 SEGMEN 1: OPENING & LATAR BELAKANG (00:00 - 01:30)
**[Visual Layar]:** Slide Pembuka (Judul Tugas, Nama Mahasiswa, NIM, Mata Kuliah).
> *"Halo semuanya! Selamat datang di video presentasi Ujian Tengah Semester mata kuliah **Keamanan Siber Berbasis Sistem Cerdas**.*
> 
> *Perkenalkan, nama saya **[Sebutkan Nama Anda]** dengan NIM **[Sebutkan NIM Anda]**.*
> 
> *Pada kesempatan kali ini, saya akan membedah salah satu implementasi nyata Machine Learning dalam keamanan sistem siber dengan topik utama: **'Dari Deteksi Statis Menuju Pertahanan Adaptif: Peran AI dalam Keamanan Siber'**.*
> 
> *Studi kasus yang kita angkat adalah pembuatan **Network Intrusion Detection System (NIDS)** berbasis model **Random Forest Classifier** untuk mendeteksi dua serangan yang sangat sering melumpuhkan server, yaitu **DoS SYN Flood** dan **Port Scanning**.*
> 
> *Mengapa kita membutuhkan AI?*
> *Ancaman siber bersifat sangat dinamis dan berevolusi setiap detik. Keterbatasan keamanan tradisional seperti firewall dan antivirus konvensional adalah metodenya yang bersifat **Rule-based** atau **Signature-based** yang statis. Mereka hanya mengenali pola serangan lama yang sudah terdaftar di database. Ketika muncul varian baru atau zero-day attack, sistem tradisional langsung gagal mendeteksinya!*
> 
> *Oleh karena itu, kita membutuhkan sistem cerdas yang mampu belajar dari pola perilaku (*behavior-based*), beradaptasi, dan merespons ancaman secara real-time."*

---

### 📌 SEGMEN 2: SIKLUS PENGEMBANGAN LENGKAP (01:30 - 03:00)
**[Visual Layar]:** Slide Diagram Alur 6 Tahapan.
> *"Dalam proyek ini, kita mengikuti alur siklus baku pengembangan Data Science dan Machine Learning secara runtut dan terstruktur, yaitu:*
> 
> *1. **Preprocessing (Pra-pemrosesan Data):** Membersihkan missing values, menangani outlier dengan metode IQR, mengekstrak fitur baru, melakukan categorical encoding, feature selection, scaling, dan mengatasi imbalanced data dengan SMOTE.*
> *2. **EDA (Exploratory Data Analysis):** Melakukan Univariate, Bivariate, dan Multivariate Analysis setelah data bersih.*
> *3. **Training:** Melatih model Random Forest pada data latih yang sudah diseimbangkan.*
> *4. **Testing:** Menguji model pada data uji baru, membedah Confusion Matrix, serta menganalisis metrik kritis False Positive vs False Negative.*
> *5. **Deployment:** Mengemas model dan artefak pipeline menjadi format produksi (`.pkl`).*
> *6. **Inference:** Menguji model pada paket lalu lintas data baru secara real-time dan mengeksekusi tindakan pertahanan adaptif otonom.*
> 
> *Sekarang, mari kita langsung buka notebook dan bedah kodingannya tahap demi tahap!"*

---

### 📌 SEGMEN 3: TAHAP 1 - PREPROCESSING DATA (03:00 - 05:30)
**[Visual Layar]:** Buka Jupyter Notebook pada bagian `Tahap 1: Preprocessing`.
> *"Kita mulai dari **Tahap 1: Preprocessing (Pra-pemrosesan Data)**.*
> *Prinsip utama di sini adalah **'Garbage In, Garbage Out'**—kualitas data jauh lebih penting daripada kuantitas data.*
> 
> *Mari kita bedah aktivitas yang kita lakukan di tahap ini dengan mengadopsi metodologi dari publikasi edukasi **Milla Oktavia (RPubs)**:*
> 
> *1. **Data Profiling & Visualisasi Missing Data (Metode `visdat`):** Pertama-tama, kita tidak hanya menghitung angka missing values, tetapi kita visualisasikan persebarannya menggunakan matriks heatmap missing values—mengadopsi fungsi paket `visdat` di R. Terlihat ada beberapa baris data kosong pada `src_bytes` dan `dst_bytes`.*
> 
> *2. **Analisis Skewness untuk Strategi Imputasi:** Mengapa kita tidak asal menggunakan rata-rata (mean)? Sesuai kaidah statistik pada referensi Milla Oktavia, kita hitung nilai **Skewness** (kemiringan distribusi) data terlebih dahulu. Ternyata `src_bytes` memiliki skewness sangat tinggi yaitu 44.61! Pada data yang menceng/skewed, imputasi terbaik adalah **Median** karena Median bersifat tahan terhadap pencilan (*robust to outliers*). Sedangkan jika simetris, baru kita gunakan Mean.*
> 
> *3. **Dealing with Outliers Menggunakan Metode IQR (Interquartile Range):** Pada data jaringan, sering terjadi anomali paket data korup atau gangguan transmisi. Kita hitung kuartil $Q1$, $Q3$, dan nilai $IQR = Q3 - Q1$. Nilai di luar batas $Q1 - 1.5 \times IQR$ dan $Q3 + 1.5 \times IQR$ kita deteksi sebagai outlier, lalu kita lakukan **capping (Winsorization)** agar nilai ekstrem tersebut tidak merusak bobot model.*
> 
> *4. **Feature Extraction (Domain Cybersecurity):** Kita ekstrak dua fitur turunan baru yang sangat krusial:*
>    - *`byte_ratio = src_bytes / (dst_bytes + 1)`: untuk mendeteksi transmisi banjir satu arah tanpa balasan server.*
>    - *`srv_concentration = srv_count / (count + 1)`: untuk mengukur apakah serangan terpusat pada satu layanan tertentu.*
> 
> *5. **Encoding Categorical Data:** Model machine learning hanya memahami angka. Kita menerapkan **Frequency Encoding** pada layanan jaringan dan **One-Hot Encoding** pada tipe protokol dan flag TCP.*
> 
> *6. **Feature Selection:** Melalui matriks korelasi, kita melihat fitur mana yang memiliki korelasi tertinggi terhadap serangan, seperti `flag_SF`, `count`, dan `dst_host_count`.*
> 
> *7. **Feature Scaling & SMOTE (Handling Imbalanced Data):** Kita standarisasi data dengan `StandardScaler`. Kemudian, karena serangan siber di dunia nyata adalah kejadian langka, kita terapkan **SMOTE** pada data training untuk menyeimbangkan kelas serangan menjadi masing-masing 5.600 sampel secara sintetis tanpa menyebabkan data leakage!"*

---

### 📌 SEGMEN 4: TAHAP 2 - EXPLORATORY DATA ANALYSIS (EDA) (05:30 - 07:30)
**[Visual Layar]:** Tampilkan grafik EDA (Univariate, Bivariate, Multivariate) di Notebook / folder `eda_plots/`.
> *"Setelah data bersih dan terstruktur, kita masuk ke **Tahap 2: EDA (Exploratory Data Analysis)**.*
> *Di sini kita melakukan tiga jenis eksplorasi:*
> 
> *1. **Univariate Analysis (Satu Variabel):** Kita melihat histogram distribusi durasi koneksi yang mayoritas berdurasi pendek, serta bar plot distribusi kelas target yang menunjukkan proporsi alami 70% Normal, 20% DoS, dan 10% Port Scan.*
> 
> *2. **Bivariate Analysis (Dua Variabel):** Kita bandingkan label serangan terhadap fitur kunci:*
>    - *Pada boxplot `label` vs `count`: terlihat jelas bahwa serangan DoS SYN Flood mengalami lonjakan drastis hingga ratusan paket per 2 detik.*
>    - *Pada boxplot `label` vs `diff_srv_rate`: serangan Port Scan memiliki rasio mendekati 1.0 karena penyerang aktif memindai banyak port berbeda secara simultan.*
> 
> *3. **Multivariate Analysis (Banyak Variabel):** Kita tampilkan **Heatmap Matriks Korelasi** untuk memahami hubungan simultan antar seluruh fitur jaringan."*

---

### 📌 SEGMEN 5: TAHAP 3 - TRAINING MODEL AI (07:30 - 09:30)
**[Visual Layar]:** Tampilkan script cell `Tahap 3: Training`.
> *"Sekarang kita masuk ke **Tahap 3: Training (Pelatihan Model)**.*
> 
> *Kasus kita adalah mendeteksi pola serangan yang sudah diketahui karakteristiknya, sehingga kita menggunakan **Supervised Classification**.*
> *Algoritma yang kita pilih adalah **Random Forest Classifier**.*
> 
> *Mengapa Random Forest?*
> *1. **Ensemble Learning (Bagging):** Menggabungkan 100 pohon keputusan acak dengan sistem voting mayoritas sehingga sangat stabil dan tahan terhadap noise data log.*
> *2. **Mampu Menangani Relasi Non-Linear:** Kombinasi port, durasi, dan byte paket adalah hubungan non-linear yang sangat cocok dipelajari oleh model berbasis pohon.*
> *3. **Tahan Overfitting:** Adanya mekanisme feature randomness mencegah pohon menghafal data train.*
> *4. **Explainable AI (XAI):** Menyediakan metrik Feature Importance agar analis SOC tahu alasan mengapa suatu paket diblokir.*
> 
> *Kita latih model pada training set yang sudah di-resample dengan SMOTE."*

---

### 📌 SEGMEN 6: TAHAP 4 - TESTING & ANALISIS KRITIS (09:30 - 11:30)
**[Visual Layar]:** Tampilkan Confusion Matrix, Classification Report, dan grafik Feature Importance.
> *"Kita lanjutkan ke **Tahap 4: Testing (Pengujian & Evaluasi Model)**.*
> 
> *Kita uji model pada 2.000 data test yang belum pernah dilihat sama sekali.*
> *Hasil evaluasi menunjukkan akurasi dan Macro F1-score mencapai 100% pada dataset uji ini.*
> 
> *Namun, dalam konteks Keamanan Siber, kita harus melakukan **Analisis Kritis: False Positive vs False Negative**!*
> 
> *- **False Positive (Alarm Palsu):** Terjadi jika lalu lintas normal karyawan diprediksi sebagai serangan. Akibatnya timbul 'alert fatigue' bagi analis SOC, namun sistem tetap aman.*
> *- Sebaliknya, **False Negative (SERANGAN LOLOS):** Terjadi jika serangan DoS atau Port Scan nyata diprediksi sebagai normal! Akibatnya? **BENCANA BESAR!** Server bisa tumbang, peretas berhasil menyusup, dan data perusahaan bisa dicuri!*
> 
> *Oleh karena itu, dalam cybersecurity, **meminimalkan False Negative (memaksimalkan nilai Recall)** untuk kelas serangan adalah prioritas nomor satu!*
> 
> *Kemudian pada grafik Feature Importance, kita melihat bahwa `count`, `duration`, dan `srv_count` adalah 3 fitur paling berpengaruh dalam keputusan AI."*

---

### 📌 SEGMEN 7: TAHAP 5 - DEPLOYMENT (11:30 - 12:30)
**[Visual Layar]:** Tampilkan folder `saved_models/` dan file `.pkl`.
> *"Setelah model terbukti handal di tahap testing, kita masuk ke **Tahap 5: Deployment (Penyebaran / Penerapan)**.*
> 
> *Model tidak boleh hanya diam di dalam notebook! Kita harus memindahkannya ke lingkungan produksi.*
> *Di sini, kita mengemas seluruh artefak yang dibutuhkan:*
> *- `nids_random_forest.pkl` untuk bobot model terlatih.*
> *- `scaler.pkl` untuk pipeline standarisasi data baru.*
> *- `feature_columns.pkl` untuk memastikan konsistensi fitur.*
> *- dan `target_classes.pkl` untuk label klasifikasi.*
> 
> *Artefak ini sekarang siap diintegrasikan ke dalam Next-Gen AI Firewall Engine atau sistem SIEM perusahaan."*

---

### 📌 SEGMEN 8: TAHAP 6 - INFERENCE & PERTAHANAN ADAPTIF (12:30 - 14:15)
**[Visual Layar]:** Jalankan script `python inference_deploy.py` di terminal atau sel notebook tahap 6. Tunjukkan log live packet.
> *"Sekarang kita tiba di tahap puncak: **Tahap 6: Inference (Inferensi Real-Time & Pertahanan Adaptif)**.*
> 
> *Di sini model yang sudah di-deploy bekerja di dunia nyata menerima paket baru:*
> 
> *1. **Paket 1 (HTTP Normal Karyawan):** AI memprediksi **Normal** (Confidence 100%). Status `[ALLOWED]`, paket diteruskan ke server web.*
> 
> *2. **Paket 2 (DoS SYN Flood Botnet):** IP asing `203.0.113.88` mengirim banjir koneksi TCP SYN tanpa balasan. AI mendeteksi **DoS_SYN_Flood** dengan keyakinan 99%!*
> *Dan inilah pertahanan adaptifnya: Sistem secara otonom mengeksekusi rule firewall: `iptables -A INPUT -s 203.0.113.88 -j DROP` dan mengaktifkan fitur SYN Cookies pada kernel server! IP penyerang diblokir seketika tanpa menunggu intervensi manual manusia!*
> 
> *3. **Paket 3 (Port Scanning):** IP `198.51.100.12` memindai banyak port privat. AI mendeteksi **Port_Scan** (Confidence 100%). Sistem langsung menerapkan **Rate Limiting** dan mengisolasi port privat.*
> 
> *4. **Paket 4 (Backup SSH Administrator):** AI memprediksi **Normal** (Confidence 100%) dan tidak memblokir akses sah.*
> 
> *Inilah esensi pertahanan adaptif: AI bertindak sebagai agen pertahanan aktif yang memutus rantai serangan siber secara otonom!"*

---

### 📌 SEGMEN 9: KESIMPULAN & PENUTUP (14:15 - 15:00)
**[Visual Layar]:** Slide Kesimpulan + Kamera Wajah Mahasiswa.
> *"Sebagai kesimpulan dari tugas ini:*
> *1. Keamanan siber tradisional berbasis tanda tangan statis sudah tidak cukup menghadapi ancaman modern; AI memungkinkan deteksi adaptif berbasis perilaku.*
> *2. Mengikuti siklus Data Science yang disiplin—dari Preprocessing yang teliti, EDA yang mendalam, Training, Testing, Deployment, hingga Inference—menjadi kunci keberhasilan sistem AI yang handal dan bebas False Negative.*
> 
> *Sekian presentasi dari saya. Seluruh kode program, dataset, dan notebook telah tersedia lengkap di repository.*
> *Terima kasih kepada Bapak/Ibu Dosen pengampu dan rekan-rekan semua. Salam teknologi dan cybersecurity!"*
