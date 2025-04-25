# 📊 Programação Linear com Simplex — Desafios no Contexto Farmacêutico

Este repositório reúne três problemas de **Programação Linear** aplicados à área farmacêutica, modelados para serem resolvidos com o método **Simplex** usando Python (`scipy.optimize.linprog`). As questões possuem níveis de dificuldade crescente e foco em **produção**, **logística** e **formulação de produtos**.

---

## ⚙️ Objetivo

Praticar modelagem matemática e resolução de problemas reais da indústria farmacêutica utilizando o método Simplex. Os cenários abordam:

- Alocação ótima de recursos
- Logística de distribuição
- Otimização de fórmulas nutricionais

---

## ✅ Questão Fácil – Produção de Medicamentos (7 variáveis)

### Enunciado

Uma farmacêutica produz três medicamentos:

- **Paracetamol (M1)**
- **Ibuprofeno (M2)**
- **Dipirona (M3)**

Eles podem ser produzidos em **duas fábricas (F1 e F2)**, e o Ibuprofeno também pode ser terceirizado (**F3**). Cada combinação de medicamento e fábrica consome diferentes quantidades dos compostos A, B e C, e gera um lucro unitário diferente:

| Med. | Fábrica | Comp. A (g) | Comp. B (g) | Comp. C (g) | Lucro (R$) |
|------|---------|-------------|-------------|-------------|------------|
| M1   | F1      | 2           | 3           | 1           | 1.50       |
| M1   | F2      | 1           | 4           | 2           | 1.30       |
| M2   | F1      | 3           | 2           | 1           | 1.80       |
| M2   | F2      | 2           | 3           | 2           | 1.60       |
| M2   | F3      | 1           | 1           | 1           | 1.10       |
| M3   | F1      | 2           | 1           | 3           | 1.40       |
| M3   | F2      | 1           | 0           | 4           | 1.20       |

**Recursos disponíveis:**

- Composto A: 2500g  
- Composto B: 3000g  
- Composto C: 2000g  

**Variáveis de decisão:**

- \( x_1 \): M1 produzido na F1  
- \( x_2 \): M1 produzido na F2  
- \( x_3 \): M2 produzido na F1  
- \( x_4 \): M2 produzido na F2  
- \( x_5 \): M2 produzido na F3  
- \( x_6 \): M3 produzido na F1  
- \( x_7 \): M3 produzido na F2  

**Objetivo:**
Maximizar o lucro total respeitando as restrições de recursos.

---

## 🚚 Questão Média – Distribuição de Vacinas (9 variáveis)

### Enunciado

Uma farmacêutica precisa distribuir **três tipos de vacinas (V1, V2, V3)** para **três regiões (R1, R2, R3)**. Cada combinação vacina-região tem um custo logístico por dose. As vacinas têm estoques limitados, e as regiões têm demandas mínimas.

| Vacina | R1 (R$) | R2 (R$) | R3 (R$) | Estoque |
|--------|---------|---------|---------|---------|
| V1     | 1.20    | 1.40    | 1.60    | 2500    |
| V2     | 1.00    | 1.30    | 1.50    | 3000    |
| V3     | 1.10    | 1.20    | 1.70    | 2000    |

**Demandas mínimas por região:**

- R1: 2000 doses  
- R2: 2500 doses  
- R3: 2200 doses  

**Variáveis de decisão:**

- \( x_{11} \): doses de V1 para R1  
- \( x_{12} \): doses de V1 para R2  
- \( x_{13} \): doses de V1 para R3  
- \( x_{21} \): doses de V2 para R1  
- \( x_{22} \): doses de V2 para R2  
- \( x_{23} \): doses de V2 para R3  
- \( x_{31} \): doses de V3 para R1  
- \( x_{32} \): doses de V3 para R2  
- \( x_{33} \): doses de V3 para R3  

**Objetivo:**
Minimizar o custo total de envio, respeitando estoques e demandas.

---

## 🧪 Questão Difícil – Formulação de Suplementos (20 variáveis)

### Enunciado

Uma farmácia de manipulação quer desenvolver **4 suplementos personalizados (S1 a S4)**, com diferentes combinações de **5 ingredientes (A a E)**. Cada ingrediente fornece nutrientes diferentes e tem um custo por grama. O objetivo é atender aos requisitos nutricionais com o menor custo.

| Ingrediente | Ferro | Vitamina C | Cálcio | Zinco | Custo (R$/g) |
|-------------|-------|------------|--------|-------|--------------|
| A           | 4     | 1          | 2      | 1     | 0.40         |
| B           | 3     | 4          | 1      | 0     | 0.35         |
| C           | 2     | 2          | 5      | 1     | 0.50         |
| D           | 1     | 3          | 2      | 4     | 0.45         |
| E           | 5     | 0          | 3      | 2     | 0.30         |

**Requisitos mínimos por suplemento:**

- Ferro ≥ 40mg  
- Vitamina C ≥ 30mg  
- Cálcio ≥ 35mg  
- Zinco ≥ 20mg  

**Variáveis de decisão:**

- \( x_{ij} \): quantidade (g) do ingrediente \( i \in \{A, B, C, D, E\} \) no suplemento \( j \in \{S1, S2, S3, S4\} \)

Total de 20 variáveis.

**Objetivo:**
Minimizar o custo total das formulações, garantindo que cada suplemento atenda aos requisitos nutricionais.

---
