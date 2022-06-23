import numpy as np
import math
import random
import pandas as pd

lam = 12


def gen_arrival():
    return -np.log(1-np.random.uniform(low=0.0, high=1.0)) / lam


df = pd.DataFrame(columns=['Среднее время между прибытиями'])

testing = np.zeros(1000)
num = np.zeros(1000)
for i in range(1000):
    while testing[i] < 1:
        num[i] += 1
        testing[i] += gen_arrival()
    a = pd.Series([num[i]], index=df.columns)
    df = df.append(a, ignore_index=True)

df.to_excel('Proverka.xlsx')
