import pandas as pd
# Para visualizar datos de forma grafica.
import matplotlib.pyplot as plt
# Para graficos estadisticos.
import seaborn as sns # type: ignore

# Read file ".csv".
df = pd.read_csv("exercises\\graphics\\mustache\\mustache.csv")

# Create graphic.
sns.boxplot(x="category", y="value", data=df)

# Show graphic.
plt.show()