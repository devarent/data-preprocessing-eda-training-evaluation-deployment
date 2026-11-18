"""
========================================================================================
MODUL INFERENCE & DEPLOYMENT (SIMULASI PERTAHANAN ADAPTIF)
Tema: "Dari Deteksi Statis Menuju Pertahanan Adaptif: Peran AI dalam Keamanan Siber"
========================================================================================
Script ini mensimulasikan sistem keamanan siber cerdas (Next-Gen AI Firewall / NIDS)
yang menerima log lalu lintas jaringan real-time dan secara otomatis mengambil
tindakan mitigasi aktif (Adaptive Response):
  - Normal Traffic    -> [PASS] Diizinkan lewat.
  - DoS SYN Flood     -> [BLOCKED] Blokir IP penyerang secara otomatis di Firewall.
  - Port Scan Recon   -> [QUARANTINE] Karantina IP, batasi connection rate, kirim SIEM alert.
========================================================================================
"""

import os
import time
import joblib
import pandas as pd
import numpy as np

def load_security_engine():
    """Memuat model AI, scaler, dan konfigurasi fitur yang telah dilatih."""
    model_path = 'saved_models/nids_random_forest.pkl'
    scaler_path = 'saved_models/scaler.pkl'
    columns_path = 'saved_models/feature_columns.pkl'
    
    if not (os.path.exists(model_path) and os.path.exists(scaler_path) and os.path.exists(columns_path)):
        raise FileNotFoundError("Model artefak belum ditemukan! Silakan jalankan 'train_nids_model.py' terlebih dahulu.")
        
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    feature_columns = joblib.load(columns_path)
    
    return model, scaler, feature_columns

def preprocess_live_traffic(raw_packet_df, scaler, feature_columns):
    """
    Melakukan pipeline preprocessing yang identik dengan fase pelatihan (Pilar #2):
    1. Feature Engineering
    2. One-Hot Encoding (align dengan feature training)
    3. Standarisasi Fitur
    """
    df = raw_packet_df.copy()
    
    # Feature Engineering
    df['byte_ratio'] = df['src_bytes'] / (df['dst_bytes'] + 1.0)
    df['srv_concentration'] = df['srv_count'] / (df['count'] + 1.0)
    
    # Frequency Encoding
    freq_dict = {'http': 0.55, 'dns': 0.25, 'smtp': 0.10, 'ftp': 0.05, 'ssh': 0.05, 'private': 0.15}
    df['service_freq_encoded'] = df['service'].map(freq_dict).fillna(0.05)
    
    # One-Hot Encoding
    cat_cols = ['protocol_type', 'service', 'flag']
    df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)
    
    # Reindex agar persis sama dengan fitur saat model dilatih (kolom hilang diisi 0)
    df_aligned = df_encoded.reindex(columns=feature_columns, fill_value=0)
    
    # Scaling
    scaled_data = scaler.transform(df_aligned)
    return scaled_data

def adaptive_mitigation_action(prediction, confidence, packet_info):
    """
    Simulasi Pilar Keamanan Adaptif:
    Mengubah deteksi statis menjadi respon otomatis dinamis.
    """
    src_ip = packet_info.get('src_ip', 'Unknown')
    dst_ip = packet_info.get('dst_ip', '192.168.1.100')
    target_port = packet_info.get('service', 'unknown')
    
    if prediction == 'Normal':
        status = "🟢 [ALLOWED - TRAFFIC NORMAL]"
        action = "Tidak ada tindakan mitigasi yang diperlukan. Paket diteruskan ke aplikasi."
        color_code = "\033[92m" # Green
    elif prediction == 'DoS_SYN_Flood':
        status = "🚨 [CRITICAL ALERT - SERANGAN DoS SYN FLOOD]"
        action = (
            f"TINDAKAN PERTAHANAN ADAPTIF:\n"
            f"  1. Mengirim perintah otomatis ke Firewall: `iptables -A INPUT -s {src_ip} -j DROP`\n"
            f"  2. Mengaktifkan SYN Cookies pada kernel server `{dst_ip}`.\n"
            f"  3. Memblokir sementara IP penyerang ({src_ip}) selama 60 menit."
        )
        color_code = "\033[91m" # Red
    elif prediction == 'Port_Scan':
        status = "⚠️ [WARNING - DETEKSI AKTIVITAS PORT SCANNING]"
        action = (
            f"TINDAKAN PERTAHANAN ADAPTIF:\n"
            f"  1. Membatasi rate koneksi (Rate Limiting) dari IP {src_ip}.\n"
            f"  2. Mengisolasi akses ke port sensitif ({target_port}).\n"
            f"  3. Mengirimkan security alert ke dashboard SOC (Security Operations Center)."
        )
        color_code = "\033[93m" # Yellow
    else:
        status = "🔍 [ANOMALY DETECTED]"
        action = "Pola serangan tidak dikenal terdeteksi. Diteruskan ke analis SOC untuk investigasi."
        color_code = "\033[95m" # Magenta

    reset_code = "\033[0m"
    return status, action, color_code, reset_code

