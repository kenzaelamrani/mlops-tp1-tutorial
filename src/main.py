import pandas as pd
import numpy as np

print("Environnement MLOps prêt ✅")

data = {
    "x": [1, 2, 3, 4, 5],
    "y": [2, 4, 6, 8, 10]
}

df = pd.DataFrame(data)

print(df)
print("Moyenne de y :", np.mean(df["y"]))