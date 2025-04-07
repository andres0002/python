import pandas as pd
# Para visualizar datos de forma grafica.
import matplotlib.pyplot as plt
# Para graficos estadisticos.
import seaborn as sns # type: ignore

# Read file ".csv".
df = pd.read_csv("exercises\\graphics\\linear\\farts.csv")

# Create graphic.
sns.lineplot(x="date", y="farts", data=df)

# Create point.
plt.plot("01-07", 16, "o")

# Show graphic.
plt.show()