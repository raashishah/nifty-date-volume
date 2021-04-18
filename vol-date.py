import os
import pandas as pd

entries = os.listdir()

df_data = {
    'date': [],
    'call_volume': [],
    'put_volume': []
}

for sheet in entries:
    if 'bhav.csv' in sheet:
        # Initializing variables
        CE_total = 0
        PE_total = 0
        # Reading the sheet
        data = pd.read_csv(sheet, usecols=['TIMESTAMP', 'SYMBOL', 'OPTION_TYP', 'VAL_INLAKH'])
        # Iterating through the sheet for 'NIFTY'
        for i in data.index:
            if data['SYMBOL'][i] == 'NIFTY':
                # Finding CE values
                if data['OPTION_TYP'][i] == 'CE':
                    # Adding total value (in lakhs) for CE
                    CE_total += int(data['VAL_INLAKH'][i])
                # Finding PE values
                elif data['OPTION_TYP'][i] == 'PE':
                    # Adding total value (in lakhs) for PE
                    PE_total += int(data['VAL_INLAKH'][i])
        df_data['date'].append(data['TIMESTAMP'][0])
        df_data['call_volume'].append(CE_total)
        df_data['put_volume'].append(CE_total)
print(df_data)
df = pd.DataFrame(df_data)
df.to_csv(f'final.csv')
