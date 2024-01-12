#%% Imports
from jgtapy import Indicators
import pandas as pd

# %%
dfsrc = pd.read_csv('pds.csv', index_col=0, parse_dates=True)
# %%
dfsrc

#%% lenght 
len(dfsrc)

i=Indicators(dfsrc)
# %%
i.alligator()


# %%
i.df
# %%
dfi = i.df

# %%
h70=dfi.head(70).copy()

# %%
h70

# %%
h70.to_csv('h70a.csv')
# %%
dfi.dropna(inplace=True)
# %%
h70.dropna(inplace=True)
# %%
h70.to_csv('h70adropped.csv')

# %%