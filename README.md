# Teoria da Relatividade Referencial (TRR) - Repositório de Auditoria Científica
# Referential Relativity Theory (RRT) - Scientific Audit Repository

---

## 🚀 Motor Cosmológico TRR / RRT Cosmological Engine (Interactive Audit)
Para facilitar a auditoria imediata sem necessidade de ambiente Python local, disponibilizamos o Motor TRR (Streamlit App).
To facilitate immediate auditing without the need for a local Python environment, we provide the RRT Engine (Streamlit App).

Acesso / Access: https://trr-motor.streamlit.app/

Função / Function: Validação de curvas de rotação galáctica e lentes gravitacionais com emissão de relatórios técnicos de auditoria que quantificam a falha do modelo ΛCDM. / Validation of galactic rotation curves and gravitational lensing, generating technical audit reports that quantify the failure of the ΛCDM model.

---

## Descrição da Obra / Work Description

### 🇧🇷 Português
Este repositório contém a infraestrutura computacional e os algoritmos de auditoria estatística utilizados para validar a **Teoria da Relatividade Referencial (TRR)**. A TRR propõe uma reformulação hidrodinâmica do espaço-tempo baseada em **Transições de Fase Termodinâmicas**. A teoria substitui entidades hipotéticas (Matéria e Energia Escuras) por um campo temporal viscoso ($\mathcal{T}_{\mu\nu}$) cuja interação com a matéria é governada pela densidade local de energia ($\rho$).

A tese está estruturada em **quatro volumes**, estabelecendo que o universo opera em regimes distintos de viscosidade causal:
1. **Fase 1 (Saturada):** Regime de alta densidade (Sistema Solar, CERN) onde a TRR é blindada, recuperando a Relatividade Geral e o Modelo Padrão.
2. **Fase 2 (Transição):** Regime de densidade crítica (Halos Galácticos) onde a viscosidade gera curvas de rotação planas (SPARC).
3. **Fase 3 (Viscosa):** Regime de vácuo profundo (Vazios Cósmicos) onde o fluxo temporal impulsiona a expansão acelerada.

### 🇺🇸 English
This repository hosts the computational infrastructure and statistical audit algorithms used to validate the **Referential Relativity Theory (RRT)**. RRT proposes a hydrodynamic reformulation of spacetime based on **Thermodynamic Phase Transitions**. The theory replaces hypothetical entities (Dark Matter and Dark Energy) with a viscous temporal field ($\mathcal{T}_{\mu\nu}$) whose interaction with matter is governed by local energy density ($\rho$).

The thesis is structured across **four volumes**, establishing that the universe operates in distinct regimes of causal viscosity:
1. **Phase 1 (Saturated):** High-density regime (Solar System, CERN) where RRT is shielded, recovering General Relativity and the Standard Model.
2. **Phase 2 (Transition):** Critical density regime (Galactic Halos) where viscosity generates flat rotation curves (SPARC).
3. **Phase 3 (Viscous):** Deep vacuum regime (Cosmic Voids) where temporal flow drives accelerated expansion.

---

## 📂 Organização dos Módulos / Module Organization

1. **Cosmology Core (`/core_cosmology`):**
    * Algoritmos de processamento de grandes catálogos (SDSS DR16Q, Pantheon+, Planck) para extração de significância estatística e validação da Rotação de Cortez ($\omega_p$).
    * *Focus: Statistical significance and Cortez Rotation validation.*

2. **Experimental & Robustness (`/experimental_robustness`):**
    * Testes de nulidade em ambientes de alta densidade (LAGEOS-2, CMS/CERN) e simulações de dinâmica galáctica (SPARC). Confirmação da **isotropia local** e da validade da Fase 1 (Saturação).
    * *Focus: Null tests, local isotropy confirmation, and galactic dynamics simulations.*

3. **Critical Falsification Tests (`/critical_falsification`):**
    * **Munição de Estresse:** Algoritmos desenhados para testar os limites físicos do Modelo Padrão ($\Lambda$CDM). Inclui testes de Causalidade de Eddington e Auditoria Topológica.
    * *Focus: Stress tests for Standard Model ($\Lambda$CDM) physical limits, including Eddington Causality and Axis Topological Audit.*

---

## 💾 Declaração de Disponibilidade de Dados / Data Availability Statement

Para garantir a **reprodutibilidade independente**, este projeto utiliza exclusivamente dados públicos brutos de repositórios oficiais. Nenhum dado foi pré-processado manualmente para favorecer a teoria.
*To ensure **independent reproducibility**, this project exclusively uses raw public data from official repositories. No data was manually pre-processed to favor the theory.*

**Instrução ao Auditor / Auditor Instruction:**
Recomenda-se baixar os arquivos listados abaixo diretamente das fontes oficiais.
*It is recommended to download the files listed below directly from official sources.*

1. **Pantheon+SH0ES:** [GitHub Oficial](https://github.com/PantheonPlusSH0ES/Data_Release)
2. **SDSS DR16Q:** [SDSS eBOSS Algorithms](https://www.sdss.org/dr16/algorithms/qso_catalog/) (`DR16Q_Superset_v3.fits`)
3. **SPARC Database:** [Case Western Reserve University](http://astroweb.cwru.edu/SPARC/)
4. **Planck 2018:** [ESA Planck Legacy Archive](https://pla.esac.esa.int/) (Mapa SMICA)

---

## 📋 Tabela de Scripts e Evidências / Scripts & Evidence Table

| Script Name | Alvo / Target | Fase (Regime) | Resultado / Result |
| :--- | :--- | :--- | :--- |
| `trr_sdss_dr16q_51sigma_audit.py` | SDSS DR16Q | **Fase 3** | **51.73σ (Anisotropy)** |
| `trr_pantheon_plus_gradient.py` | Pantheon+ | **Fase 2/3** | **25.47σ (Gradient)** |
| `trr_planck_cmb_alignment.py` | Planck (CMB) | **Fase 3** | **98.36% Alignment** |
| `trr_sparc_rotation_curves.py` | SPARC | **Fase 2** | **1.33% Error (Residual)** |
| `trr_ruptura_cronologia.py` | Quasars $z > 5$ | **Fase 3** | **100% Causal Violation (ΛCDM)** |
| `trr_fadiga_gravitacional.py` | LIGO / GW | **Impedância** | **23% Distance Divergence** |
| `trr_cern_cms_isotropy_test.py` | CERN/CMS | **Fase 1** | **Isotrópico / Null** |
| `trr_lageos_pnb_shielding.py` | LAGEOS-2 | **Fase 1** | **0.22σ (Shielded)** |

> **Nota de Auditoria:** Os resultados de **51.73σ** e a falha de causalidade em quasares foram validados sob o protocolo de **Hubble Detrending**, isolando o sinal viscoso puro de artefatos de expansão métrica.

---

### 🛠️ Requisitos Técnicos / Technical Requirements
Utilize **Python 3.11+** com as bibliotecas: `numpy`, `scipy`, `pandas`, `astropy`, `matplotlib` e `fpdf`.

---
**Autor / Author:** Jean Coutinho Cortez
**Local / Location:** Rio de Janeiro, Brasil 🇧🇷
**Data / Date:** Janeiro / January 2026
