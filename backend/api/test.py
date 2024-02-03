from pydantic import BaseModel
from typing import List, Tuple


class Departments(BaseModel):
    name: str


class Organization(BaseModel):
    items: List[Departments]


# Ваш список кортежей
data = [('Отдел Разработки',), ('Отдел Разработки',)]
# Преобразование списка кортежей в список экземпляров Departments
departments_list = [Departments(name=department_name) for department_name, in data]
# Создание экземпляра Organization
a = Organization(items=departments_list)

for item in a.items:
    print(item.name)