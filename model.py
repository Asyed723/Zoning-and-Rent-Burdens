#Models

#libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

#create dfs
census=pd.read_csv('data/burden_clean.csv')
wrluri=pd.read_stata('data/wrluri.dta')

#aggregate wrluri to metro areas
wrluri_metro=(
    wrluri.dropna(subset=['cbsacode18', 'WRLURI18'])
    .groupby('cbsacode18')
    .apply(lambda x: pd.Series({
        'WRLURI18': np.average(x['WRLURI18'], 
                               weights=x['weight_cbsa'].fillna(1)),
        'num_municipalities': len(x),
        'cbsatitle': x['cbsatitle18'].iloc[0]
        }))
    .reset_index()
    )

#force msa code to numeric
census['msa_code']=pd.to_numeric(census['msa_code'], errors='coerce')
wrluri_metro['cbsacode18']=pd.to_numeric(wrluri_metro['cbsacode18'],
                                         errors='coerce')

