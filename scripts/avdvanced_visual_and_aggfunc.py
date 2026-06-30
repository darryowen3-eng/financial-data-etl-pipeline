#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("perfect_clean_data.csv")

groupcode_by_rate = (df.groupby("Currency_Code")["Exchange_Rate"]
            .sum().sort_values(ascending=False).reset_index(name = 'Total_Rates'))
print(groupcode_by_rate)

# Clearly state what goes on the X and Y axes
groupcode_by_rate.plot(x='Currency_Code', y='Total_Rates', kind='bar', color='skyblue', edgecolor='black')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df['month_exchanged'] = pd.to_datetime(df['Transaction_Date']).dt.month_name()


exchagebymonth = (df.groupby('month_exchanged')['Exchange_Rate']
                  .sum()
                  .reset_index(name='Total_Rates'))

# 3. Define the correct chronological order for months
month_order = [
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
]

exchagebymonth['month_exchanged'] = pd.Categorical(
    exchagebymonth['month_exchanged'], 
    categories=month_order, 
    ordered=True
)
exchagebymonth = exchagebymonth.sort_values('month_exchanged')
print(exchagebymonth)

plt.figure(figsize=(10, 5)) 

plt.plot(
    exchagebymonth['month_exchanged'], 
    exchagebymonth['Total_Rates'], 
    marker='o',            
    color='#1f77b4',      
    linewidth=2.5,    
    markersize=8              
)


plt.title("MONTHLY EXCHANGE RATE VOLUME TRENDS (2026)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("MONTH OF TRANSACTION", fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel("TOTAL EXCHANGE VALUE", fontsize=11, fontweight='bold', labelpad=10)
plt.xticks(rotation=45)       
plt.grid(True, linestyle='--', alpha=0.6) 
plt.tight_layout()         
plt.show()


# 1. Create your excellent pivot table
report = pd.pivot_table(
    df,
    index = "month_exchanged",
    columns = "Currency_Code",
    values = "Exchange_Rate",
    aggfunc = "sum",
    fill_value = 0
)

month_order = [
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
]
report = report.reindex(month_order)
print(report)


# In[ ]:




