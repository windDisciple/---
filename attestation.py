import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

data.loc[data['whoAmI'] == 'robot', 'robot'] = True
data.loc[data['whoAmI'] == 'human', 'robot'] = False
data.loc[data['whoAmI'] == 'human', 'human'] = True
data.loc[data['whoAmI'] == 'robot', 'human'] = False
data

