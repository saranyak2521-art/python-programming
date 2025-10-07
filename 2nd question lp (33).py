import pandas as pd
import numpy as np

# Generate random salaries
data = {"Name": ["A","B","C","D","E"], 
        "Salary": np.random.randint(5000, 99000, 5)}
df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# Filter condition: Salary > 50000
filtered = df[df["Salary"] > 50000]
print("\nFiltered DataFrame (Salary > 50000):\n", filtered)
