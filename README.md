# Teoria da Relatividade Referencial (TRR) - Repositório de Auditoria Científica
# Referential Relativity Theory (RRT) - Scientific Audit Repository

---

## Descrição da Obra

Este repositório contém a infraestrutura computacional e os algoritmos de auditoria estatística utilizados para validar a **Teoria da Relatividade Referencial (TRR)**. A TRR propõe uma reformulação hidrodinâmica do espaço-tempo baseada em **Transições de Fase Termodinâmicas**. A teoria substitui entidades hipotéticas (Matéria e Energia Escuras) por um campo temporal viscoso ($\mathcal{T}_{\mu\nu}$) cuja interação com a matéria é governada pela densidade local de energia ($\rho$).

A tese está estruturada em **quatro volumes**, estabelecendo que o universo opera em regimes distintos de viscosidade causal:
1.  **Fase 1 (Saturada):** Regime de alta densidade (Sistema Solar, CERN) onde a TRR é blindada, recuperando a Relatividade Geral e o Modelo Padrão.
2.  **Fase 2 (Transição):** Regime de densidade crítica (Halos Galácticos) onde a viscosidade gera curvas de rotação planas (SPARC).
3.  **Fase 3 (Viscosa):** Regime de vácuo profundo (Vazios Cósmicos) onde o fluxo temporal impulsiona a expansão acelerada.

### 📂 Organização dos Módulos

1.  **Cosmology Core (`/cosmology_core`):** Algoritmos de processamento de grandes catálogos (SDSS DR16Q, Pantheon+, Planck) para extração de significância estatística e validação da Rotação de Cortez ($\omega_p$).
2.  **Phase Transition Dynamics (`/phase_transition`):** Simulações da função de blindagem $K(\rho)$ e modelagem das curvas de rotação galáctica sem matéria escura.
3.  **Null Tests & Shielding (`/null_tests`):** Testes de robustez em ambientes de alta densidade (LAGEOS-2, CMS/CERN) para confirmar a **isotropia local** e a validade da Fase 1 (Saturação).

### 🛠️ Requisitos Técnicos
Para rodar os scripts, utilize o ambiente **Python 3.11+**. As bibliotecas necessárias são:
* `numpy`, `scipy` (Cálculos tensoriais e estatísticos)
* `pandas` (Processamento de catálogos)
* `astropy` (FITS e Coordenadas Celestes)
* `matplotlib` (Histogramas e Mapas)
* `healpy` (Análise de multipolos CMB)

### ⚠️ Notas de Execução
O pico de **51.73σ** detectado no SDSS refere-se à coerência vetorial dos resíduos anisotrópicos em relação ao modelo $\Lambda$CDM. O algoritmo inclui testes de **Injeção Cega (Blind Injection)** para descartar artefatos numéricos.

---

## Work Description

This repository hosts the computational infrastructure and statistical audit algorithms used to validate the **Referential Relativity Theory (RRT)**. RRT proposes a hydrodynamic reformulation of spacetime based on **Thermodynamic Phase Transitions**. The theory replaces hypothetical entities (Dark Matter and Dark Energy) with a viscous temporal field ($\mathcal{T}_{\mu\nu}$) whose interaction with matter is governed by local energy density ($\rho$).

The thesis is structured across **four volumes**, establishing that the universe operates in distinct regimes of causal viscosity:
1.  **Phase 1 (Saturated):** High-density regime (Solar System, CERN) where RRT is shielded, recovering General Relativity and the Standard Model.
2.  **Phase 2 (Transition):** Critical density regime (Galactic Halos) where viscosity generates flat rotation curves (SPARC).
3.  **Phase 3 (Viscous):** Deep vacuum regime (Cosmic Voids) where temporal flow drives accelerated expansion.

### 📂 Module Organization

1.  **Cosmology Core (`/cosmology_core`):** Processing algorithms for large catalogs (SDSS DR16Q, Pantheon+, Planck) to extract statistical significance and validate the Cortez Rotation ($\omega_p$).
2.  **Phase Transition Dynamics (`/phase_transition`):** Simulations of the shielding function $K(\rho)$ and modeling of galactic rotation curves without dark matter.
3.  **Null Tests & Shielding (`/null_tests`):** Robustness tests in high-density environments (LAGEOS-2, CMS/CERN) to confirm **local isotropy** and the validity of Phase 1 (Saturation).

### 🛠️ Technical Requirements
To run the scripts, use a **Python 3.11+** environment. Required libraries include:
* `numpy`, `scipy` (Tensorial calculations)
* `pandas` (Catalog processing)
* `astropy` (FITS and Coordinates)
* `matplotlib` (Histograms and Heatmaps)
* `healpy` (CMB multipole analysis)

### ⚠️ Execution Notes
The **51.73σ** peak detected in SDSS refers to the vector coherence of anisotropic residuals relative to the $\Lambda$CDM model. The algorithm includes **Blind Injection** tests to rule out numerical artifacts.

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

---
**Autor / Author:** Jean Coutinho Cortez
**Local / Location:** Rio de Janeiro, Brasil 🇧🇷
**Data / Date:** Janeiro / January 2026
