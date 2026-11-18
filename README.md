# Praktikum Machine Learning untuk Keamanan Sistem
## Tugas Besar Video YouTube - Keamanan Siber Berbasis Sistem Cerdas
### Tema: Dari Deteksi Statis Menuju Pertahanan Adaptif: Peran AI dalam Keamanan Siber

Proyek ini mengimplementasikan sistem deteksi intrusi jaringan (**Network Intrusion Detection System / NIDS**) cerdas menggunakan algoritma **Random Forest Classifier**. Sistem ini mampu mendeteksi lalu lintas jaringan normal, serangan **DoS SYN Flood**, dan pemindaian port (**Port Scanning**), serta mengeksekusi mitigasi pertahanan adaptif secara otomatis.

---

## 📁 Struktur Direktori & File Proyek

```text
├── generate_dataset.py            # Modul 1: Ingestion & Pembuatan Dataset Network Traffic (Pilar #1)
├── network_traffic_dataset.csv    # Dataset mentah 10.000 sampel trafik jaringan
├── train_nids_model.py            # Modul 2-7: Preprocessing, SMOTE, Training, Evaluasi & Export Model
├── inference_deploy.py            # Modul Deployment: Simulasi Live Traffic & Respon Pertahanan Adaptif
├── nids_machine_learning_security.ipynb # Jupyter Notebook interaktif lengkap untuk presentasi/video
├── NASKAH_VIDEO_YOUTUBE.md        # Panduan naskah rekaman video YouTube kata-demi-kata (durasi ~12-15 menit)
├── SLIDE_PRESENTASI_UTS.md        # Ringkasan materi 10 slide presentasi (bisa dicopy ke PPT/Canva)
├── eda_plots/                     # Folder grafik hasil visualisasi EDA & evaluasi
│   ├── 01_class_distribution.png        # Distribusi imbalanced data kelas target
│   ├── 02_attack_behavior_patterns.png  # Pola fitur penting (count, diff_srv_rate, dst_bytes)
│   ├── 03_confusion_matrix.png          # Confusion Matrix hasil testing model
│   └── 04_feature_importance.png        # Top fitur paling berpengaruh (Explainable AI)
└── saved_models/                  # Folder artefak model hasil training
    ├── nids_random_forest.pkl           # Bobot model Random Forest Classifier
    ├── scaler.pkl                       # Objek StandardScaler untuk normalisasi
    ├── feature_columns.pkl              # Daftar kolom hasil One-Hot Encoding
    └── target_classes.pkl               # Daftar nama kelas target
```

---

## 🚀 Cara Menjalankan Program

### 1. Prasyarat Lingkungan
Pastikan Python sudah terpasang beserta pustaka yang dibutuhkan:
```bash
pip install pandas scikit-learn seaborn matplotlib imbalanced-learn joblib
```

### 2. Generate Dataset (Pilar #1)
```bash
python generate_dataset.py
```

### 3. Pelatihan Model & Evaluasi (Pilar #2 & #3)
Menjalankan data cleaning, feature engineering, normalisasi, SMOTE, training Random Forest, dan menghasilkan grafik evaluasi:
```bash
python train_nids_model.py
```

### 4. Menjalankan Simulasi Pertahanan Adaptif (Inference / Deploy)
Menguji model terhadap data paket baru secara real-time dan melihat aksi mitigasi firewall otomatis:
```bash
python inference_deploy.py
```

### 5. Menjalankan Jupyter Notebook dari CMD (Tanpa Membuka Browser)

Proyek ini memiliki virtual environment di folder `.venv`. Aktifkan dulu lalu jalankan notebook secara headless:

```bat
:: Windows CMD - aktifkan virtual environment
.venv\Scripts\activate

:: Eksekusi seluruh notebook dari awal sampai akhir (in-place)
jupyter nbconvert --to notebook --execute --inplace nids_machine_learning_security.ipynb

:: Alternatif: jalankan semua cell dan hasilkan file .ipynb baru
jupyter nbconvert --to notebook --execute nids_machine_learning_security.ipynb --output nids_machine_learning_security_executed.ipynb

:: Atau buka notebook interaktif di browser
jupyter notebook nids_machine_learning_security.ipynb
```

Semua grafik EDA dan evaluasi otomatis disimpan sebagai file PNG di folder `eda_plots/` (misal `00_missing_data_visdat.png`, `03_pairplot_psych.png`, `04_confusion_matrix.png`, `05_feature_importance.png`), dan artefak model `.pkl` diperbarui di `saved_models/` setiap kali notebook dijalankan ulang.

Untuk menonaktifkan environment kembali ke CMD:
```bat
deactivate
```

---

## 🎯 Hubungan dengan Materi Kuliah UTS

| Konsep UTS | Implementasi dalam Koding |
|---|---|
| **Latar Belakang & Masalah** | Serangan DoS SYN Flood dan Port Scan menipu firewall statis; diatasi dengan deteksi perilaku berbasis Machine Learning. |
| **Pilar #1: Data adalah Bahan Bakar** | Menggunakan fitur Network Traffic NetFlow: durasi, TCP flag (`SF`, `S0`), ukuran byte, frekuensi koneksi (`count`). |
| **Pilar #2: Preprocessing (Garbage In, Garbage Out)** | Pembersihan data, pembuatan fitur baru (`byte_ratio`, `srv_concentration`), One-Hot Encoding, StandardScaler, dan penanganan imbalanced data dengan **SMOTE**. |
| **Pilar #3: Model AI (Mesin Deteksi)** | **Random Forest Classifier** (Supervised Ensemble Learning) dengan 100 pohon keputusan dan analisis **Feature Importance** (Explainable AI). |
| **Evaluasi Kritis** | Analisis dampak **False Positive (Alert Fatigue)** vs **False Negative (Bencana Fatal / Serangan Lolos)**. |
| **Pertahanan Adaptif** | `inference_deploy.py` secara otomatis menjalankan blokir IP via IPTables dan rate-limiting saat mendeteksi anomali. |

