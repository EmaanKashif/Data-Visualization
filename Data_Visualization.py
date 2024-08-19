import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb

data1 = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
             2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 
             2022, 2023, 2024],
    'Exchange_Rate': [51.90, 63.5, 60.5, 57.75, 57.8, 59.7, 60.4, 60.83, 81.1, 84.1, 
                      85.75, 88.6, 96.5, 107.2, 103, 105.20, 104.6, 110.01, 122.09, 
                      163.75, 168.88, 179.16, 225.40, 278, 278.50]
}


data = pd.DataFrame(data1)
print(data)

sb.set_style("whitegrid")
plt.figure(figsize=(14, 7))
plt.plot(data['Year'], data['Exchange_Rate'], marker='o', color='blue', linestyle='-', linewidth=2)
plt.title('Dollar Trend in Pakistan (2000 - 2024)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Exchange Rate', fontsize=14)
plt.annotate('Financial Crisis', xy=(2008, 81.1), xytext=(2005, 100),
             arrowprops=dict(facecolor='black', arrowstyle="->"),
             fontsize=12, color='red')
plt.annotate('Economic Instability', xy=(2018, 122.09), xytext=(2015, 150),
             arrowprops=dict(facecolor='black', arrowstyle="->"),
             fontsize=12, color='red')
plt.annotate('Economic Challenges', xy=(2022, 225.40), xytext=(2019, 250),
             arrowprops=dict(facecolor='black', arrowstyle="->"),
             fontsize=12, color='red')
plt.grid(True)
plt.show()

