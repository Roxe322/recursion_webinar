- [Что такое рекурсия?](#org315c1f8)
- [Правильная рекурсия](#orge46caee)
- [Что такое стек вызовов?](#org9239392)
- [Что такое стек вызовов?](#org47c112c)
- [Почему рекурсия это плохо](#org9846ba3)
- [Recursion depth](#orga6c8280)
- [Глубина рекурсии](#orga8dfaeb)
- [Почему рекурсия это хорошо](#org644d71f)
- [Вариант задачи для рекурсии](#orgc18c49b)
- [Хвостовая рекурсия](#orgaf15ca0)
- [Оптимизация хвостовой рекурсии и почему её нет в Python](#org6f48bfa)
- [Пример когда рекурсия помогает](#org2364f17)
- [Дополнительная литература](#org46f786a)
- [Динамическое программирование](#org9ed2ad2)
- [Кэширование](#orge11c35f)
- [Поиск приблизительно совпадающих строк](#org330f75e)
- [Рекурсивное решение](#org0775ab3)
- [Динамическое программирование в действии](#orgbda5f5a)
- [Вопросы-ответы](#org2c8394c)



<a id="org315c1f8"></a>

# Что такое рекурсия?

Приём в программировании, когда задача может быть разделена на несколько таких же, но проще, задач.

```python
def pow(x, n):
    # возведение числа в степень это
    # умножение числа на число
    # в степени n-1
    if n == 0:
        return 1
    return x * pow(x, n-1)
```


<a id="orge46caee"></a>

# Правильная рекурсия

```python
def pow(x, n):
    # хорошо бы проверить,
    # что база достижима
    assert n >= 0
    # base case / база рекурсии
    if n == 0:
        return 1
    # recursive case / шаг рекурсии
    return x * pow(x, n-1)
```


<a id="org9239392"></a>

# Что такое стек вызовов?

```python
def foo(msg):
    print('{} foo'.format(msg))

def main():
    msg = 'hello'
    foo(msg)

if __name__ == '__main__':
    main()
```


<a id="org47c112c"></a>

# Что такое стек вызовов?

![img](callstack.png)


<a id="org9846ba3"></a>

# Почему рекурсия это плохо

-   стек вызовов растёт вместе с ростом глубины рекурсии
-   можно попасть в бесконечную рекурсию и истратить всю память на стек вызовов


<a id="orga6c8280"></a>

# Recursion depth

```python
def inf_counter(x):
    print(x)
    return inf_counter(x+1)

inf_counter(0)
```


<a id="orga8dfaeb"></a>

# Глубина рекурсии

```python
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(
    sys.getrecursionlimit() + 234
)
print(sys.getrecursionlimit())
```

    1000
    1234


<a id="org644d71f"></a>

# Почему рекурсия это хорошо

Помогает описать решение задачи понятным языком

```python
# n! = n * (n-1)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
```

    120


<a id="orgaf15ca0"></a>

# Хвостовая рекурсия

Рекурсия, не требующая действий с возвращённым результатом из шага рекурсии.

```python
def factorial(n, collected=1):
    if n == 0:
        return collected
    return factorial(n-1, collected*n)

print(factorial(5))
```
    120

# Переписываем на цикл
```python
def factorial(n):
    collected = 1
    while n > 0:
        collected *= n
        n -= 1
    return collected
```


<a id="org6f48bfa"></a>

# Оптимизация хвостовой рекурсии и почему её нет в Python

-   Интерпретаторы/компиляторы могут оптимизировать хвостовую рекурсию (Tail Call Optimization) и не делать записей в стек вызовов, а подменять переменные в стеке вызовов, таким образом код получится равнозначным обычному циклу
-   <span class="underline"><span class="underline">[Почему TCO нет и не будет в Python](https://neopythonic.blogspot.com/2009/04/final-words-on-tail-calls.html)</span></span>


<a id="orgc18c49b"></a>

# Вариант задачи для рекурсии

Попробуйте реализовать решение <span class="underline"><span class="underline">[этой задачи](https://github.com/Roxe322/recursion_webinar/blob/master/count_change.py)</span></span> без использования рекурсии


<a id="org2364f17"></a>

# Пример когда рекурсия помогает

-   **Задача:** У вас есть вложенная структура данных и вы хотите просуммировать значения поля X во всех объектах этой структуры.
-   **Решение задачи:** <https://github.com/Roxe322/recursion_webinar/blob/master/recursion_example.py>


<a id="org46f786a"></a>

# Дополнительная литература

-   [SICP](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book.html)


<a id="org9ed2ad2"></a>

# Динамическое программирование

```python

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n=n-1) + fib(n=n-2)

```

![img](fibonacci.png)


<a id="orge11c35f"></a>

# Кэширование

```python
cache = {0: 1, 1: 1}

def fib(n):
    if n not in cache:
        cache[n] = fib(n=n-1) + fib(n=n-2)
    return cache[n]

```

![img](cached_fibonacci.png)


<a id="org330f75e"></a>

# Поиск приблизительно совпадающих строк

Возможные действия над строками, каждое действие будет иметь стоимость \(1\)

-   ***замена*:** заменить один символ в строку A1 на символ из строки A2. ("мама" → "рама")
-   ***вставка*:** вставить один символ в строку A1 так чтобы она совпала с подстрокой A2. ("роза" → "проза")
-   ***удаление*:** удалить один символ в строке A1 так чтобы она совпала с подстрокой A2. ("гроза" → "роза")


<a id="org0775ab3"></a>

# Рекурсивное решение

```python
def lev(a: str, b: str) -> int:
    if not a: return len(b)
    if not b: return len(a)
    return min([
        lev(a[1:],b[1:])+(a[0]!=b[0]),
        lev(a[1:],b)+1,
        lev(a,b[1:])+1
    ])

print(lev("salt", "foobar"))
print(lev("halt", "salt"))
```

    - 6
    - 1


<a id="orgbda5f5a"></a>

# Динамическое программирование в действии

```python
def levenshtein(a, b):
    n, m = len(a), len(b)

    current_row = range(n + 1)  # Будем хранить только текущий и предыдущий ряд, а не всю матрицу
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]
```


<a id="org2c8394c"></a>

# Вопросы-ответы

![img](questions.jpg)
