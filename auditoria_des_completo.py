import pandas as pd
import numpy as np
from astropy.io import fits
from astropy.coordinates import SkyCoord
import astropy.units as u
from scipy.optimize import least_squares
import os

os.chdir(r"C:\Users\JM\dosie tese\novos testes")

def auditoria_espacial_multi_catalogo():
    print("--- INICIANDO BUSCA ESPACIAL (DES vs PANTHEON/UNION) ---")
    
    try:
        # 1. Carregar seu arquivo DES
        with fits.open('DES-SN5YR_DES_HEAD.FITS') as hdul:
            df_des = pd.DataFrame(hdul[1].data)
        
        # 2. Carregar o Pantheon+ (ou o arquivo que você tiver do Union)
        # Vamos assumir que você tem o arquivo csv do Pantheon+ ainda
        df_pan = pd.read_csv('PantheonPlusSH0ES.csv', sep=r'\s+', engine='python')

        # 3. MATCH ESPACIAL (O pulo do gato)
        # Criamos catálogos de coordenadas
        c_des = SkyCoord(ra=df_des['RA'].values*u.degree, dec=df_des['DEC'].values*u.degree)
        c_pan = SkyCoord(ra=df_pan['RA'].values*u.degree, dec=df_pan['DEC'].values*u.degree)

        # Buscamos quem está no mesmo lugar (tolerância de 2 segundos de arco)
        idx, d2d, d3d = c_des.match_to_catalog_sky(c_pan)
        max_sep = 2 * u.arcsec
        sep_constraint = d2d < max_sep
        
        df_final = df_des[sep_constraint].copy()
        
        print(f"✅ Sucesso! Encontramos {len(df_final)} SNe via Match Espacial.")
        
        if len(df_final) < 500:
            print("Amostra ainda pequena. Aumentando tolerância para 5 arcsec...")
            sep_constraint = d2d < 5 * u.arcsec
            df_final = df_des[sep_constraint].copy()
            print(f"✅ Nova contagem: {len(df_final)} SNe.")

        # 4. Cálculo do Dipolo na amostra recuperada
        coords_gal = SkyCoord(ra=df_final['RA'].values*u.degree, 
                              dec=df_final['DEC'].values*u.degree, frame='icrs')
        df_final['l'], df_final['b'] = coords_gal.galactic.l.degree, coords_gal.galactic.b.degree
        
        z_mean = df_final['REDSHIFT_FINAL'].mean()
        df_final['residual'] = (df_final['REDSHIFT_FINAL'] - z_mean) / df_final['REDSHIFT_FINAL'].std()

        def model(params, l, b):
            D, l_p, b_p = params
            l_rad, b_rad = np.radians(l), np.radians(b)
            return D * (np.sin(b_rad)*np.sin(b_p) + np.cos(b_rad)*np.cos(b_p)*np.cos(l_rad - l_p))

        x0 = [0.01, np.radians(164), np.radians(-58)]
        res = least_squares(lambda p: model(p, df_final['l'], df_final['b']) - df_final['residual'], x0)

        # 5. Significância
        boot_Ds = []
        for _ in range(1000):
            sample = df_final.sample(frac=1.0, replace=True)
            res_b = least_squares(lambda p: model(p, sample['l'], sample['b']) - 
                                 ((sample['REDSHIFT_FINAL'] - z_mean)/sample['REDSHIFT_FINAL'].std()), x0)
            boot_Ds.append(res_b.x[0])
        
        sigma = np.mean(boot_Ds) / np.std(boot_Ds)

        print("\n" + "="*50)
        print(f"Direção: l = {np.degrees(res.x[1]):.2f}°, b = {np.degrees(res.x[2]):.2f}°")
        print(f"Significância: {abs(sigma):.2f} Sigma")
        print("="*50)

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    auditoria_espacial_multi_catalogo()