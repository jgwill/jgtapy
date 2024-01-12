#%% Imports
from jgtapy import Indicators
import pandas as pd

# %%
dfsrc = pd.read_csv('pds.csv', index_col=0, parse_dates=True)
# %%
dfsrc
# %%

# try:
#   # Check if 'Date' is the index column
#   if dfsrc.index.name == 'Date':
#     # Reset the index to remove 'Date' as the index column
#     dfsrc = dfsrc.reset_index()
# except Exception:
#   pass

ldfsrc=len(dfsrc)

i=Indicators(dfsrc)
# %%

# i.awesome_oscillator(column_name='ao')
# i.accelerator_oscillator( column_name= 'ac')
# %%
i.ao_ac_oscillator('ao','ac')


# %%
dfi = i.df
# %%
h70=dfi.head(70).copy()
# %%
h70

# %%
h70.to_csv('h70.csv')
# %%
dfi.dropna(inplace=True)
# %%
h70.dropna(inplace=True)
# %%
h70.to_csv('h70dropped.csv')

# %%
