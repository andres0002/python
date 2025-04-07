import pandas as pd
# Para visualizar datos de forma grafica.
import matplotlib.pyplot as plt
# Para graficos estadisticos.
import seaborn as sns # type: ignore

# Read file ".csv".
df = pd.read_csv("exercises\\graphics\\bar\\cofla_income.csv")

# Create graphic.
sns.barplot(x="source", y="income", data=df)

# Total de ingresos.
total = df["income"].sum()
print(f"Total income: {total}.")

# Show graphic.
plt.show()