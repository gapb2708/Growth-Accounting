#!/usr/bin/env python
# coding: utf-8

# In[160]:


import pandas as pd
import numpy as np
df= pd.read_excel("Tarea1P3.xlsx", sheet_name="pais1")
df["α"]=1-df["W"]*df["L"]/df["Y"]
df["A"]=df["Y"]/(df["K"]**df["α"]*df["L"]**(1-df["α"]))
df["LogY"]=np.log(df["Y"])
df["LogK"]=np.log(df["K"])
df["LogL"]=np.log(df["L"])
df["LogA"]=np.log(df["A"])
α=df.loc[1,"α"]

for i in range(1,len(df)):
    df.loc[i, "ΔY"] = df.loc[i,"LogY"]-df.loc[i-1,"LogY"]
    df.loc[i, "ΔK"] = df.loc[i,"LogK"]-df.loc[i-1,"LogK"]
    df.loc[i, "ΔL"] = df.loc[i,"LogL"]-df.loc[i-1,"LogL"]
    df.loc[i, "ΔA"] = df.loc[i,"LogA"]-df.loc[i-1,"LogA"]

first_25years = pd.Series({'first ΔY':df.loc[0:24, 'ΔY'].sum(),
                      'first ΔK':df.loc[0:24, 'ΔK'].sum(),
                      'first ΔL':df.loc[0:24, 'ΔL'].sum(),
                      "first ΔA":df.loc[0:24, 'ΔA'].sum()})
last_25years = pd.Series({'last ΔY':df.loc[25:50, 'ΔY'].sum(),
                      'last ΔK':df.loc[25:50, 'ΔK'].sum(),
                      'last ΔL':df.loc[25:50, 'ΔL'].sum(),
                      "last ΔA":df.loc[25:50, 'ΔA'].sum()})
KContribution=pd.Series({'first 25 years': α*first_25years[1]/first_25years[0] ,
                      'last 25 years': α*last_25years[1]/last_25years[0]})
LContribution=pd.Series({'first 25 years': (1-α)*first_25years[2]/first_25years[0] ,
                      'last 25 years': (1-α)*last_25years[2]/last_25years[0]})
AContribution=pd.Series({'first 25 years': first_25years[3]/first_25years[0] ,
                      'last 25 years': last_25years[3]/last_25years[0]})

df1=KContribution.to_frame().transpose()
df2=LContribution.to_frame().transpose()
df3=AContribution.to_frame().transpose()
df1=df1.merge(df2, how="outer")
df1=df1.merge(df3, how="outer")
df1["Contribution"]=("K Contribution","L Contribution","A Contribution")
df1=df1[["Contribution","first 25 years", "last 25 years"]]
df1


# In[161]:


df=pd.read_excel("Tarea1P3.xlsx",sheet_name="pais2")
df["α"]=1-df["W"]*df["L"]/df["Y"]
df["A"]=df["Y"]/(df["K"]**df["α"]*df["L"]**(1-df["α"]))
df["LogY"]=np.log(df["Y"])
df["LogK"]=np.log(df["K"])
df["LogL"]=np.log(df["L"])
df["LogA"]=np.log(df["A"])
α=df.loc[1,"α"]

for i in range(1,len(df)):
    df.loc[i, "ΔY"] = df.loc[i,"LogY"]-df.loc[i-1,"LogY"]
    df.loc[i, "ΔK"] = df.loc[i,"LogK"]-df.loc[i-1,"LogK"]
    df.loc[i, "ΔL"] = df.loc[i,"LogL"]-df.loc[i-1,"LogL"]
    df.loc[i, "ΔA"] = df.loc[i,"LogA"]-df.loc[i-1,"LogA"]

first_25years = pd.Series({'first ΔY':df.loc[0:24, 'ΔY'].sum(),
                      'first ΔK':df.loc[0:24, 'ΔK'].sum(),
                      'first ΔL':df.loc[0:24, 'ΔL'].sum(),
                      "first ΔA":df.loc[0:24, 'ΔA'].sum()})
last_25years = pd.Series({'last ΔY':df.loc[25:50, 'ΔY'].sum(),
                      'last ΔK':df.loc[25:50, 'ΔK'].sum(),
                      'last ΔL':df.loc[25:50, 'ΔL'].sum(),
                      "last ΔA":df.loc[25:50, 'ΔA'].sum()})
KContribution=pd.Series({'first 25 years': α*first_25years[1]/first_25years[0] ,
                      'last 25 years': α*last_25years[1]/last_25years[0]})
LContribution=pd.Series({'first 25 years': (1-α)*first_25years[2]/first_25years[0] ,
                      'last 25 years': (1-α)*last_25years[2]/last_25years[0]})
AContribution=pd.Series({'first 25 years': first_25years[3]/first_25years[0] ,
                      'last 25 years': last_25years[3]/last_25years[0]})

df1=KContribution.to_frame().transpose()
df2=LContribution.to_frame().transpose()
df3=AContribution.to_frame().transpose()
df1=df1.merge(df2, how="outer")
df1=df1.merge(df3, how="outer")
df1["Contribution"]=("K Contribution","L Contribution","A Contribution")
df1=df1[["Contribution","first 25 years", "last 25 years"]]
df1
