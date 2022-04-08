"""
Parquet – бинарный столбцовый формат хранения данных, более производительный в операциях чтения-записи, чем CSV, например.
"""
import pandas as pd
import numpy as np
import dask.dataframe as dd

def main():
    # Считываем файл csv в Dataframe df
    df = dd.read_csv('pp-complete.csv', sep=',', dtype={'31': 'object',
       'Unnamed: 8': 'object'})
    # Конвертируем наш CSV-файл в Parquet
    df.to_parquet('100m')
    # Считываем в Dataframe df2 все части как в единый
    df2 = dd.read_parquet('100m/part.*.parquet')
    # Выбираем нужные столбцы по которому будем отбор на дубликаты (Street, Locality, Town/City, District, County)
    b = df2.iloc[:, 9:14].compute()
    # Выбираем только дубликаты, т.е. столбы котрые повторяются больше 1 раза
    f_c = b.groupby(b.columns.tolist()).size() > 1
    cc = b.groupby(b.columns.tolist()).size().loc[f_c]
    # И сохраняем результат в новом csv файле duplicates.csv
    cc.to_csv('duplicates.csv', sep=',')
    print(cc)

if __name__ == '__main__':
    main()