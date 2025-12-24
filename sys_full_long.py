import pandas as pd
import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u
from scipy.optimize import least_squares
import os

# Ajuste para a sua pasta
os.chdir(r"C:\Users\JM\dosie tese\novos testes")

def auditoria_pantheon_2018():
    print("--- INICIANDO AUDITORIA: PANTHEON 2018 (1048 SNe) ---")
    
    try:
        # 1. Carregar o catálogo Pantheon 2018
        # Se ainda não baixou o lcparam_full_long.txt, este script tenta ler o arquivo local
        # ou você pode usar o PantheonPlusSH0ES.csv filtrando para os IDs de 2018.
        if os.path.exists('lcparam_full_long.txt'):
            df = pd.read_csv('lcparam_full_long.txt', sep=r'\s+')
        else:
            print("Ficheiro lcparam_full_long.txt não encontrado. Usando base Pantheon+ filtrada...")
            df_full = pd.read_csv('PantheonPlusSH0ES.csv', sep=r'\s+', engine='python')
            # O Pantheon 2018 está contido no Plus. Vamos pegar as primeiras 1048 ou filtrar por Survey
            df = df_full.head(1048).copy()
            df.rename(columns={'m_b_corr': 'mb', 'zcmb': 'z'}, inplace=True)

        print(f"✅ Amostra carregada: {len(df)} Supernovas.")

        # 2. Coordenadas Galácticas
        coords = SkyCoord(ra=df['RA'].values*u.degree, dec=df['DEC'].values*u.degree, frame='icrs')
        df['l'], df['b'] = coords.galactic.l.degree, coords.galactic.b.degree

        # 3. Cálculo do Resíduo (Vetor T_mu)
        df['residual'] = df['mb'] - df['mb'].mean()

        # 4. Ajuste de Dipolo
        def model(params, l, b):
            D, l_p, b_p = params
            l_rad, b_rad = np.radians(l), np.radians(b)
            return D * (np.sin(b_rad)*np.sin(b_p) + np.cos(b_rad)*np.cos(b_p)*np.cos(l_rad - l_p))

        # Chute inicial (Direção Axis of Evil)
        x0 = [0.1, np.radians(164), np.radians(-58)]
        res = least_squares(lambda p: model(p, df['l'], df['b']) - df['residual'], x0)

        # 5. Bootstrap (2000 iterações)
        print("Calculando Bootstrap com 1048 SNe...")
        boot_Ds = []
        for _ in range(2000):
            sample = df.sample(frac=1.0, replace=True)
            res_b = least_squares(lambda p: model(p, sample['l'], sample['b']) - (sample['mb'] - sample['mb'].mean()), x0)
            boot_Ds.append(res_b.x[0])

        sigma = np.mean(boot_Ds) / np.std(boot_Ds)

        print("\n" + "="*50)
        print("      RESULTADO PANTHEON 2018 (AUDITORIA)")
        print("="*50)
        print(f"Direção: l = {np.degrees(res.x[1]):.2f}°, b = {np.degrees(res.x[2]):.2f}°")
        print(f"Magnitude do Dipolo: {res.x[0]:.6f}")
        print(f"Significância Final: {abs(sigma):.2f} Sigma")
        print("="*50)

    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    auditoria_pantheon_2018()