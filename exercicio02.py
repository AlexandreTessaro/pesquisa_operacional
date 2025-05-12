import pulp
from tabulate import tabulate
import matplotlib.pyplot as plt

# Criação do modelo
model = pulp.LpProblem("Minimizar_Custo_Distribuicao_Vacinas", pulp.LpMinimize)

# Variáveis de decisão
x11 = pulp.LpVariable("V1_R1", lowBound=0)
x12 = pulp.LpVariable("V1_R2", lowBound=0)
x13 = pulp.LpVariable("V1_R3", lowBound=0)
x21 = pulp.LpVariable("V2_R1", lowBound=0)
x22 = pulp.LpVariable("V2_R2", lowBound=0)
x23 = pulp.LpVariable("V2_R3", lowBound=0)
x31 = pulp.LpVariable("V3_R1", lowBound=0)
x32 = pulp.LpVariable("V3_R2", lowBound=0)
x33 = pulp.LpVariable("V3_R3", lowBound=0)

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

# Mapeamento descritivo para visualização
label_map = {
    "V1_R1": "Vacina 1 - Região 1",
    "V1_R2": "Vacina 1 - Região 2",
    "V1_R3": "Vacina 1 - Região 3",
    "V2_R1": "Vacina 2 - Região 1",
    "V2_R2": "Vacina 2 - Região 2",
    "V2_R3": "Vacina 2 - Região 3",
    "V3_R1": "Vacina 3 - Região 1",
    "V3_R2": "Vacina 3 - Região 2",
    "V3_R3": "Vacina 3 - Região 3",
}

# Coletar resultados
status = pulp.LpStatus[model.status]
custo_total = pulp.value(model.objective)
variaveis = [(label_map[var.name], var.varValue) for var in model.variables()]

# ==== Resultado com melhor visual UX ====
print("="*50)
print("🚚  RESULTADO DA OTIMIZAÇÃO DE DISTRIBUIÇÃO")
print("="*50)
print(f"📊 Status da Solução: \033[1m{status}\033[0m")
print(f"💸 Custo Total Mínimo: \033[1mR$ {custo_total:,.2f}\033[0m\n")

print("🏥 Distribuição Otimizada de Vacinas:\n")
print(tabulate(variaveis, headers=["💉 Vacina e Região", "🚚 Doses Enviadas"], tablefmt="fancy_grid"))

print("\n📌 Resumo Estratégico:")
print("- A alocação foi otimizada para minimizar o custo total de distribuição.")
print("- Respeitou-se o limite de estoque de cada vacina.")
print("- A demanda mínima de cada região foi atendida.")
print("- O gráfico a seguir ilustra visualmente o plano de distribuição ideal.\n")

# ==== Gráfico de barras ====
nomes = [v[0] for v in variaveis]
valores = [v[1] for v in variaveis]

plt.figure(figsize=(10, 6))
bars = plt.bar(nomes, valores, color='mediumseagreen')
plt.title("📦 Distribuição Otimizada de Vacinas por Região")
plt.xlabel("Vacina e Região")
plt.ylabel("Doses Enviadas")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
