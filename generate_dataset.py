"""
=============================================================================
MODUL 1: DATA INGESTION & SYNTHESIS (PILAR #1: DATA ADALAH BAHAN BAKAR)
Kasus: Network Intrusion Detection System (NIDS)
Dataset: Network Traffic Flow (Inspirasi NSL-KDD & CIC-IDS2017)
=============================================================================
"""

import numpy as np
import pandas as pd
import os

def generate_network_data(n_samples=10000, random_seed=42):
    np.random.seed(random_seed)
    
    # Distribusi data imbalanced realistis (Pilar #2: Serangan adalah kejadian langka)
    n_normal = int(n_samples * 0.70)      # 70% Normal
    n_dos = int(n_samples * 0.20)         # 20% DoS SYN Flood
    n_scan = n_samples - n_normal - n_dos # 10% Port Scan
    
    print(f"[*] Men-generate {n_samples} baris network traffic logs:")
    print(f"    - Normal Traffic : {n_normal} sampel (70%)")
    print(f"    - DoS SYN Flood  : {n_dos} sampel (20%)")
    print(f"    - Port Scan      : {n_scan} sampel (10%)")
    
    # --- 1. DATA NORMAL ---
    duration_norm = np.random.exponential(scale=2.5, size=n_normal)
    protocol_norm = np.random.choice(['tcp', 'udp', 'icmp'], size=n_normal, p=[0.75, 0.20, 0.05])
    service_norm = np.random.choice(['http', 'dns', 'smtp', 'ftp', 'ssh'], size=n_normal, p=[0.55, 0.25, 0.10, 0.05, 0.05])
    flag_norm = np.random.choice(['SF', 'S0', 'REJ'], size=n_normal, p=[0.92, 0.05, 0.03])
    src_bytes_norm = np.random.gamma(shape=2, scale=400, size=n_normal) + 50
    dst_bytes_norm = np.random.gamma(shape=3, scale=800, size=n_normal) + 100
    count_norm = np.random.poisson(lam=5, size=n_normal) + 1
    srv_count_norm = np.random.poisson(lam=4, size=n_normal) + 1
    same_srv_rate_norm = np.clip(np.random.normal(loc=0.85, scale=0.10, size=n_normal), 0.0, 1.0)
    diff_srv_rate_norm = np.clip(1.0 - same_srv_rate_norm + np.random.normal(0, 0.05, n_normal), 0.0, 1.0)
    dst_host_count_norm = np.random.randint(1, 200, size=n_normal)
    dst_host_srv_count_norm = np.random.randint(10, 255, size=n_normal)
    label_norm = ['Normal'] * n_normal
    
    # --- 2. DATA DoS SYN FLOOD ---
    duration_dos = np.zeros(n_dos)
    protocol_dos = np.random.choice(['tcp'], size=n_dos)
    service_dos = np.random.choice(['http', 'private'], size=n_dos, p=[0.85, 0.15])
    flag_dos = np.random.choice(['S0', 'RSTO'], size=n_dos, p=[0.95, 0.05])
    src_bytes_dos = np.random.uniform(40, 80, size=n_dos)
    dst_bytes_dos = np.zeros(n_dos)
    count_dos = np.random.poisson(lam=120, size=n_dos) + 50
    srv_count_dos = count_dos - np.random.randint(0, 5, size=n_dos)
    same_srv_rate_dos = np.clip(np.random.normal(loc=0.98, scale=0.02, size=n_dos), 0.9, 1.0)
    diff_srv_rate_dos = np.clip(np.random.normal(loc=0.02, scale=0.02, size=n_dos), 0.0, 0.1)
    dst_host_count_dos = np.random.randint(200, 255, size=n_dos)
    dst_host_srv_count_dos = np.random.randint(1, 30, size=n_dos)
    label_dos = ['DoS_SYN_Flood'] * n_dos
    
    # --- 3. DATA PORT SCAN ---
    duration_scan = np.random.uniform(0, 0.5, size=n_scan)
    protocol_scan = np.random.choice(['tcp', 'udp'], size=n_scan, p=[0.8, 0.2])
    service_scan = np.random.choice(['private', 'http', 'smtp', 'ftp', 'dns'], size=n_scan, p=[0.5, 0.2, 0.1, 0.1, 0.1])
    flag_scan = np.random.choice(['REJ', 'S0', 'RSTO'], size=n_scan, p=[0.60, 0.35, 0.05])
    src_bytes_scan = np.random.uniform(20, 60, size=n_scan)
    dst_bytes_scan = np.zeros(n_scan)
    count_scan = np.random.poisson(lam=60, size=n_scan) + 20
    srv_count_scan = np.random.poisson(lam=2, size=n_scan) + 1
    same_srv_rate_scan = np.clip(np.random.normal(loc=0.10, scale=0.05, size=n_scan), 0.0, 0.3)
    diff_srv_rate_scan = np.clip(np.random.normal(loc=0.90, scale=0.05, size=n_scan), 0.7, 1.0)
    dst_host_count_scan = np.random.randint(150, 255, size=n_scan)
    dst_host_srv_count_scan = np.random.randint(1, 10, size=n_scan)
    label_scan = ['Port_Scan'] * n_scan
    
    # Gabungkan semua data
    data = {
        'duration': np.concatenate([duration_norm, duration_dos, duration_scan]),
        'protocol_type': np.concatenate([protocol_norm, protocol_dos, protocol_scan]),
        'service': np.concatenate([service_norm, service_dos, service_scan]),
        'flag': np.concatenate([flag_norm, flag_dos, flag_scan]),
        'src_bytes': np.round(np.concatenate([src_bytes_norm, src_bytes_dos, src_bytes_scan]), 2),
        'dst_bytes': np.round(np.concatenate([dst_bytes_norm, dst_bytes_dos, dst_bytes_scan]), 2),
        'count': np.concatenate([count_norm, count_dos, count_scan]),
        'srv_count': np.concatenate([srv_count_norm, srv_count_dos, srv_count_scan]),
        'same_srv_rate': np.round(np.concatenate([same_srv_rate_norm, same_srv_rate_dos, same_srv_rate_scan]), 4),
        'diff_srv_rate': np.round(np.concatenate([diff_srv_rate_norm, diff_srv_rate_dos, diff_srv_rate_scan]), 4),
        'dst_host_count': np.concatenate([dst_host_count_norm, dst_host_count_dos, dst_host_count_scan]),
        'dst_host_srv_count': np.concatenate([dst_host_srv_count_norm, dst_host_srv_count_dos, dst_host_srv_count_scan]),
        'label': np.concatenate([label_norm, label_dos, label_scan])
    }
    
    # Acak urutan baris data (shuffle)
    indices = np.random.permutation(n_samples)
    for col in data:
        data[col] = data[col][indices]
        
    df = pd.DataFrame(data)
    
    # Simulasi dunia nyata (Garbage In, Garbage Out):
    # 1. Masukkan missing values ke beberapa kolom numerik
    nan_indices_src = np.random.choice(n_samples, size=15, replace=False)
    nan_indices_dst = np.random.choice(n_samples, size=12, replace=False)
    df.loc[nan_indices_src, 'src_bytes'] = np.nan
    df.loc[nan_indices_dst, 'dst_bytes'] = np.nan
    
    # 2. Masukkan beberapa outliers ekstrim (noise / transmisi anomali)
    outlier_idx = np.random.choice(n_samples, size=5, replace=False)
    df.loc[outlier_idx, 'src_bytes'] = 999999.0
    
    return df

if __name__ == '__main__':
    df = generate_network_data(n_samples=10000)
    output_file = 'network_traffic_dataset.csv'
    df.to_csv(output_file, index=False)
    print(f"[✓] Berhasil menyimpan dataset ke '{output_file}'!")
    print(f"[✓] Ukuran file: {os.path.getsize(output_file) / 1024:.2f} KB")
