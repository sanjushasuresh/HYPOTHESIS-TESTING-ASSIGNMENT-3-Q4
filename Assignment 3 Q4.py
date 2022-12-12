# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 16:54:49 2022

@author: LENOVO
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
df = pd.read_csv("Costomer+OrderForm.csv")
df.head
df.shape
df.Phillippines.value_counts()
df.Indonesia.value_counts()
df.Malta.value_counts()
df.India.value_counts()
TC = np.array([[271,267,269,280],[29,33,31,20]])
TC
from scipy import stats
X = stats.chi2_contingency(TC)
p_val = X[1]
p_val
# H0 = Customer order forms defective % does not vary by centre
# H1 = Customer order forms defective % varies by centre
if p_val<0.05:
    print("H0 is rejected, H1 is accepted")
else:
    print("H1 is rejected, H0 is accepted")
# Since H1 is rejected and H0 is accepted, we can conclude that 
# the customer order forms defective % does not vary by centre