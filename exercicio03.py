import pulp

# Criação do modelo
model = pulp.LpProblem("Maximizar_Lucro_Suplementos", pulp.LpMaximize)

# Variáveis de decisão
x = [pulp.LpVariable(f"S{i+1}", lowBound=0, cat='Continuous') for i in range(10)]

# Dados
preco_venda = [120, 140, 110, 130, 135, 125, 115, 120, 130, 140]

# Custo por grama dos ingredientes
custo_ingrediente = {
    "Ferro": 0.40,
    "Vitamina C": 0.35,
    "Cálcio": 0.50,
    "Zinco": 0.45,
    "Cafeína": 0.30,
    "Magnésio": 0.25,
    "Ômega 3": 0.60,
    "Proteína Isolada": 0.55
}

# Estoque máximo (g)
estoque = {
    "Ferro": 200,
    "Vitamina C": 200,
    "Cálcio": 200,
    "Zinco": 150,
    "Cafeína": 100,
    "Magnésio": 150,
    "Ômega 3": 120,
    "Proteína Isolada": 200
}

# Consumo de ingredientes por unidade de suplemento
consumo = {
    "Ferro": [8,10,5,12,6,8,4,10,7,9],
    "Vitamina C": [6,8,4,5,7,9,6,7,8,5],
    "Cálcio": [12,10,15,10,5,7,10,6,8,9],
    "Zinco": [5,4,3,5,7,6,2,4,3,5],
    "Cafeína": [4,6,3,2,5,6,3,2,4,3],
    "Magnésio": [8,6,7,5,6,5,7,6,5,6],
    "Ômega 3": [6,5,4,3,5,6,4,5,4,5],
    "Proteína Isolada": [10,12,8,9,7,8,9,7,8,9]
}

# Calculando o lucro unitário de cada suplemento
lucro_unitario = []
for i in range(10):
    custo = sum(consumo[ing][i] * custo_ingrediente[ing] for ing in consumo)
    lucro = preco_venda[i] - custo
    lucro_unitario.append(lucro)

# Função objetivo: Maximizar o lucro total
model += pulp.lpSum(lucro_unitario[i] * x[i] for i in range(10)), "Lucro_Total"

# Restrições de estoque para cada ingrediente
for ing in consumo:
    model += pulp.lpSum(consumo[ing][i] * x[i] for i in range(10)) <= estoque[ing], f"Estoque_{ing}"

# Resolver o problema
model.solve()

# Exibir resultados
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lucro Total: R$ {pulp.value(model.objective):.2f}")
for var in model.variables():
    print(f"{var.name} = {var.varValue:.2f}")
