import numpy as np
import pickle
import os

key=os.listdir('../katakana_datasets/Capitals64/test')
print(len(key))
print(key)

ran=np.arange(46)





d = {k: np.random.permutation(ran) for k in key}
print(d)
with open('../katakana_datasets/Capitals64/test_dict/dict.pkl', 'wb') as f1:
    pickle.dump(d, f1)
for i in d:
    print(d[i])
    print(type(d[i]))