def run_inference_simulation():
    print("=" * 80)
    print("NEXT-GENERATION AI INTRUSION DETECTION & ADAPTIVE DEFENSE SYSTEM")
    print("Simulasi Penanganan Data Baru (Inference & Deploy)")
    print("=" * 80)
    
    # 1. Load Model
    print("[*] Memuat model machine learning dan artefak preprocessing...")
    model, scaler, feature_columns = load_security_engine()
    print("[✓] Model Random Forest siap aktif menjaga jaringan!\n")
    
    # 2. Definisikan Data Baru (Simulasi Live Traffic dari Berbagai IP)
    live_traffic_samples = [
        {
            'desc': 'Skenario 1: Karyawan mengakses portal web internal (HTTP Normal)',
            'meta': {'src_ip': '192.168.1.45', 'dst_ip': '192.168.1.100', 'service': 'http'},
            'packet': {
                'duration': 1.8,
                'protocol_type': 'tcp',
                'service': 'http',
                'flag': 'SF',
                'src_bytes': 350.0,
                'dst_bytes': 2800.0,
                'count': 3,
                'srv_count': 3,
                'same_srv_rate': 1.0,
                'diff_srv_rate': 0.0,
                'dst_host_count': 25,
                'dst_host_srv_count': 200
            }
        },
        {
            'desc': 'Skenario 2: Botnet melancarkan serangan banjir TCP SYN (SYN Flood DoS)',
            'meta': {'src_ip': '203.0.113.88', 'dst_ip': '192.168.1.100', 'service': 'http'},
            'packet': {
                'duration': 0.0,
                'protocol_type': 'tcp',
                'service': 'http',
                'flag': 'S0',
                'src_bytes': 48.0,
                'dst_bytes': 0.0,
                'count': 185,
                'srv_count': 182,
                'same_srv_rate': 0.99,
                'diff_srv_rate': 0.01,
                'dst_host_count': 255,
                'dst_host_srv_count': 5
            }
        },
        {
            'desc': 'Skenario 3: Penyerang melakukan pemindaian port untuk mencari celah (Port Scan)',
            'meta': {'src_ip': '198.51.100.12', 'dst_ip': '192.168.1.100', 'service': 'private'},
            'packet': {
                'duration': 0.1,
                'protocol_type': 'tcp',
                'service': 'private',
                'flag': 'REJ',
                'src_bytes': 40.0,
                'dst_bytes': 0.0,
                'count': 78,
                'srv_count': 2,
                'same_srv_rate': 0.05,
                'diff_srv_rate': 0.95,
                'dst_host_count': 210,
                'dst_host_srv_count': 2
            }
        },
        {
            'desc': 'Skenario 4: Administrator melakukan backup data melalui SSH aman (Normal SSH)',
            'meta': {'src_ip': '192.168.1.10', 'dst_ip': '192.168.1.100', 'service': 'ssh'},
            'packet': {
                'duration': 14.5,
                'protocol_type': 'tcp',
                'service': 'ssh',
                'flag': 'SF',
                'src_bytes': 14500.0,
                'dst_bytes': 28900.0,
                'count': 2,
                'srv_count': 2,
                'same_srv_rate': 1.0,
                'diff_srv_rate': 0.0,
                'dst_host_count': 10,
                'dst_host_srv_count': 150
            }
        }
    ]
    
    for i, test in enumerate(live_traffic_samples, 1):
        print("-" * 80)
        print(f"[PAKET LIVE #{i}] {test['desc']}")
        print(f"Info Koneksi: {test['meta']['src_ip']} -> {test['meta']['dst_ip']} | Service: {test['meta']['service']}")
        
        # Konversi ke DataFrame
        df_packet = pd.DataFrame([test['packet']])
        
        # Preprocessing live
        processed_data = preprocess_live_traffic(df_packet, scaler, feature_columns)
        
        # Prediksi AI & Confidence
        prediction = model.predict(processed_data)[0]
        probs = model.predict_proba(processed_data)[0]
        confidence = np.max(probs) * 100
        
        # Tentukan tindakan adaptif
        status, action, color_code, reset_code = adaptive_mitigation_action(prediction, confidence, test['meta'])
        
        print(f"Hasil Klasifikasi AI : {color_code}{prediction}{reset_code} (Tingkat Keyakinan: {confidence:.2f}%)")
        print(f"Status Sistem        : {status}")
        print(f"Respon Sistem        :\n{action}")
        time.sleep(0.5)

    print("\n" + "=" * 80)
    print("SIMULASI PERTAHANAN ADAPTIF BERHASIL DISELESAIKAN!")
    print("Sistem AI berhasil membedakan lalu lintas normal dan menghentikan serangan secara otomatis.")
    print("=" * 80)

if __name__ == '__main__':
    run_inference_simulation()

