import pandas as pd
# Para visualizar datos de forma grafica.
import matplotlib.pyplot as plt
# Para graficos estadisticos.
import seaborn as sns # type: ignore

# Read file ".csv".
df = pd.read_csv("exercises\\graphics\\dispersion\\dispersion.csv")

# Create graphic.
sns.scatterplot(x="time", y="money", data=df)

# Show graphic.
plt.show()