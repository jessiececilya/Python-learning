import seaborn as sb, numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
#data_binom =binom.rvs(size=10,n=20,p=0.8)
data_binom = binom.rvs(n=20,p=0.8,loc=0,size=100)
print(data_binom)
ax = sb.distplot(data_binom,kde=True,color='blue',hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='Binomial', ylabel='Frequency')
plt.show()