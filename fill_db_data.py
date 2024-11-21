# from .. import Part_in
from app.api.models.parts import Part_in, Part_out

import orm 

from sqlalchemy.ext.asyncio import AsyncSession

import pandas as pd
import numpy as np

import os


def parse_table_sheet(table, sheet):
    df =  table.parse(table.sheet_names[2])
    df = df.replace({np.nan: None})
    # print(df.head())
    return df

def read_excel_file(file_path: str) -> list[pd.DataFrame]:
    tables = pd.ExcelFile(file_path)
    # print(tables.sheet_names, type(tables))
    tables_list = []
    for table in tables.sheet_names:
        tables_list.append(parse_table_sheet(tables, table))
    # print(tables_list)
    return tables_list 

def input_values_db(values: pd.DataFrame) -> None:
    session: AsyncSession = orm.get_session() 

   
if __name__ == '__main__':
    file = 'Данные_для_базы.xlsx'
   
    df = read_excel_file(file)
    # print(df)
    # test = Part_in(**df[0].iloc[0])
    test = dict(df[0].iloc[0]).values()
    data = dict(zip(Part_in().model_dump().keys(), test))
    part = Part_in(**data)
    part_db = orm.Part(**part)
    print(part)
    # for item in test.model_dump().keys():

    #     print(item) 
   
