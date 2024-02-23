'1'
'ответ - False'

'2'
x=5
print(x+3)
'ответ - 5'

'3'

# d = {1:'one', 3:'three', 2:'two', '4':'four'}
# d.pop('4')
# d.sorted()
#
# print(d)
'ответ - sorted'

'4'
'ответ - связанные списки'

'5'
'ответ - if is raining и elif temperature'

'6'
'while True и if movie==exit'

'7'
def score(cf:float, scores:list):
    for i in scores:
        print(cf * i)

cf = 0.2
scores= [4, 5, 4]

score(cf, scores)


def score(cf, *scores):
    for i in scores:
        print(cf * i)

cf = 0.2
scores= [4, 5, 4]

score(cf, *scores)


def score(cf, scores):
    for i in scores:
        print(cf * i)

cf = 0.2
scores= [4, 5, 4]

score(cf, scores)


def score(cf:float, *scores:list):
    for i in scores:
        print(cf * i)

cf = 0.2
scores= [4, 5, 4]

score(cf, *scores)
'Использование цикла for для обращения к каждому элементу списка scores вместо последней строки кода'

'8'
'ответ - Статические методы могут изменять свойства экземпляра класса'

'9'
'ответ -from mymodules.mymodule import myfunction'

'10'
"ответ - with open('sales.txt', 'a') as f:"

'11'
"ответ - Удалить или изменить стандартные модули Python"

'12'
"ответ - None"

'13'
"ответ - 200.9"


import re

str = '3 Topapa 3a 200.99'
pat = r'\d+.\d'
match = re.search(pat, str)

print(match.group())

'14'
"ответ - нельзя создавать экземпляр абстрактного класса"

"SQL"
'1'
'ответ SELECT firstName, lastName FROM Employees WHERE Salary <= 50000;'

'2'
'ALTER TABLE Clients RENAME COLUMN new_email TO email;'

'3'
"добавится новая запись (4, 5, ‘BMW X5 M50d, null')"