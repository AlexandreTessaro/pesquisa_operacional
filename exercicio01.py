import pulp

# Criação do modelo
model = pulp.LpProblem("Maximizar_Lucro_Farmaceutica", pulp.LpMaximize)

# Variáveis de decisão
x1 = pulp.LpVariable("M1_F1", lowBound=0, cat='Continuous')
x2 = pulp.LpVariable("M1_F2", lowBound=0, cat='Continuous')
x3 = pulp.LpVariable("M2_F1", lowBound=0, cat='Continuous')
x4 = pulp.LpVariable("M2_F2", lowBound=0, cat='Continuous')
x5 = pulp.LpVariable("M2_F3", lowBound=0, cat='Continuous')
x6 = pulp.LpVariable("M3_F1", lowBound=0, cat='Continuous')
x7 = pulp.LpVariable("M3_F2", lowBound=0, cat='Continuous')

# Função objetivo (Maximizar o lucro)
model += (
    1.5 * x1 +
    1.3 * x2 +
    1.8 * x3 +
    1.6 * x4 +
    1.1 * x5 +
    1.4 * x6 +
    1.2 * x7
), "Lucro_Total"

# Restrições de recursos
model += (2*x1 + 1*x2 + 3*x3 + 2*x4 + 1*x5 + 2*x6 + 1*x7 <= 2500), "Composto_A"
model += (3*x1 + 4*x2 + 2*x3 + 3*x4 + 1*x5 + 1*x6 + 0*x7 <= 3000), "Composto_B"
model += (1*x1 + 2*x2 + 1*x3 + 2*x4 + 1*x5 + 3*x6 + 4*x7 <= 2000), "Composto_C"

# Resolver o problema
model.solve()

# Exibir resultados
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lucro Total: R$ {pulp.value(model.objective):.2f}")
for var in model.variables():
    print(f"{var.name} = {var.varValue:.2f}")
