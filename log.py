import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

data = pd.read_csv(
    r'C:\Users\jaina\project_tekzen3\Serverlogs.csv', sep=',')


# data['Date first seen'] = pd.to_datetime(
# data['Date first seen']) + pd.DateOffset(days=1)  # Modifed timestamps as needed
# data.to_parquet('data_parquet_SL', index=False)
# data.to_parquet('data_parquet_modifiedSL', index=False) #converting the file to parquet file format
# print(data)
df_original = pd.read_parquet('data_parquet_SL')  # reading the parquet file
df_modified = pd.read_parquet('data_parquet_modifiedSL')

plt.plot(df_original['Date first seen'],
         df_original['Duration'], label='Original')

plt.plot(df_modified['Date first seen'],
         df_modified['Duration'], label='Modified')

plt.xlabel('Timestamp')
plt.ylabel('Response Time')
plt.legend()
plt.show()

# print(df_modified.columns)
