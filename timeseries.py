from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('stock.csv')
df = pd.DataFrame(data, columns = ['ValueDate', 'Price'])
# Set the Date as Index
df['ValueDate'] = pd.to_datetime(df['ValueDate'])
df.index = df['ValueDate']
print(df.index)
del df['ValueDate']
df.plot(figsize=(15, 6))
plt.show()