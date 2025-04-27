import pulp

# Criação do modelo
model = pulp.LpProblem("Minimizar_Custo_Distribuicao_Vacinas", pulp.LpMinimize)

# Variáveis de decisão
x11 = pulp.LpVariable("V1_R1", lowBound=0, cat='Continuous')
x12 = pulp.LpVariable("V1_R2", lowBound=0, cat='Continuous')
x13 = pulp.LpVariable("V1_R3", lowBound=0, cat='Continuous')
x21 = pulp.LpVariable("V2_R1", lowBound=0, cat='Continuous')
x22 = pulp.LpVariable("V2_R2", lowBound=0, cat='Continuous')
x23 = pulp.LpVariable("V2_R3", lowBound=0, cat='Continuous')
x31 = pulp.LpVariable("V3_R1", lowBound=0, cat='Continuous')
x32 = pulp.LpVariable("V3_R2", lowBound=0, cat='Continuous')
x33 = pulp.LpVariable("V3_R3", lowBound=0, cat='Continuous')

# Função objetivo (Minimizar o custo total)
model += (
    1.20*x11 + 1.40*x12 + 1.60*x13 +
    1.00*x21 + 1.30*x22 + 1.50*x23 +
    1.10*x31 + 1.20*x32 + 1.70*x33
), "Custo_Total"

# Restrições de estoque
model += (x11 + x12 + x13 <= 2500), "Estoque_V1"
model += (x21 + x22 + x23 <= 3000), "Estoque_V2"
model += (x31 + x32 + x33 <= 2000), "Estoque_V3"

# Restrições de demanda mínima
model += (x11 + x21 + x31 >= 2000), "Demanda_R1"
model += (x12 + x22 + x32 >= 2500), "Demanda_R2"
model += (x13 + x23 + x33 >= 2200), "Demanda_R3"

# Resolver o problema
model.solve()

# Exibir resultados
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Custo Total: R$ {pulp.value(model.objective):.2f}")
for var in model.variables():
    print(f"{var.name} = {var.varValue:.2f}")
