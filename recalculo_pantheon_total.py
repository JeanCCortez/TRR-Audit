import pandas as pd
import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u
from scipy.optimize import least_squares
import os

# Ajuste de diretório
os.chdir(r"C:\Users\JM\dosie tese\novos testes")

def auditoria_total_pantheon():
    file_path = 'PantheonPlusSH0ES.csv'
    
    try:
        # 1. Carregamento sem filtros restritivos
        df = pd.read_csv(file_path, sep='\s+', engine='python')
        print(f"--- ANALISANDO TODO O CATÁLOGO PANTHEON+: {len(df)} SNe ---")

        # Filtro básico: Apenas remover SNe com erro de redshift ou dados faltantes
        # Mantendo a amostra o maior possível (perto de 1700)
        df_clean = df[df['zHD'] > 0.01].copy()
        print(f"Amostra utilizada para auditoria: {len(df_clean)} Supernovas")

        # 2. Coordenadas Galácticas
        coords = SkyCoord(ra=df_clean['RA'].values*u.degree, 
                          dec=df_clean['DEC'].values*u.degree, frame='icrs')
        df_clean['l'] = coords.galactic.l.degree
        df_clean['b'] = coords.galactic.b.degree

        # 3. Resíduos de Magnitude (Calculados individualmente)
        # mu_obs - mu_modelo (Aqui simplificado pela média para ver o dipolo bruto)
        df_clean['residual'] = df_clean['m_b_corr'] - df_clean['m_b_corr'].mean()

        # 4. Ajuste de Dipolo
        def model(params, l, b):
            D, l_p, b_p = params
            l_rad, b_rad = np.radians(l), np.radians(b)
            cos_theta = (np.sin(b_rad) * np.sin(b_p) + 
                         np.cos(b_rad) * np.cos(b_p) * np.cos(l_rad - l_p))
            return D * cos_theta

        # Chute inicial no Eixo do Mal
        x0 = [0.01, np.radians(220), np.radians(-15)]
        res = least_squares(lambda p: model(p, df_clean['l'], df_clean['b']) - df_clean['residual'], x0)
        D_fit, lp_fit, bp_fit = res.x

        # 5. Bootstrap para o Sigma real
        print("Executando Bootstrap (2000 iterações)...")
        boot_Ds = []
        for _ in range(2000):
            sample = df_clean.sample(frac=1.0, replace=True)
            res_b = least_squares(lambda p: model(p, sample['l'], sample['b']) - (sample['m_b_corr'] - sample['m_b_corr'].mean()), x0)
            boot_Ds.append(res_b.x[0])

        sigma = np.mean(boot_Ds) / np.std(boot_Ds)

        print("\n" + "="*45)
        print("      RESULTADO RECALCULADO PANTHEON+")
        print("="*45)
        print(f"Direção: l = {np.degrees(lp_fit):.2f}°, b = {np.degrees(bp_fit):.2f}°")
        print(f"Magnitude do Dipolo: {D_fit:.6f}")
        print(f"Significância Resultante: {abs(sigma):.2f} Sigma")
        print("="*45)

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    auditoria_total_pantheon()