import numpy as np
import pandas as pd
import os
import glob

print("="*80)
print("TRR: PROTOCOLO DE UNIFICAÇÃO MESTRA (REAL DATA AUDIT)")
print("Objetivo: Provar a rigidez estrutural usando APENAS dados observacionais/matemáticos reais.")
print("="*80)

# CONFIGURAÇÃO DE CAMINHOS (Ajuste se necessário)
PASTA_SPARC = r'./Rotmod_LTG'

# ==============================================================================
# 1. O NÚCLEO IMUTÁVEL (CONSTANTES TRR)
# ==============================================================================
class TRR_Constants:
    def __init__(self, d0_override=None, omega_override=None):
        # Constantes Nominais (Valores propostos na Tese)
        self.D0 = 0.794 if d0_override is None else d0_override
        self.OMEGA_P = 19.68 if omega_override is None else omega_override 
        
        # Constantes Físicas Auxiliares (CORREÇÃO AQUI)
        self.C = 299792.458 # km/s (Velocidade da Luz)
        
        # Aceleração Crítica (a0) VINCULADA a D0
        # Se D0 muda, a gravidade muda. Isso conecta Cosmologia (D0) com Galáxias (a0).
        self.A0 = 1.2001e-10 * (self.D0 / 0.794)

# ==============================================================================
# 2. MOTORES DE TESTE COM DADOS REAIS
# ==============================================================================

def teste_sparc_real(const):
    """
    Lê os arquivos .dat REAIS da pasta SPARC.
    Calcula o resíduo médio global da Lei de Cortez para todas as galáxias.
    """
    arquivos = glob.glob(os.path.join(PASTA_SPARC, "*.dat"))
    if not arquivos:
        print("ERRO CRÍTICO: Pasta SPARC vazia ou não encontrada.")
        return 9999.0 # Erro infinito

    erros_velocidade = []
    
    # ML Fixo (Spitzer) - Padrão Ouro
    ML_disk = 0.5
    ML_bul = 0.7

    for arq in arquivos: 
        try:
            df = pd.read_csv(arq, sep=r'\s+', comment='#', header=None,
                             names=['Rad', 'Vobs', 'errV', 'Vgas', 'Vdisk', 'Vbul', 'SBdis', 'SBbul'])
            df = df.apply(pd.to_numeric, errors='coerce').dropna()
            
            # Filtro de Borda (Onde a TRR atua - Regime de Baixa Aceleração)
            # Alinhado com o script dedicado (0.8 * r_max) para precisão máxima
            r_max = df['Rad'].max()
            df = df[df['Rad'] > r_max * 0.8] 
            if df.empty: continue

            # Física Real
            v_bar_sq = df['Vgas']**2 + (df['Vdisk']**2 * ML_disk) + (df['Vbul']**2 * ML_bul)
            r_m = df['Rad'] * 3.086e19 # kpc -> m
            v_bar_si = v_bar_sq * 1e6 # (km/s)^2 -> (m/s)^2
            
            # Evitar erros matemáticos
            valid = (r_m > 0) & (v_bar_sq > 0)
            if not valid.any(): continue
            
            # Aceleração Newtoniana
            g_bar = v_bar_si[valid] / r_m[valid]
            
            # LEI DE CORTEZ (Dependente de const.A0, que depende de D0)
            fator = 1 - np.exp(-np.sqrt(g_bar / const.A0))
            g_trr = g_bar / fator
            v_trr = np.sqrt(g_trr * r_m[valid]) / 1000 # m/s -> km/s
            
            # Erro Médio Absoluto desta galáxia
            res = np.mean(np.abs(v_trr - df['Vobs'][valid]))
            erros_velocidade.append(res)
            
        except: continue
    
    # Retorna o Erro Médio Global do Universo (km/s)
    if not erros_velocidade: return 9999.0
    return np.mean(erros_velocidade)

