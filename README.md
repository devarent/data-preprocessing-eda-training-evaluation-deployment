
<!-- dbx-style-kit -->
<div align="center">

<img src="https://img.shields.io/badge/data-preprocessing-eda-training-evaluation-deployment-1f6feb?style=for-the-badge" alt="data-preprocessing-eda-training-evaluation-deployment" />
<img src="https://img.shields.io/badge/LANG%20Python-3178c6?style=for-the-badge" alt="LANG Python" />
<img src="https://img.shields.io/badge/STARS%200-eab308?style=for-the-badge" alt="STARS 0" />
<img src="https://img.shields.io/badge/LICENSE%20MIT-22c55e?style=for-the-badge" alt="LICENSE MIT" />

<br>

<img src="https://img.shields.io/badge/OPEN%20SOURCE-yes-22c55e?style=for-the-badge&logo=github&logoColor=white" alt="OPEN SOURCE" />
<img src="https://img.shields.io/badge/BUILT%20IN%20PUBLIC-true-6366f1?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="BUILT IN PUBLIC" />
<img src="https://img.shields.io/badge/HANDS%20ON%20LABS-52-0ea5e9?style=for-the-badge&logo=docker&logoColor=white" alt="HANDS ON LABS" />
<img src="https://img.shields.io/badge/DOCUMENTED-yes-14b8a6?style=for-the-badge&logo=markdown&logoColor=white" alt="DOCUMENTED" />

<br>

<b>Pipeline machine learning lengkap - preprocessing, EDA, training, evaluasi, dan deployment.</b>

</div>

---
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


---

## Project Governance

