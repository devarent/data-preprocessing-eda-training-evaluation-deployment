"""
========================================================================================
SIKLUS PENGEMBANGAN MACHINE LEARNING KEAMANAN SIBER
Topik: Dari Deteksi Statis Menuju Pertahanan Adaptif (Review Materi UTS)
Studi Kasus: Network Intrusion Detection System (NIDS) - DoS & Port Scan
Referensi Tambahan: Metodologi EDA & Data Preprocessing (Milla Oktavia, RPubs)

URUTAN SIKLUS PENGEMBANGAN (6 TAHAPAN LENGKAP):
  1. Preprocessing (Pra-pemrosesan Data)
     - Data Profiling & Skewness Analysis (Justifikasi Akademis Mean vs Median)
     - Visualisasi Missing Data (Adopsi pola paket 'visdat')
     - Handling Missing Values (Imputasi berbasis Skewness)
     - Dealing with Outliers (Metode IQR: Q1, Q3, Capping / Winsorization)
     - Feature Extraction (Domain Cyber: byte_ratio, srv_concentration)
     - Categorical Encoding (Frequency Encoding & One-Hot Encoding)
     - Feature Selection (Analisis Korelasi & Multikolinearitas)
     - Feature Scaling (StandardScaler) & Balancing (SMOTE)
  2. EDA (Exploratory Data Analysis)
     - Univariate Analysis (Histogram & Bar Plot)
     - Bivariate Analysis (Box Plot pola serangan)
     - Multivariate Analysis (Correlation Heatmap & Pair Plot ala paket 'psych')
  3. Training (Pelatihan Model Random Forest)
  4. Testing (Evaluasi Model, Confusion Matrix, Analisis Kritis FP vs FN)
  5. Deployment (Penyimpanan Artefak Model untuk Produksi)
  6. Inference (Simulasi Real-Time & Pertahanan Adaptif Otonom)
========================================================================================
"""

import os
import warnings
warnings.filterwarnings('ignore')
import joblib
import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score
from imblearn.over_sampling import SMOTE

