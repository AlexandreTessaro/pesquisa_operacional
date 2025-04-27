# 📊 Programação Linear com Simplex — Desafios no Contexto Farmacêutico

Este repositório reúne três problemas de Programação Linear aplicados à área farmacêutica, modelados para serem resolvidos com o método Simplex usando Python (`scipy.optimize.linprog`).  
As questões possuem níveis de dificuldade crescente e foco em produção, logística e formulação de produtos.

---

## ⚙️ Objetivo

Praticar modelagem matemática e resolução de problemas reais da indústria farmacêutica utilizando o método Simplex. Os cenários abordam:

- Alocação ótima de recursos
- Logística de distribuição
- Otimização de produção e maximização de lucro

---

## ✅ Questão Fácil – Produção de Medicamentos (7 variáveis)

### Enunciado

Uma farmacêutica produz três medicamentos:

- **Paracetamol (M1)**
- **Ibuprofeno (M2)**
- **Dipirona (M3)**

Eles podem ser produzidos em duas fábricas (**F1** e **F2**), e o **Ibuprofeno** também pode ser terceirizado (**F3**).  
Cada combinação de medicamento e fábrica consome diferentes quantidades dos compostos A, B e C, e gera um lucro unitário diferente:

| Medicamento | Fábrica | Comp. A (g) | Comp. B (g) | Comp. C (g) | Lucro (R$) |
|:-----------:|:-------:|:-----------:|:-----------:|:-----------:|:----------:|
| M1          | F1      | 2           | 3           | 1           | 1.50       |
| M1          | F2      | 1           | 4           | 2           | 1.30       |
| M2          | F1      | 3           | 2           | 1           | 1.80       |
| M2          | F2      | 2           | 3           | 2           | 1.60       |
| M2          | F3      | 1           | 1           | 1           | 1.10       |
| M3          | F1      | 2           | 1           | 3           | 1.40       |
| M3          | F2      | 1           | 0           | 4           | 1.20       |

**Recursos disponíveis:**

- Composto A: 2500g
- Composto B: 3000g
- Composto C: 2000g

**Variáveis de decisão:**

- `x1`: M1 produzido na F1
- `x2`: M1 produzido na F2
- `x3`: M2 produzido na F1
- `x4`: M2 produzido na F2
- `x5`: M2 produzido na F3
- `x6`: M3 produzido na F1
- `x7`: M3 produzido na F2

**Objetivo:**  
Maximizar o lucro total respeitando as restrições de recursos.

---

## 🚚 Questão Média – Distribuição de Vacinas (9 variáveis)

### Enunciado

Uma farmacêutica precisa distribuir três tipos de vacinas (**V1**, **V2**, **V3**) para três regiões (**R1**, **R2**, **R3**).  
Cada combinação vacina-região tem um custo logístico por dose.  
As vacinas têm estoques limitados, e as regiões têm demandas mínimas.

| Vacina | R1 (R$) | R2 (R$) | R3 (R$) | Estoque |
|:------:|:-------:|:-------:|:-------:|:-------:|
| V1     | 1.20    | 1.40    | 1.60    | 2500    |
| V2     | 1.00    | 1.30    | 1.50    | 3000    |
| V3     | 1.10    | 1.20    | 1.70    | 2000    |

**Demandas mínimas por região:**

- R1: 2000 doses
- R2: 2500 doses
- R3: 2200 doses

**Variáveis de decisão:**

- `x11`: doses de V1 para R1
- `x12`: doses de V1 para R2
- `x13`: doses de V1 para R3
- `x21`: doses de V2 para R1
- `x22`: doses de V2 para R2
- `x23`: doses de V2 para R3
- `x31`: doses de V3 para R1
- `x32`: doses de V3 para R2
- `x33`: doses de V3 para R3

**Objetivo:**  
Minimizar o custo total de envio, respeitando estoques e demandas.

---

## 🧪 Questão Difícil – Otimização de Produção e Lucro em Suplementos Nutricionais (10 variáveis)

### Enunciado

Uma farmácia de manipulação está planejando a produção de 10 suplementos nutricionais personalizados (**S1** a **S10**), cada um com uma fórmula fixa composta por 8 ingredientes:

- Ferro
- Vitamina C
- Cálcio
- Zinco
- Cafeína
- Magnésio
- Ômega 3
- Proteína Isolada

Cada ingrediente possui um custo por grama e uma quantidade máxima disponível em estoque.  
Cada suplemento possui um preço de venda fixo.

**Ingredientes e Estoques Máximos:**

| Ingrediente     | Estoque (g) |
|:----------------:|:-----------:|
| Ferro             | 200         |
| Vitamina C        | 200         |
| Cálcio            | 200         |
| Zinco             | 150         |
| Cafeína           | 100         |
| Magnésio          | 150         |
| Ômega 3           | 120         |
| Proteína Isolada  | 200         |

**Preço de Venda dos Suplementos:**

| Suplemento | Preço de Venda (R$) |
|:----------:|:------------------:|
| S1         | 120                |
| S2         | 140                |
| S3         | 110                |
| S4         | 130                |
| S5         | 135                |
| S6         | 125                |
| S7         | 115                |
| S8         | 120                |
| S9         | 130                |
| S10        | 140                |

**Fórmula de Composição dos Suplementos (g por unidade):**

| Ingrediente        | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 |
|:------------------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|
| Ferro              | 8  | 10 | 5  | 12 | 6  | 8  | 4  | 10 | 7  | 9   |
| Vitamina C         | 6  | 8  | 4  | 5  | 7  | 9  | 6  | 7  | 8  | 5   |
| Cálcio             | 12 | 10 | 15 | 10 | 5  | 7  | 10 | 6  | 8  | 9   |
| Zinco              | 5  | 4  | 3  | 5  | 7  | 6  | 2  | 4  | 3  | 5   |
| Cafeína            | 4  | 6  | 3  | 2  | 5  | 6  | 3  | 2  | 4  | 3   |
| Magnésio           | 8  | 6  | 7  | 5  | 6  | 5  | 7  | 6  | 5  | 6   |
| Ômega 3            | 6  | 5  | 4  | 3  | 5  | 6  | 4  | 5  | 4  | 5   |
| Proteína Isolada   | 10 | 12 | 8  | 9  | 7  | 8  | 9  | 7  | 8  | 9   |

**Custo por Grama dos Ingredientes:**

| Ingrediente        | Custo (R$/g) |
|:------------------:|:-----------:|
| Ferro              | 0.40        |
| Vitamina C         | 0.35        |
| Cálcio             | 0.50        |
| Zinco              | 0.45        |
| Cafeína            | 0.30        |
| Magnésio           | 0.25        |
| Ômega 3            | 0.60        |
| Proteína Isolada   | 0.55        |

**Variáveis de decisão:**

- `x1`: unidades a produzir de S1
- `x2`: unidades a produzir de S2
- `x3`: unidades a produzir de S3
- `x4`: unidades a produzir de S4
- `x5`: unidades a produzir de S5
- `x6`: unidades a produzir de S6
- `x7`: unidades a produzir de S7
- `x8`: unidades a produzir de S8
- `x9`: unidades a produzir de S9
- `x10`: unidades a produzir de S10

**Objetivo:**  
Maximizar o lucro total, respeitando os limites de estoque de cada ingrediente.

---


