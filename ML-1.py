from fastai.imports import *
from fastai.structured import *

from pandas_summary import DataFrameSummary
from sklearn.ensemble import RandomForestRegressor
from IPython.display import display

from sklearn import metrics

# 1. a better way of .format. This way allows functions inside the curly brackets{}
name = 'Jeremy'
age = 43
f'Hello {name.upper()}, you are {age}'

# 1.1 we can even store PATH of a directory and use {PATH} to read files
# 1.2 notes on read_csv: use low_memory and parse_date every time.
df_raw = pd.read_csv(f'{PATH}Train.csv', low_memory=False, parse_date=['saledate'])

# 2. a trick of display long columns lists
df_raw.tail().transpose()

# 3. Fix Stationary problem: log transformation:
df_raw.SalePrice = np.log(df_raw.SalePrice)

# 4. a fast way to initiate a ML model 
m = RandomForestRegressor(n_jobs=-1)
m.fit(df_raw.drop('SalePrice', axis=1), df_raw.SalsPrice)

# 5. Fastai tools
# 5.1 strip datetimes and assing them to different columns
add_datepart(df_raw, 'saledate')

# 6. CleanData
# 6.1 Access date parts (You can access any part after the dt.)
df_raw.saledate.dt.
# 6.2 Access catgorical parts (here it returns all categoriies)
df_raw.UsageBand.cat.categories
df
# 6.2.1 We can reorder the categories (to make the order of the corersponiding numerics more meaningful)
df_raw.UsageBand.cat.set_categoreis(['High, 'Medium', 'Low'], ordered=True, inplace=True)




