#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
df= pd.read_excel("Tarea1P2.xlsx")
for i in range(len(df.columns)+1):
    avg_growth=round((df.iloc[-1,1:i]/df.iloc[0,1:i])**(1/(df.iloc[-1,0]-df.iloc[0,0]))-1,4)
    
df["Tendency1"] = df.iloc[0,1]
df["Tendency2"] = df.iloc[0,2]
df["Tendency3"] = df.iloc[0,3]
df["Tendency4"] = df.iloc[0,4]

for i in range(1,len(df)):

    df.loc[i, "Tendency1"] = df.loc[i-1,"Tendency1"]*(1+avg_growth[0])
    df.loc[i, "Tendency2"] = df.loc[i-1,"Tendency2"]*(1+avg_growth[1])
    df.loc[i, "Tendency3"] = df.loc[i-1,"Tendency3"]*(1+avg_growth[2])
    df.loc[i, "Tendency4"] = df.loc[i-1,"Tendency4"]*(1+avg_growth[3])
    
df["Ciclo1"] = np.log(df["pais 1"])-np.log(df["Tendency1"])
df["Ciclo2"] = np.log(df["pais 2"])-np.log(df["Tendency2"])
df["Ciclo3"] = np.log(df["pais 3"])-np.log(df["Tendency3"])
df["Ciclo4"] = np.log(df["pais 4"])-np.log(df["Tendency4"])

avg_ciclo1=np.average(df["Ciclo1"])
avg_ciclo2=np.average(df["Ciclo2"])
avg_ciclo3=np.average(df["Ciclo3"])
avg_ciclo4=np.average(df["Ciclo4"])

avg_ciclo= pd.Series({'pais 1':avg_ciclo1,
                      'pais 2':avg_ciclo2,
                      'pais 3':avg_ciclo3,
                      "pais 4":avg_ciclo4})


# In[10]:


df1=pd.Series.sort_values(avg_ciclo).to_frame("avg cicle")
df2=pd.Series.sort_values(avg_growth,ascending=False).to_frame("avg growth")
df1,df2

