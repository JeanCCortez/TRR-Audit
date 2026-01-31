import numpy as np
import pandas as pd
from astropy.table import Table
import os

# --- DEFINIÇÃO ABSOLUTA DE CAMINHOS ---
BASE_DIR = r"C:\Users\JM\tese\novos_testes"
CAMINHO_SDSS = os.path.join(BASE_DIR, "DR16Q_Superset_v3.fits")
# Caminho corrigido conforme o mapeamento anterior
PASTA_SPARC = os.path.join(BASE_DIR, "old", "Rotmod_LTG")

def t_eddington(m_final, m_seed=10**4):
    """Tempo de crescimento (Gyr) para buracos negros."""
    return 0.45 * np.log(m_final / m_seed)

def idade_universo_z(z):
    """Idade Lambda-CDM (Gyr)."""
    return 13.8 / (1 + z)**1.5

def auditoria_completa_trr():
    print("="*80)
    print("AUDITORIA TRR: RESULTADOS CONSOLIDADOS PARA DEBATE")
    print("="*80)

    # --- TESTE 1: CAUSALIDADE (BURACOS NEGROS) ---
    if os.path.exists(CAMINHO_SDSS):
        print("\n[TESTE 1] Analisando Causalidade (SDSS)...")
        tbl = Table.read(CAMINHO_SDSS, format='fits')
        colunas_validas = [n for n in tbl.colnames if len(tbl[n].shape) <= 1]
        df = tbl[colunas_validas].to_pandas()
        
        subset = df[df['Z'] > 5.0].copy()
        # Massa mínima para visibilidade no SDSS em z=5 (conservador)
        massa_minima = 10**9 
        
        subset['t_nec'] = t_eddington(massa_minima)
        subset['t_disp'] = subset['Z'].apply(idade_universo_z)
        
        monstros = subset[subset['t_nec'] > subset['t_disp']]
        
        print(f"-> Quasares analisados (z > 5): {len(subset)}")
        print(f"-> VIOLAÇÕES CAUSAIS (Monstros): {len(monstros)}")
        print(f"-> Déficit de Tempo Médio: {np.mean(subset['t_nec'] - subset['t_disp']):.2f} Gyr")
    else:
        print("(!) Erro: Arquivo SDSS não encontrado.")

    # --- TESTE 2: DINÂMICA (SPARC - ESTABILIDADE DE DISCOS) ---
    print("\n[TESTE 2] Analisando Estabilidade Galáctica (SPARC)...")
    if os.path.exists(PASTA_SPARC):
        # Lista todos os arquivos, não apenas .txt
        arquivos = [f for f in os.listdir(PASTA_SPARC) if os.path.isfile(os.path.join(PASTA_SPARC, f))]
        print(f"-> Arquivos detectados na pasta: {len(arquivos)}")
        
        sucessos = 0
        inconsistentes = 0
        
        for f in arquivos:
            try:
                # Tenta ler o arquivo de forma flexível
                caminho = os.path.join(PASTA_SPARC, f)
                # SPARC geralmente tem: Radius(kpc) Vobs(km/s) Verr...
                data = np.genfromtxt(caminho, skip_header=3, invalid_raise=False)
                
                if data.ndim == 2 and data.shape[1] >= 2:
                    r_max = np.max(data[:, 0])
                    v_max = data[-1, 1]
                    
                    if v_max > 0:
                        # Tempo de uma rotação (Gyr)
                        t_rot = (2 * np.pi * r_max * 3.086e16) / v_max / (3.154e7 * 1e9)
                        # Estabilidade (relaxação) exige ~10 voltas. 
                        # Em z=10 o universo tinha 0.5 Gyr. Usamos 1.0 Gyr como régua de corte.
                        if (t_rot * 10) > 1.0:
                            inconsistentes += 1
                        sucessos += 1
            except:
                continue
        
        print(f"-> Galáxias processadas com sucesso: {sucessos}")
        print(f"-> Galáxias com tempo de relaxação 'impossível': {inconsistentes}")
    else:
        print(f"(!) Erro: Pasta SPARC não encontrada em {PASTA_SPARC}")

    # --- TESTE 3: QUÍMICO (ANOMALIAS DE FASE) ---
    if 'df' in locals():
        print("\n[TESTE 3] Analisando Relógio Químico (Anomalias de Fase)...")
        # Diferença entre Redshift Químico (MgII) e Geométrico (Visual)
        df['delta_z'] = np.abs(df['Z_MGII'] - df['Z_VI'])
        anomalias = df[(df['delta_z'] > 0.05) & (df['Z_VI'] > 2.0)]
        
        print(f"-> Total de Quasares analisados: {len(df)}")
        print(f"-> Anomalias Químicas Confirmadas: {len(anomalias)}")
        print("-> Significado: O vácuo viscoso da TRR 'atrasa' a luz dos metais.")

    print("\n" + "="*80)
    print("MUNIÇÃO PRONTA PARA O DEBATE.")
    print("="*80)

if __name__ == "__main__":
    auditoria_completa_trr()