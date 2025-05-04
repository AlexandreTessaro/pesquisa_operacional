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

Uma indústria farmacêutica está planejando sua produção para o próximo mês e precisa decidir quantas unidades de cada medicamento serão fabricadas para maximizar o lucro, respeitando as limitações de matérias-primas disponíveis.

A empresa fabrica três tipos de medicamentos:

- M1: Paracetamol
- M2: Ibuprofeno
- M3: Dipirona

Esses medicamentos podem ser produzidos em duas fábricas próprias (F1 e F2) e, no caso do Ibuprofeno (M2), também pode ser terceirizado em uma fábrica externa (F3).

Cada medicamento, em cada fábrica, consome quantidades específicas de três compostos químicos:

- Composto A
- Composto B
- Composto C

Além disso, cada combinação medicamento-fábrica gera um lucro unitário diferente.
O objetivo é encontrar a melhor estratégia de produção, respeitando os limites de uso dos compostos:

- Composto A: 2500 g
- Composto B: 3000 g
- Composto C: 2000 g

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

- x1 = unidades de M1 produzidas em F1
- x2 = unidades de M1 produzidas em F2
- x3 = unidades de M2 produzidas em F1
- x4 = unidades de M2 produzidas em F2
- x5 = unidades de M2 produzidas em F3 (terceirizada)
- x6 = unidades de M3 produzidas em F1
- x7 = unidades de M3 produzidas em F2

**Objetivo:**  
Maximizar o lucro total respeitando as restrições de recursos.

**Max Z=1,5x1​+1,3x2​+1,8x3​+1,6x4​+1,1x5​+1,4x6​+1,2x7​**

**Restrições de Recursos**

**Composto A:**
2x1 ​+ 1x2 ​+ 3x3 ​+ 2x4​ + 1x5​ + 2x6​ + 1x7​ ≤ 2500

**Composto B:** 
3x1​ + 4x2​ + 2x3​ + 3x4 ​+ 1x5 ​+ 1x6 ​+ 0x7 ​≤3000

**Composto C:** 
1x1 ​+ 2x2 ​+ 1x3 ​+ 2x4 ​+ 1x5 ​+ 3x6 ​+ 4x7 ​≤ 2000

**Restrição de não negatividade:**

x1​,x2​,x3​,x4​,x5​,x6​,x7 ​≥ 0

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


