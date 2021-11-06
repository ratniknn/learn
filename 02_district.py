# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as csr1_1, room2 as csr1_2
from district.central_street.house2 import room1 as csr2_1, room2 as csr2_2
from district.soviet_street.house1 import room1 as ssr1_1, room2 as ssr1_2
from district.soviet_street.house2 import room1 as ssr2_1, room2 as ssr2_2

str2 = ','.join(csr1_1.folks), ','.join(csr1_2.folks), ','.join(csr2_1.folks), ','.join(csr2_2.folks), '\n',\
       ','.join(ssr1_1.folks), ','.join(ssr1_2.folks), ','.join(ssr2_1.folks), ','.join(ssr2_2.folks),
str1 = ','.join(str2)
print('В районе живут', str1)


