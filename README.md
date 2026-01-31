# Teoria da Relatividade Referencial (TRR) - Repositório de Auditoria Científica
# Referential Relativity Theory (RRT) - Scientific Audit Repository

---

## Descrição da Obra / Work Description

### 🇧🇷 Português
Este repositório contém a infraestrutura computacional e os algoritmos de auditoria estatística utilizados para validar a **Teoria da Relatividade Referencial (TRR)**. A TRR propõe uma reformulação hidrodinâmica do espaço-tempo baseada em **Transições de Fase Termodinâmicas**. A teoria substitui entidades hipotéticas (Matéria e Energia Escuras) por um campo temporal viscoso ($\mathcal{T}_{\mu\nu}$) cuja interação com a matéria é governada pela densidade local de energia ($\rho$).

A tese está estruturada em **quatro volumes**, estabelecendo que o universo opera em regimes distintos de viscosidade causal:
1.  **Fase 1 (Saturada):** Regime de alta densidade (Sistema Solar, CERN) onde a TRR é blindada, recuperando a Relatividade Geral e o Modelo Padrão.
2.  **Fase 2 (Transição):** Regime de densidade crítica (Halos Galácticos) onde a viscosidade gera curvas de rotação planas (SPARC).
3.  **Fase 3 (Viscosa):** Regime de vácuo profundo (Vazios Cósmicos) onde o fluxo temporal impulsiona a expansão acelerada.

### 🇺🇸 English
This repository hosts the computational infrastructure and statistical audit algorithms used to validate the **Referential Relativity Theory (RRT)**. RRT proposes a hydrodynamic reformulation of spacetime based on **Thermodynamic Phase Transitions**. The theory replaces hypothetical entities (Dark Matter and Dark Energy) with a viscous temporal field ($\mathcal{T}_{\mu\nu}$) whose interaction with matter is governed by local energy density ($\rho$).

The thesis is structured across **four volumes**, establishing that the universe operates in distinct regimes of causal viscosity:
1.  **Phase 1 (Saturated):** High-density regime (Solar System, CERN) where RRT is shielded, recovering General Relativity and the Standard Model.
2.  **Phase 2 (Transition):** Critical density regime (Galactic Halos) where viscosity generates flat rotation curves (SPARC).
3.  **Phase 3 (Viscous):** Deep vacuum regime (Cosmic Voids) where temporal flow drives accelerated expansion.

---

## 📂 Organização dos Módulos / Module Organization

1.  **Cosmology Core (`/core_cosmology`):**
    * Algoritmos de processamento de grandes catálogos (SDSS DR16Q, Pantheon+, Planck) para extração de significância estatística e validação da Rotação de Cortez ($\omega_p$).
    * *Focus: Statistical significance and Cortez Rotation validation.*

2.  **Experimental & Robustness (`/experimental_robustness`):**
    * Testes de nulidade em ambientes de alta densidade (LAGEOS-2, CMS/CERN) e simulações de dinâmica galáctica (SPARC). Confirmação da **isotropia local** e da validade da Fase 1 (Saturação).
    * *Focus: Null tests, local isotropy confirmation, and galactic dynamics simulations.*

3.  **Critical Falsification Tests (`/critical_falsification`):** 🆕
    * **Munição de Estresse:** Algoritmos desenhados para testar os limites físicos do Modelo Padrão ($\Lambda$CDM). Inclui testes de Causalidade de Eddington (crescimento de Buracos Negros) e Auditoria Topológica do Eixo de Anisotropia.
    * *Focus: Stress tests for Standard Model ($\Lambda$CDM) physical limits, including Eddington Causality and Axis Topological Audit.*

---

## 💾 Declaração de Disponibilidade de Dados / Data Availability Statement

Para garantir a **reprodutibilidade independente** e a integridade da auditoria, este projeto utiliza exclusivamente dados públicos brutos de repositórios oficiais. Nenhum dado foi pré-processado manualmente.
*To ensure **independent reproducibility** and audit integrity, this project exclusively uses raw public data from official repositories. No data was manually pre-processed.*

**Instrução ao Auditor / Auditor Instruction:**
Recomenda-se baixar os arquivos listados abaixo diretamente das fontes oficiais.
*It is recommended to download the files listed below directly from official sources.*

