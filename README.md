# 📊 Programação Linear com Simplex — Desafios no Contexto Farmacêutico

Este repositório contém três problemas de Programação Linear aplicados à área farmacêutica, com níveis de dificuldade **fácil**, **médio** e **difícil**, prontos para serem resolvidos com o método **Simplex**, usando bibliotecas como `scipy.optimize.linprog`.

## ⚙️ Objetivo

Explorar e praticar técnicas de modelagem matemática utilizando o método Simplex para resolução de problemas reais do setor farmacêutico, abordando temas como:

- Produção de medicamentos
- Logística e distribuição de vacinas
- Formulação nutricional de suplementos

---

## 📁 Problemas

### ✅ 1. Produção Otimizada de Medicamentos (Fácil - 7 variáveis)

Simula a produção de três medicamentos (Paracetamol, Ibuprofeno e Dipirona) em diferentes fábricas, cada uma com rendimentos e custos distintos. O objetivo é **maximizar o lucro**, respeitando as restrições de insumos (compostos A, B e C).

> **Número de variáveis:** 7  
> **Tipo:** Maximização  
> **Tema:** Alocação de recursos e produção

---

### 🚚 2. Distribuição de Vacinas (Médio - 9 variáveis)

Simula o envio de três tipos de vacinas para três regiões distintas, cada uma com custos logísticos diferentes e exigências mínimas de entrega. O objetivo é **minimizar o custo total de transporte**.

> **Número de variáveis:** 9  
> **Tipo:** Minimização  
> **Tema:** Logística e distribuição

---

### 🧪 3. Formulação de Suplementos Personalizados (Difícil - 20 variáveis)

Modela a formulação de quatro suplementos diferentes com cinco ingredientes cada. Cada ingrediente contribui com diferentes nutrientes e possui custos distintos. O objetivo é **minimizar o custo de produção**, respeitando os requisitos nutricionais de cada suplemento.

> **Número de variáveis:** 20  
> **Tipo:** Minimização  
> **Tema:** Composição de produtos / Engenharia de alimentos

---

## 📌 Requisitos para Resolução

Você pode resolver esses problemas usando Python com a biblioteca `scipy`. Instale os pacotes necessários com:

```bash
pip install scipy numpy
