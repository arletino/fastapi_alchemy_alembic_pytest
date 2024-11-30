# from .. import Part_in
from app.api.models.parts import Part_in, Part_out
from app.settings import settings
import orm 

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from pydantic import ValidationError
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
    tables_list = []
    for table in tables.sheet_names:
        tables_list.append(parse_table_sheet(tables, table))
    return tables_list 

async def input_values_db(parts: list[orm.Part], session: AsyncSession) -> None:
    tmp = set()
    for part in parts:
        if part.article not in tmp:
            tmp.add(part.article)
            session.add(part)
            await session.flush()
    try:
        await session.commit()
    except SQLAlchemyError as e:
        print(e)
       
async def update_elem_db(elm: orm.Part, session: AsyncIterator) -> None:
    pass
    
    
async def main():
    file = 'Данные_для_базы.xlsx'
    df = read_excel_file(file)
    async with connect_db():
        count = 0
        list_parts = []
        for index, part in df[0].iterrows():
            count += 1
            print(count)
            part_pd = dict(part).values()
            data = dict(zip(Part_in().model_dump().keys(), part_pd))
            try:
                part = Part_in(**data)
                part_db = orm.Part(**part.model_dump())
                if part_db not in list_parts:
                    list_parts.append(part_db)
                
            except ValidationError as e:
                print(f'{e} on part {part['art']}')
            except AttributeError as e:
                print(f' {e} on part {part['art']}')
        async for session in orm.get_session():
            await input_values_db(list_parts, session)


if __name__ == '__main__':
    
    asyncio.run(main())
   