def main():
    os.makedirs('eda_plots', exist_ok=True)
    os.makedirs('saved_models', exist_ok=True)

    print("=" * 85)
    print("SIKLUS LENGKAP MACHINE LEARNING UNTUK KEAMANAN SISTEM")
    print("Alur: 1.Preprocessing -> 2.EDA -> 3.Training -> 4.Testing -> 5.Deployment -> 6.Inference")
    print("Adopsi Metodologi: EDA & Data Preprocessing (Milla Oktavia, RPubs)")
    print("=" * 85)

    # Ingestion Data Awal (Pilar #1: Data adalah Bahan Bakar)
    dataset_path = 'network_traffic_dataset.csv'
    if not os.path.exists(dataset_path):
        import generate_dataset
        generate_dataset.generate_network_data()

    data = pd.read_csv(dataset_path)
    print(f"\n[INFO DATASET] Memuat raw dataset: {data.shape[0]} baris, {data.shape[1]} kolom")
    print(data.head(3))

    # =========================================================================
    # TAHAP 1: PREPROCESSING (PRA-PEMROSESAN DATA)
    # =========================================================================
    print("\n" + "=" * 50)
    print("TAHAP 1: PREPROCESSING (PRA-PEMROSESAN DATA)")
    print("=" * 50)

    # 1.1 Data Profiling & Visualisasi Missing Data (Konsep visdat ala Milla Oktavia)
    print("\n[1.1] Visualisasi & Profiling Missing Values (Metode 'visdat'):")
    missing_counts = data.isnull().sum()
    print("      - Ringkasan Missing Values per Kolom:")
    for col, count in missing_counts[missing_counts > 0].items():
        print(f"        * {col:<15}: {count} baris kosong ({count/len(data)*100:.2f}%)")

    # Simpan Heatmap Visualisasi Missing Data (ala paket visdat di R)
    plt.figure(figsize=(10, 4))
    sns.heatmap(data.isnull(), cbar=False, cmap='YlOrRd', yticklabels=False)
    plt.title("Visualisasi Missing Data Matrix (Adopsi Paket 'visdat')", fontsize=12, fontweight='bold')
    plt.xlabel('Kolom Fitur Jaringan')
    plt.ylabel('Posisi Sampel')
    plt.tight_layout()
    plt.savefig('eda_plots/00_missing_data_visdat.png', dpi=300)
    plt.close()
    print("      [✓] Visualisasi matriks missing values tersimpan di 'eda_plots/00_missing_data_visdat.png'")

    # 1.2 Skewness Analysis & Imputasi Berbasis Distribusi (Metode Milla Oktavia)
    print("\n[1.2] Analisis Skewness untuk Memilih Strategi Imputasi:")
    # Prinsip Milla Oktavia: Jika distribusi miring (skewed, |skew| > 1), gunakan MEDIAN. Jika simetris, gunakan MEAN.
    skew_src = data['src_bytes'].skew()
    skew_dst = data['dst_bytes'].skew()
    print(f"      - Skewness 'src_bytes': {skew_src:.2f} (Distribusi Sangat Miring/Skewed)")
    print(f"      - Skewness 'dst_bytes': {skew_dst:.2f} (Distribusi Miring/Skewed)")

    median_src = data['src_bytes'].median()
    median_dst = data['dst_bytes'].median()
    data['src_bytes'] = data['src_bytes'].fillna(median_src)
    data['dst_bytes'] = data['dst_bytes'].fillna(median_dst)
    print(f"      - Imputasi 'src_bytes' dengan Median ({median_src:.2f}) karena sifat data skewed (Robust to outliers).")
    print(f"      - Imputasi 'dst_bytes' dengan Median ({median_dst:.2f}) agar tidak terdistorsi pencilan.")
    print(f"      - Total sisa missing values setelah imputasi: {data.isnull().sum().sum()}")

    # 1.3 Dealing with Outliers (Metode Interquartile Range - IQR)
    print("\n[1.3] Dealing with Outliers (Metode IQR):")
    Q1 = data['src_bytes'].quantile(0.25)
    Q3 = data['src_bytes'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = data[(data['src_bytes'] < lower_bound) | (data['src_bytes'] > upper_bound)]
    print(f"      - Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")
    print(f"      - Ambang Batas: [{lower_bound:.2f} s/d {upper_bound:.2f}]")
    print(f"      - Outlier ekstrem terdeteksi: {len(outliers)} baris")
    
    # Capping (Winsorization) nilai ekstrem agar model tidak bias terhadap noise korup
    data['src_bytes'] = np.clip(data['src_bytes'], lower_bound, upper_bound)
    print("      - Outlier ekstrem berhasil di-capping dalam rentang batas wajar [lower, upper].")

    # 1.4 Feature Extraction (Feature Engineering Domain Cybersecurity)
    print("\n[1.4] Feature Extraction (Ekstraksi Fitur Domain Keamanan):")
    data['byte_ratio'] = data['src_bytes'] / (data['dst_bytes'] + 1.0)
    data['srv_concentration'] = data['srv_count'] / (data['count'] + 1.0)
    print("      - Berhasil mengekstrak fitur baru: 'byte_ratio' dan 'srv_concentration'")

    # 1.5 Encoding Categorical Data
    print("\n[1.5] Encoding Categorical Data:")
    freq_encoding = data['service'].value_counts(normalize=True).to_dict()
    data['service_freq_encoded'] = data['service'].map(freq_encoding)
    print("      - Frequency Encoding diterapkan pada kolom 'service'")

    cat_cols = ['protocol_type', 'service', 'flag']
    X_raw = data.drop(columns=['label'])
    y = data['label']
    X_encoded = pd.get_dummies(X_raw, columns=cat_cols, drop_first=True)
    print(f"      - One-Hot Encoding selesai. Total fitur numerik: {X_encoded.shape[1]} kolom")

    # 1.6 Feature Selection (Berdasarkan Korelasi & Analisis Multikolinearitas)
    print("\n[1.6] Feature Selection:")
    label_map = {'Normal': 0, 'DoS_SYN_Flood': 1, 'Port_Scan': 2}
    temp_target = y.map(label_map)
    corr_series = X_encoded.apply(lambda x: x.corr(temp_target)).abs()
    print("      - Top 5 Fitur dengan korelasi tertinggi terhadap serangan:")
    print(corr_series.sort_values(ascending=False).head(5))

    # 1.7 Feature Scaling & Menangani Imbalanced Data dengan SMOTE
    print("\n[1.7] Feature Scaling & Balancing (StandardScaler + SMOTE):")
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=0.20, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    feature_names = X_encoded.columns.tolist()

    print("      - Distribusi kelas training SEBELUM SMOTE:")
    for cls, val in y_train.value_counts().items():
        print(f"        * {cls:<15}: {val}")

    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train_scaled, y_train)

    print("      - Distribusi kelas training SESUDAH SMOTE:")
    for cls, val in y_train_resampled.value_counts().items():
        print(f"        * {cls:<15}: {val}")
    print("      [PENTING] SMOTE HANYA diterapkan pada data train untuk mencegah data leakage!")

    # =========================================================================
    # TAHAP 2: EXPLORATORY DATA ANALYSIS (EDA)
    # =========================================================================
    print("\n" + "=" * 50)
    print("TAHAP 2: EXPLORATORY DATA ANALYSIS (EDA)")
    print("=" * 50)

    # 2.1 Univariate Analysis: Menganalisis Satu Variabel pada Satu Waktu
    print("\n[2.1] Univariate Analysis:")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Histogram Durasi Koneksi
    axes[0].hist(data['duration'], bins=20, color='#3498db', edgecolor='black')
    axes[0].set_title('Univariate: Distribusi Durasi Koneksi', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('Durasi (detik)')
    axes[0].set_ylabel('Frekuensi')

    # Bar Plot Distribusi Kelas Target
    target_counts = y.value_counts()
    axes[1].bar(target_counts.index, target_counts.values, color=['#2ecc71', '#e74c3c', '#e67e22'])
    axes[1].set_title('Univariate: Distribusi Kelas Target (Imbalanced)', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Label Trafik / Serangan')
    axes[1].set_ylabel('Jumlah Sampel')
    for i, v in enumerate(target_counts.values):
        axes[1].text(i, v + 120, f"{v}", ha='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig('eda_plots/01_univariate_analysis.png', dpi=300)
    plt.close()
    print("      [✓] Visualisasi tersimpan: 'eda_plots/01_univariate_analysis.png'")

    # 2.2 Bivariate Analysis: Menganalisis Hubungan Antara Dua Variabel
    print("\n[2.2] Bivariate Analysis:")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Bivariate 1: Boxplot Label vs Count (DoS)
    sns.boxplot(x='label', y='count', data=data, ax=axes[0], palette=['#2ecc71', '#e74c3c', '#e67e22'])
    axes[0].set_title('Bivariate: Label vs Connection Count (DoS Indikator)', fontsize=12, fontweight='bold')

    # Bivariate 2: Boxplot Label vs Diff Srv Rate (Scan)
    sns.boxplot(x='label', y='diff_srv_rate', data=data, ax=axes[1], palette=['#2ecc71', '#e74c3c', '#e67e22'])
    axes[1].set_title('Bivariate: Label vs Diff Srv Rate (Scan Indikator)', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.savefig('eda_plots/02_bivariate_analysis.png', dpi=300)
    plt.close()
    print("      [✓] Visualisasi tersimpan: 'eda_plots/02_bivariate_analysis.png'")

    # 2.3 Multivariate Analysis: Heatmap & Pair Plot (Adopsi pola paket 'psych' di R)
    print("\n[2.3] Multivariate Analysis (Heatmap & Pair Plot ala 'psych'):")
    plt.figure(figsize=(10, 8))
    numeric_cols = ['duration', 'src_bytes', 'dst_bytes', 'count', 'srv_count', 'same_srv_rate', 'diff_srv_rate', 'byte_ratio', 'srv_concentration']
    corr_matrix = data[numeric_cols].corr()
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5)
    plt.title('Multivariate Analysis: Heatmap Korelasi Fitur Jaringan', fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig('eda_plots/03_multivariate_correlation.png', dpi=300)
    plt.close()
    print("      [✓] Visualisasi Correlation Heatmap tersimpan di 'eda_plots/03_multivariate_correlation.png'")

    # Visualisasi Pair Plot Statistik Multivariat
    pair_sample = data[['duration', 'count', 'diff_srv_rate', 'byte_ratio', 'label']].sample(n=500, random_state=42)
    pair_plot = sns.pairplot(pair_sample, hue='label', palette={'Normal': '#2ecc71', 'DoS_SYN_Flood': '#e74c3c', 'Port_Scan': '#e67e22'}, diag_kind='kde')
    pair_plot.fig.suptitle("Multivariate Pair Plot (Adopsi Paket 'psych')", y=1.02, fontsize=13, fontweight='bold')
    pair_plot.savefig('eda_plots/03_pairplot_psych.png', dpi=200)
    plt.close()
    print("      [✓] Visualisasi Pair Plot statistik tersimpan di 'eda_plots/03_pairplot_psych.png'")

    # =========================================================================
    # TAHAP 3: TRAINING (PELATIHAN MODEL)
    # =========================================================================
    print("\n" + "=" * 50)
    print("TAHAP 3: TRAINING (PELATIHAN MODEL)")
    print("=" * 50)
    print("[*] Menginisialisasi Random Forest Classifier (100 Trees, max_depth=12)")
    rf_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=12,
        min_samples_split=5,
        random_state=42,
        n_jobs=1
    )

    print("[*] Melatih model pada training set yang telah di-resample...")
    rf_model.fit(X_train_resampled, y_train_resampled)
    print("[✓] Model Training Selesai!")

    # =========================================================================
    # TAHAP 4: TESTING (PENGUJIAN & EVALUASI MODEL)
    # =========================================================================
    print("\n" + "=" * 50)
    print("TAHAP 4: TESTING (PENGUJIAN & EVALUASI MODEL)")
    print("=" * 50)
    y_pred = rf_model.predict(X_test_scaled)
    target_classes = sorted(list(y_test.unique()))

    test_acc = accuracy_score(y_test, y_pred)
    f1_mac = f1_score(y_test, y_pred, average='macro')
    print(f"[✓] Overall Test Accuracy : {test_acc * 100:.2f}%")
    print(f"[✓] Macro F1-Score        : {f1_mac:.4f}\n")

    print("--- Classification Report ---")
    print(classification_report(y_test, y_pred, digits=4))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred, labels=target_classes)
    plt.figure(figsize=(7, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=target_classes, yticklabels=target_classes, cbar=False,
                annot_kws={'size': 14, 'weight': 'bold'})
    plt.title('Testing: Confusion Matrix Evaluation', fontsize=13, fontweight='bold')
    plt.xlabel('Prediksi AI', fontsize=11, fontweight='bold')
    plt.ylabel('Kondisi Nyata', fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig('eda_plots/04_confusion_matrix.png', dpi=300)
    plt.close()
    print("[✓] Confusion Matrix tersimpan di 'eda_plots/04_confusion_matrix.png'")

    print("\n--- ANALISIS KRITIS DALAM KEAMANAN SIBER: FP vs FN ---")
    print("1. False Positive (Alarm Palsu):")
    print("   - Trafik normal dianggap serangan. Menimbulkan 'alert fatigue' bagi analis SOC.")
    print("2. False Negative (SERANGAN LOLOS):")
    print("   - Serangan nyata dianggap normal. DAMPAK FATAL! Server lumpuh atau data dicuri.")
    print("   - Oleh karena itu, metrik RECALL untuk kelas serangan wajib dijaga mendekati 1.00 (100%).")

    # Feature Importance (XAI)
    importances = rf_model.feature_importances_
    feat_df = pd.DataFrame({'feature': feature_names, 'importance': importances}).sort_values('importance', ascending=False)
    plt.figure(figsize=(10, 5))
    sns.barplot(x='importance', y='feature', data=feat_df.head(8), palette='viridis')
    plt.title('Top 8 Feature Importance (Pilar Deteksi Serangan)', fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig('eda_plots/05_feature_importance.png', dpi=300)
    plt.close()
    print("[✓] Feature Importance tersimpan di 'eda_plots/05_feature_importance.png'")

    # =========================================================================
    # TAHAP 5: DEPLOYMENT (PENYEBARAN / PENERAPAN)
    # =========================================================================
    print("\n" + "=" * 50)
    print("TAHAP 5: DEPLOYMENT (PENYEBARAN / PENERAPAN)")
    print("=" * 50)
    joblib.dump(rf_model, 'saved_models/nids_random_forest.pkl')
    joblib.dump(scaler, 'saved_models/scaler.pkl')
    joblib.dump(feature_names, 'saved_models/feature_columns.pkl')
    joblib.dump(target_classes, 'saved_models/target_classes.pkl')
    print("[✓] Artefak model berhasil dikemas dan disimpan:")
    print("    - saved_models/nids_random_forest.pkl (Bobot Model)")
    print("    - saved_models/scaler.pkl (Pipeline Standarisasi)")
    print("    - saved_models/feature_columns.pkl (Daftar Fitur)")
    print("    - saved_models/target_classes.pkl (Label Target)")
    print("[✓] Model siap diintegrasikan ke lingkungan produksi (Next-Gen AI Firewall Engine)!")

    # =========================================================================
    # TAHAP 6: INFERENCE (INFERENSI REAL-TIME & MITIGASI ADAPTIF)
    # =========================================================================
    print("\n" + "=" * 50)
    print("TAHAP 6: INFERENCE (INFERENSI & PERTAHANAN ADAPTIF)")
    print("=" * 50)
    import inference_deploy
    inference_deploy.run_inference_simulation()

if __name__ == '__main__':
    main()
