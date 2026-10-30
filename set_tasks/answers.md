# Т118 / Множества set — ответы
## Задание 1. Уникальные кабинеты

rooms = [205, 310, 205, 412, 310, 205]   
unique_rooms = set(rooms)   
print(len(unique_rooms))    
print(sorted(unique_rooms))   

Результат:  
3, [205, 310, 412]  

`set(rooms)` создаёт новый объект, исходный список не затрагивается.
#### Разница между `set()` и `{}`:
- `set()` — пустое множество.
- `{}` — пустой словарь (`dict`), а не множество.

## Задание 2. Набор навыков

skills = {"python", "git"}  
skills.add("sql")  
skills.add("git")  
skills.update(["json", "sql"])  
skills.discard("java")  
skills.remove("git")  
print(skills)  
print(len(skills))  

Результат:  
{'sql', 'python', 'json'}, 3.

#### Что будет при `remove("java")`?
Элемента `"java"` нет, поэтому `remove` выбросит `KeyError: 'java'`.

#### Что будет при `clear()`? 
Удаляет все элементы, множество остаётся пустым, но объект тот же:

## Задание 3. Два кружка EKEB

python_club = {"Айдар", "Алина", "Данияр"}  
testing_club = {"Алина", "Данияр", "Мадина"}  
a = python_club  
b = testing_club  
print(sorted(a | b))  
print(sorted(a & b))  
print(sorted(a - b))  
print(sorted(b - a))  
print(sorted(a ^ b)) 

Результат:  
['Айдар', 'Алина', 'Данияр', 'Мадина']  
['Алина', 'Данияр']  
['Айдар']  
['Мадина']  
['Айдар', 'Мадина']