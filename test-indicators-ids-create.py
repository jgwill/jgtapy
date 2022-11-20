import pandas as pd
import jgtapy
df=pd.read_csv('sample-pds-history.csv')
dfi=jgtapy.Indicators.jgt_create_ids_indicators_as_instance(df)

asdf=jgtapy.Indicators.jgt_create_ids_indicators_as_dataframe(df,cleanupOriginalColumn=True)
print(asdf)


fb89=asdf[asdf['fb89']==True]
print(fb89)