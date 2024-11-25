# from .. import Part_in
from app.api.models.parts import Part_in, Part_out
from app.settings import settings
import orm 

from sqlalchemy.ext.asyncio import AsyncSession

import pandas as pd
import numpy as np
import asyncio
from typing import AsyncIterator
import contextlib



@contextlib.asynccontextmanager
async def connect_db() -> AsyncIterator[None]:
    orm.db_manager.init(settings.database_url)
    yield
    await orm.db_manager.close()

def parse_table_sheet(table, sheet):
    df =  table.parse(table.sheet_names[2])
    df = df.replace({np.nan: None})
    return df

def read_excel_file(file_path: str) -> list[pd.DataFrame]:
    tables = pd.ExcelFile(file_path)
    # print(tables.sheet_names, type(tables))
    tables_list = []
    for table in tables.sheet_names:
        tables_list.append(parse_table_sheet(tables, table))
    # print(tables_list)
    return tables_list 

async def input_values_db(part: orm.Part, session: AsyncSession) -> None:
    session.add(part)
    await session.commit()
    await session.refresh(part)
       

async def main():
    file = 'Данные_для_базы.xlsx'
   
    df = read_excel_file(file)
    # print(df)
    # test = Part_in(**df[0].iloc[0])
    
    test = dict(df[0].iloc[0]).values()
    data = dict(zip(Part_in().model_dump().keys(), test))
    part = Part_in(**data)
    part_db = orm.Part(**part.model_dump())
    async with connect_db() as con: 
        async for session in orm.get_session():
            await input_values_db(part_db, session)

if __name__ == '__main__':
    
    asyncio.run(main())

    # for item in test.model_dump().keys():

    #     print(item) 
   
