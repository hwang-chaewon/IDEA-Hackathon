# -*- coding: utf-8 -*-
"""병기데이터정리(hj).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PCMtZsdgZ98l7LBNkV74C1x_XwvPCBE2
"""

from google import colab

import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
import os

os.chdir('/content/drive/MyDrive/대외활동/암빅데이터경진대회/Validation')

df = pd.read_csv('/content/drive/MyDrive/대외활동/암빅데이터경진대회/Validation/항암환자new.csv')

df.tail(5)

df.iloc[[0],[6,7,8,9,10,11,12,13,14,15,16,17]]

df.iloc[[0],[18,19,20,21,22,23,24,25,26,27,28,29,30]]

df.iloc[[0],[31,32,33]]

t=[]

for i in range(3346):
  st_t=df.iloc[[i],[6,7,8,9,10,11,12,13,14,15,16,17]]
  np_t=st_t.to_numpy()
  np_t=np_t[0]
  stage_t=np.where(np_t > 0)[0]
  y=stage_t.tolist()
  if not y:
    t.append(0)
    
  else:
    t.append(y[-1])

df["병기(t)"]=t

n=[]

for i in range(3346):
  st_n=df.iloc[[i],[18,19,20,21,22,23,24,25,26,27,28,29,30]]
  np_n=st_n.to_numpy()
  np_n=np_n[0]
  stage_n=np.where(np_n > 0)[0]
  y=stage_n.tolist()
  if not y:
    n.append(0)
    
  else:
    n.append(y[-1])

df["병기(n)"]=n

m=[]

for i in range(3346):
  st_m=df.iloc[[i],[31,32,33]]
  np_m=st_m.to_numpy()
  np_m=np_m[0]
  stage_m=np.where(np_m > 0)[0]
  y=stage_m.tolist()
  if not y:
    m.append(0)
    
  else:
    m.append(y[-1])

df["병기(m)"]=m

"""기존 병기 열 들 전부 제거"""

df.drop(['TX',
       'T0', 'T1', 'T1mi', 'T1a', 'T1b', 'T1c', 'T2', 'T2a', 'T2b', 'T3', 'T4',
       'Nx', 'N1mi', 'N1', 'N1a', 'N1b', 'N1c', 'N2', 'N2a', 'N2b', 'N3',
       'N3a', 'N3b', 'N3c', 'M1', 'M1a', 'M1b'], axis=1,inplace=True)

df.tail(5)

df.to_csv("train.csv", index=None)