### 1. Cosmologia e Tensão de Hubble (Pantheon+)
* **Fonte/Source:** [GitHub Oficial Pantheon+SH0ES](https://github.com/PantheonPlusSH0ES/Data_Release)
* **Arquivo/File:** `Pantheon+SH0ES.dat`
* **Uso:** Validação da expansão tardia e anisotropia de magnitude.

### 2. Quasares e Estrutura em Larga Escala (SDSS DR16Q)
* **Fonte/Source:** [SDSS eBOSS Algorithms](https://www.sdss.org/dr16/algorithms/qso_catalog/)
* **Arquivo/File:** `DR16Q_Superset_v3.fits` (~1.5 GB)
* **Uso:** Detecção do dipolo de densidade ($51\sigma$) e testes de "Buracos Negros Impossíveis" (Causalidade).

### 3. Curvas de Rotação Galáctica (SPARC)
* **Fonte/Source:** [Case Western Reserve University (SPARC)](http://astroweb.cwru.edu/SPARC/)
* **Arquivo/File:** `SPARC_Database.zip` (Extrair pasta `Rotmod_LTG`)
* **Uso:** Teste de gravidade modificada hidrodinâmica vs. Matéria Escura.

### 4. Radiação Cósmica de Fundo (Planck 2018)
* **Fonte/Source:** [ESA Planck Legacy Archive](https://pla.esac.esa.int/)
* **Dados:** Mapa SMICA (Multipolos baixos $\ell=2,3$).
* **Uso:** Verificação do alinhamento do "Eixo do Mal" com o fluxo de quasares.

### 5. Gravidade Local (LAGEOS-2)
* **Fonte/Source:** [NASA CDDIS](https://cddis.nasa.gov/Data_and_Derived_Products/SLR/Orbit_data.html)
* **Arquivo/File:** Efemérides `.sp3` (ex: `asi.orb.lageos2.251220.v80.sp3`)
* **Uso:** Validação do Princípio de Neutralidade Bariônica (PNB) no Sistema Solar.

---

## 📋 Tabela de Scripts e Evidências / Scripts & Evidence Table

| Script Name | Alvo / Target | Fase (Regime) / Phase | Resultado / Result |
| :--- | :--- | :--- | :--- |
| `trr_sdss_dr16q_51sigma_audit.py` | SDSS DR16Q (Quasars) | **Fase 3 (Viscosa)** | **51.73σ (Anisotropy)** |
| `trr_pantheon_plus_gradient.py` | Pantheon+ (SNe Ia) | **Fase 2/3 (Mista)** | **25.47σ (Gradient)** |
| `trr_planck_cmb_alignment.py` | Planck (CMB) | **Fase 3 (Primordial)** | **98.36% Alignment** |
| `trr_sparc_rotation_curves.py` | SPARC (Galaxies) | **Fase 2 (Transition)** | **5.81 km/s (Residual)** |
| `trr_cern_cms_isotropy_test.py` | CERN/CMS (Muons) | **Fase 1 (Saturated)** | **Isotrópico / Null** |
| `trr_lageos_pnb_shielding.py` | LAGEOS-2 (Gravity) | **Fase 1 (Saturated)** | **0.22σ (Shielded)** |
| `trr_micius_quantum_phase.py` | Micius (Quantum) | **Fase 1 (Saturated)** | **Null / Hardware Limit** |
| `trr_jackknife_stability.py` | Stability Analysis | **Global** | **0.19° Deviation** |
| `trr_3_testes_municao.py` 🆕 | $\Lambda$CDM Limits (Black Holes) | **Causal Violation** | **3978 Failures (100%)** |
| `trr_auditoria_eixo.py` 🆕 | Topological Audit | **Global Geometry** | **82.66% Axis Concentration** |

---

### 🛠️ Requisitos Técnicos / Technical Requirements
Para rodar os scripts, utilize o ambiente **Python 3.11+**. As bibliotecas necessárias são:
* `numpy`, `scipy` (Cálculos tensoriais e estatísticos)
* `pandas` (Processamento de catálogos)
* `astropy` (FITS e Coordenadas Celestes)
* `matplotlib` (Histogramas e Mapas)
* `healpy` (Análise de multipolos CMB - Opcional)

### ⚠️ Notas de Execução / Execution Notes
O pico de **51.73σ** detectado no SDSS refere-se à coerência vetorial dos resíduos anisotrópicos em relação ao modelo $\Lambda$CDM. O algoritmo inclui testes de **Injeção Cega (Blind Injection)** para descartar artefatos numéricos.
*The **51.73σ** peak detected in SDSS refers to the vector coherence of anisotropic residuals relative to the $\Lambda$CDM model. The algorithm includes **Blind Injection** tests to rule out numerical artifacts.*

---
**Autor / Author:** Jean Coutinho Cortez
**Local / Location:** Rio de Janeiro, Brasil 🇧🇷
**Data / Date:** Janeiro / January 2026
