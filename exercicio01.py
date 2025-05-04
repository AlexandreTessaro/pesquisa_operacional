!pip install pulp tabulate matplotlib

import pulp
from tabulate import tabulate
import matplotlib.pyplot as plt

# Criação do modelo de otimização
model = pulp.LpProblem("Maximizar_Lucro_Farmaceutica", pulp.LpMaximize)

# Variáveis de decisão (quantidade produzida de cada medicamento em cada fábrica)
x1 = pulp.LpVariable("x1", lowBound=0)  # M1 em F1
x2 = pulp.LpVariable("x2", lowBound=0)  # M1 em F2
x3 = pulp.LpVariable("x3", lowBound=0)  # M2 em F1
x4 = pulp.LpVariable("x4", lowBound=0)  # M2 em F2
x5 = pulp.LpVariable("x5", lowBound=0)  # M2 em F3
x6 = pulp.LpVariable("x6", lowBound=0)  # M3 em F1
x7 = pulp.LpVariable("x7", lowBound=0)  # M3 em F2

# Função objetivo: maximizar o lucro total
model += (
    1.5 * x1 + 1.3 * x2 + 1.8 * x3 +
    1.6 * x4 + 1.1 * x5 + 1.4 * x6 + 1.2 * x7
), "Lucro_Total"

# Restrições de uso dos compostos
model += (2*x1 + 1*x2 + 3*x3 + 2*x4 + 1*x5 + 2*x6 + 1*x7 <= 2500), "Limite_Composto_A"
model += (3*x1 + 4*x2 + 2*x3 + 3*x4 + 1*x5 + 1*x6 + 0*x7 <= 3000), "Limite_Composto_B"
model += (1*x1 + 2*x2 + 1*x3 + 2*x4 + 1*x5 + 3*x6 + 4*x7 <= 2000), "Limite_Composto_C"

# Resolver o modelo
model.solve()

# Mapeamento descritivo para visualização
label_map = {
    "x1": "M1 (Paracetamol) - Fábrica 1",
    "x2": "M1 (Paracetamol) - Fábrica 2",
    "x3": "M2 (Ibuprofeno) - Fábrica 1",
    "x4": "M2 (Ibuprofeno) - Fábrica 2",
    "x5": "M2 (Ibuprofeno) - Fábrica 3 (Terceirizada)",
    "x6": "M3 (Dipirona) - Fábrica 1",
    "x7": "M3 (Dipirona) - Fábrica 2"
}

# Coletar resultados
status = pulp.LpStatus[model.status]
lucro_total = pulp.value(model.objective)
variaveis = [(label_map[var.name], var.varValue) for var in model.variables()]

# ==== Resultado com melhor visual UX ====
print("="*50)
print("🔍  RESULTADO DA OTIMIZAÇÃO")
print("="*50)
print(f"📊 Status da Solução: \033[1m{status}\033[0m")
print(f"💰 Lucro Máximo Obtido: \033[1mR$ {lucro_total:,.2f}\033[0m\n")

print("📦 Distribuição Otimizada da Produção:\n")
print(tabulate(variaveis, headers=["🧪 Medicamento e Fábrica", "📈 Unidades Produzidas"], tablefmt="fancy_grid"))

print("\n📌 Resumo Estratégico:")
print("- A produção foi ajustada para maximizar o lucro total.")
print("- Foram priorizadas combinações medicamento-fábrica com maior retorno por grama.")
print("- Todas as restrições de matéria-prima foram respeitadas.")
print("- O gráfico a seguir ilustra visualmente a alocação ideal da produção.\n")

# ==== Gráfico de barras ====
nomes = [v[0] for v in variaveis]
valores = [v[1] for v in variaveis]

plt.figure(figsize=(10, 6))
bars = plt.bar(nomes, valores)
plt.title("📊 Produção Otimizada por Medicamento e Fábrica")
plt.xlabel("Medicamento e Fábrica")
plt.ylabel("Unidades Produzidas")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
