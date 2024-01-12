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
i.fractals('fractal_up', 'fractal_down')
i.fractals21('fractal_up21', 'fractal_down21')

# %%
i.df
# %%
dfi = i.df

# %%
h70=dfi.head(70).copy()

# %%
h70

# %%
h70.to_csv('h70f.csv')
# %%
dfi.dropna(inplace=True)
# %%
h70.dropna(inplace=True)
# %%
h70.to_csv('h70fdropped.csv')

# %%