import numpy as np
import pandas as pd
from sklearn import datasets
#
from sklearn import model_selection
from sklearn import metrics
import matplotlib.pylab as plt

dataset = datasets.fetch_olivetti_faces()
print(dataset.DESCR)

print(dataset.keys()) #dict_keys(['data', 'images', 'target', 'DESCR'])
df = pd.DataFrame(dataset.data)
df['target'] = dataset.target
print(df.loc[:20])