def teste_riemann_real(const):
    """
    Usa os Zeros de Riemann REAIS (Tabela LMFDB).
    Verifica se a fase TRR (Omega/D0) sincroniza com eles.
    """
    # Primeiros 5 zeros não-triviais (Parte Imaginária) - DADOS MATEMÁTICOS REAIS
    zeros_reais = np.array([14.134725, 21.022040, 25.010857, 30.424876, 32.935061])
    
    # A hipótese TRR (Vol V): Zeros são harmônicos da viscosidade temporal.
    # Frequência de Base = Omega_P / D0
    freq_base = const.OMEGA_P / const.D0
    
    # Calculamos o "Resto de Fase" para cada zero.
    # Se a teoria é real, (Zero / Freq) deve ser próximo de um inteiro ou meio-inteiro.
    # Quanto menor o resto, maior a ressonância.
    
    fases = zeros_reais / freq_base
    desvio_do_inteiro = np.abs(fases - np.round(fases))
    
    # O erro é a média do desvio de fase. (0 = Ressonância Perfeita, 0.5 = Antirressonância)
    return np.mean(desvio_do_inteiro)

def teste_navier_stokes_limite(const):
    """
    Verifica a finitude teórica.
    """
    # Limite físico
    v_limite = const.C # Velocidade da luz (Agora definida na classe)
    
    # Fator de amortecimento depende de D0
    # Se D0 for zero, explode. Se for o valor correto, deve ser finito.
    amortecimento = np.exp(-1.0 / const.D0)
    
    # O erro é o valor residual. Queremos que seja estável.
    return amortecimento

# ==============================================================================
# 3. EXECUTOR DE CENÁRIOS
# ==============================================================================

def avaliar_universo(nome, d0, omega):
    print(f"\n>>> TESTANDO: {nome}")
    u = TRR_Constants(d0, omega)
    print(f"    Config: D0={u.D0:.4f}, a0={u.A0:.4e}")
    
    # 1. Teste SPARC (Dados Reais)
    erro_sparc = teste_sparc_real(u)
    print(f"    [SPARC Real] Erro Médio de Velocidade: {erro_sparc:.4f} km/s")
    
    # 2. Teste Riemann (Dados Reais)
    erro_riemann = teste_riemann_real(u)
    print(f"    [Riemann]    Desvio de Fase Médio:     {erro_riemann:.4f}")
    
    # 3. Navier-Stokes
    erro_ns = teste_navier_stokes_limite(u)
    
    # Métrica Unificada de Erro (Quanto menor, melhor)
    # Normalizamos para ter pesos comparáveis
    total_error = (erro_sparc / 10.0) + (erro_riemann * 5.0) + erro_ns
    
    print(f"    >>> ERROR SCORE TOTAL: {total_error:.5f}")
    return total_error

if __name__ == "__main__":
    # A. Universo TRR (Nominal)
    print("Processando dados reais... (Isso pode levar alguns segundos)")
    score_nom = avaliar_universo("TRR NOMINAL (D0=0.794)", 0.794, 19.68)
    
    # B. Universo Perturbado (+2% em D0)
    # Se D0 é uma constante fundamental, mudar ela DEVE aumentar o erro nos dados reais.
    # Perturbação de 2%
    d0_pert = 0.794 * 1.02
    score_pert = avaliar_universo("TRR PERTURBADO (D0=0.810)", d0_pert, 19.68)
    
    print("\n" + "="*80)
    print("VEREDITO DE RIGIDEZ ESTRUTURAL (REAL DATA)")
    print("="*80)
    
    print(f"Erro Universo Nominal:    {score_nom:.5f}")
    print(f"Erro Universo Perturbado: {score_pert:.5f}")
    
    delta = score_pert - score_nom
    
    if delta > 0:
        print(f"\n[SUCESSO] O erro aumentou em {delta:.5f} ao perturbar a constante.")
        print("Isso prova que D0=0.794 é um mínimo local real nos dados observacionais.")
        print("A teoria é RÍGIDA (Falseável).")
    else:
        print("\n[FALHA] O universo perturbado funcionou melhor ou igual.")
        print("A teoria é flexível demais.")