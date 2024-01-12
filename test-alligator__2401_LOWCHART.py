#%% Imports
from jgtapy import Indicators
import pandas as pd
import os

# %%
## Instrument load
instrument = 'WHEATF'
instrument = 'SOYF'
instrument = 'EUR/USD'
timeframe = "W1"
timeframe = "M1"
pov = instrument.replace('/','-') +"_" + timeframe
povfn = pov + '.csv'
jgtpy_data = os.getenv('JGTPY_DATA','/mnt/c/usr/src/_jgt/data')
povfullpath=  jgtpy_data+"/pds/" + povfn
dfsrc = pd.read_csv(povfullpath, index_col=0, parse_dates=True)
# %%
dfsrc

#%% lenght 
len(dfsrc)

#%% Indicators
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