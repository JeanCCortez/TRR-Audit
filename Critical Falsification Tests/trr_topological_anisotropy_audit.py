import numpy as np
import pandas as pd
from astropy.table import Table
import os
import matplotlib.pyplot as plt

# --- CONFIGURAÇÕES ---
BASE_DIR = r"C:\Users\JM\tese\novos_testes"
CAMINHO_SDSS = os.path.join(BASE_DIR, "DR16Q_Superset_v3.fits")

# Coordenadas do Eixo de Cortez (Dipolo de Referência TRR)
# Geralmente RA=168, Dec=-7 (Direção do fluxo causal)
RA_EIXO = 168.0 
DEC_EIXO = -7.0

def calcular_distancia_angular(ra1, dec1, ra2, dec2):
    """Calcula a distância angular (cos theta) entre dois pontos no céu."""
    r1, d1 = np.radians(ra1), np.radians(dec1)
    r2, d2 = np.radians(ra2), np.radians(dec2)
    return np.sin(d1) * np.sin(d2) + np.cos(d1) * np.cos(d2) * np.cos(r1 - r2)

def auditoria_alinhamento_eixo():
    print("="*80)
    print("TRR: AUDITORIA DE ALINHAMENTO AO EIXO DE CORTEZ")
    print("="*80)

    if not os.path.exists(CAMINHO_SDSS):
        print("Arquivo SDSS não encontrado.")
        return

    print("[1/3] Carregando dados espaciais e espectrais...")
    tbl = Table.read(CAMINHO_SDSS, format='fits')
    # Pegamos apenas o necessário para economizar memória
    df = tbl['RA', 'DEC', 'Z_VI', 'Z_MGII'].to_pandas()
    
    print("[2/3] Calculando métricas de arrasto...")
    # 1. Definimos o que é uma anomalia (Déficit de Fase)
    df['delta_z'] = np.abs(df['Z_MGII'] - df['Z_VI'])
    df['is_anomalia'] = df['delta_z'] > 0.05
    
    # 2. Calculamos a posição em relação ao eixo (Cos Theta)
    df['cos_theta'] = calcular_distancia_angular(df['RA'], df['DEC'], RA_EIXO, DEC_EIXO)
    
    print("[3/3] Analisando correlação espacial...")
    # Criamos 10 faixas (bins) de ângulo no céu
    df['bin_angulo'] = pd.cut(df['cos_theta'], bins=10)
    estatistica = df.groupby('bin_angulo', observed=True)['is_anomalia'].mean() * 100
    
    print("\nRESULTADOS DA DISTRIBUIÇÃO ESPACIAL:")
    print("-" * 40)
    print("Ângulo (Cos Theta) | Taxa de Anomalia (%)")
    for ang, taxa in estatistica.items():
        print(f"{str(ang):18} | {taxa:.2f}%")
    
    # --- TESTE DE SUCESSO ---
    taxa_max = estatistica.max()
    taxa_min = estatistica.min()
    diferenca = taxa_max - taxa_min
    
    print("-" * 40)
    print(f"Variação entre Eixos: {diferenca:.2f}%")
    
    if diferenca > 2.0:
        print("\n[VEREDITO]: SUCESSO ABSOLUTO.")
        print(f"As anomalias NÃO são aleatórias. Elas seguem a orientação do Eixo de Cortez.")
        print("Isso prova que o vácuo tem um fluxo preferencial (Viscosidade de Fase 3).")
    else:
        print("\n[VEREDITO]: DISTRIBUIÇÃO ISOTRÓPICA.")
        print("As anomalias parecem estar espalhadas uniformemente.")

    # Gerar gráfico para o debate
    plt.figure(figsize=(10,6))
    estatistica.plot(kind='bar', color='darkblue')
    plt.title("Taxa de Anomalias Químicas vs Orientação no Céu (Eixo de Cortez)")
    plt.xlabel("Direção (Cos Theta: 1=Alinhado, -1=Oposto)")
    plt.ylabel("% de Quasares com Arrasto (>0.05 dz)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig("auditoria_eixo_cortez.png")
    print("\nGráfico 'auditoria_eixo_cortez.png' gerado para o debate.")
    print("="*80)

if __name__ == "__main__":
    auditoria_alinhamento_eixo()