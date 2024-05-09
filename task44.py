# В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид.

# Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data)

data.loc[data['whoAmI'] == 'robot', 'robot'] = '1'
data.loc[data['whoAmI'] == 'human', 'human'] = '1'
data = data.fillna(0)

print(data[data.columns[1:3]])