[![CI](https://github.com/devarent/data-preprocessing-eda-training-evaluation-deployment/actions/workflows/ci.yml/badge.svg)](https://github.com/devarent/data-preprocessing-eda-training-evaluation-deployment/actions/workflows/ci.yml)

[Contributing](CONTRIBUTING.md) | [Security Policy](SECURITY.md) | [Code of Conduct](CODE_OF_CONDUCT.md)

---

<!-- tech-stack-wall -->
## Tech Stack

<div align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />

</div>

<details>
<summary><b>Full Tech Stack Wall</b></summary>
<br>

<div align="center">

<b>Languages</b><br>
<img src="https://img.shields.io/badge/Rust-dea584?style=for-the-badge&logo=rust&logoColor=black" alt="Rust" />
<img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white" alt="Go" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" alt="Java" />
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black" alt="C" />
<img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++" />
<img src="https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white" alt="Kotlin" />
<img src="https://img.shields.io/badge/Swift-F05138?style=for-the-badge&logo=swift&logoColor=white" alt="Swift" />
<img src="https://img.shields.io/badge/Ruby-CC342D?style=for-the-badge&logo=ruby&logoColor=white" alt="Ruby" />
<img src="https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white" alt="PHP" />
<img src="https://img.shields.io/badge/Lua-2C2D72?style=for-the-badge&logo=lua&logoColor=white" alt="Lua" />
<img src="https://img.shields.io/badge/Shell-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Shell" />
<br><br>
<b>Frontend &amp; Desktop</b><br>
<img src="https://img.shields.io/badge/Vue-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=black" alt="Vue" />
<img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React" />
<img src="https://img.shields.io/badge/Svelte-FF3E00?style=for-the-badge&logo=svelte&logoColor=white" alt="Svelte" />
<img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js" />
<img src="https://img.shields.io/badge/Nuxt-00DC82?style=for-the-badge&logo=nuxtdotjs&logoColor=black" alt="Nuxt" />
<img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white" alt="Flutter" />
<img src="https://img.shields.io/badge/React%20Native-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React Native" />
<img src="https://img.shields.io/badge/Tauri-FFC131?style=for-the-badge&logo=tauri&logoColor=black" alt="Tauri" />
<img src="https://img.shields.io/badge/Electron-47848F?style=for-the-badge&logo=electron&logoColor=white" alt="Electron" />
<img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite" />
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
<img src="https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white" alt="Sass" />
<img src="https://img.shields.io/badge/Less-1D365D?style=for-the-badge&logo=less&logoColor=white" alt="Less" />
<img src="https://img.shields.io/badge/Tailwind%20CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS" />
<img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap" />
<img src="https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=threedotjs&logoColor=white" alt="Three.js" />
<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js" />
<img src="https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white" alt="jQuery" />
<br><br>
<b>Database &amp; Storage</b><br>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL" />
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
<img src="https://img.shields.io/badge/SQL%20Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white" alt="SQL Server" />
<img src="https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white" alt="Oracle" />
<img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis" />
<img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB" />
<img src="https://img.shields.io/badge/DuckDB-FFCB00?style=for-the-badge&logo=duckdb&logoColor=black" alt="DuckDB" />
<img src="https://img.shields.io/badge/ClickHouse-FFCC00?style=for-the-badge&logo=clickhouse&logoColor=black" alt="ClickHouse" />
<img src="https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=elasticsearch&logoColor=white" alt="Elasticsearch" />
<img src="https://img.shields.io/badge/Neo4j-008CC1?style=for-the-badge&logo=neo4j&logoColor=white" alt="Neo4j" />
<img src="https://img.shields.io/badge/InfluxDB-22ADF6?style=for-the-badge&logo=influxdb&logoColor=white" alt="InfluxDB" />
<img src="https://img.shields.io/badge/Cassandra-1287B1?style=for-the-badge&logo=apachecassandra&logoColor=white" alt="Cassandra" />
<img src="https://img.shields.io/badge/DynamoDB-4053D6?style=for-the-badge&logo=amazondynamodb&logoColor=white" alt="DynamoDB" />
<img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black" alt="Firebase" />
<img src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=black" alt="Supabase" />
<img src="https://img.shields.io/badge/MinIO-C72E49?style=for-the-badge&logo=minio&logoColor=white" alt="MinIO" />
<br><br>
<b>Messaging &amp; Streaming</b><br>
<img src="https://img.shields.io/badge/Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white" alt="Kafka" />
<img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white" alt="RabbitMQ" />
<img src="https://img.shields.io/badge/RocketMQ-FF6A00?style=for-the-badge&logoColor=white" alt="RocketMQ" />
<img src="https://img.shields.io/badge/Pulsar-188FFF?style=for-the-badge&logo=apachepulsar&logoColor=white" alt="Pulsar" />
<img src="https://img.shields.io/badge/Flink-E6526F?style=for-the-badge&logo=apacheflink&logoColor=white" alt="Flink" />
<br><br>
<b>DevOps &amp; Cloud Native</b><br>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes" />
<img src="https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform" />
<img src="https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white" alt="Ansible" />
<img src="https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white" alt="Jenkins" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions" />
<img src="https://img.shields.io/badge/GitLab%20CI-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white" alt="GitLab CI" />
<img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" alt="Prometheus" />
<img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" alt="Grafana" />
<img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="Nginx" />
<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white" alt="AWS" />
<img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" alt="Azure" />
<img src="https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white" alt="Cloudflare" />
<br><br>
<b>Tools &amp; Platforms</b><br>
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux" />
<img src="https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white" alt="macOS" />
<img src="https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="VS Code" />
<img src="https://img.shields.io/badge/Vim-019733?style=for-the-badge&logo=vim&logoColor=white" alt="Vim" />
<img src="https://img.shields.io/badge/Tmux-1BB91F?style=for-the-badge&logoColor=white" alt="Tmux" />
<img src="https://img.shields.io/badge/Homebrew-FAB316?style=for-the-badge&logo=homebrew&logoColor=black" alt="Homebrew" />
<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white" alt="Postman" />
<img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white" alt="Figma" />
<img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/Maven-C71A36?style=for-the-badge&logo=apachemaven&logoColor=white" alt="Maven" />
<img src="https://img.shields.io/badge/Gradle-02303A?style=for-the-badge&logo=gradle&logoColor=white" alt="Gradle" />
<img src="https://img.shields.io/badge/CMake-064F8C?style=for-the-badge&logo=cmake&logoColor=white" alt="CMake" />

</div>
</details>

<div align="center">
<sub>Hands-on engineering, built and documented in the open.</sub>
</div>