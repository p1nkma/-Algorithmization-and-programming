import functools
import random
import time
import unittest

def measure_execution_time(func):
    @functools.wraps(func)
    def timed_execution(*args, **kwargs):
        # Используем perf_counter для максимальной точности
        start = time.perf_counter() 
        result = func(*args, **kwargs)
        end = time.perf_counter()
        
        duration = end - start
        # Выводим 6 или 8 знаков после запятой, чтобы увидеть микросекунды
        print(f"Function {func.__name__} took {duration:.8f} seconds to execute")
        return result
    return timed_execution

# 1.Наивный поиск
@measure_execution_time
def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    res = []  # Создаем список для СБОРА всех индексов
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            res.append(i)  # Добавляем в список, но НЕ выходим из функции
    return res  # Возвращаем список только когда ПРОВЕРИЛИ ВЕСЬ ТЕКСТ

# 2.Алгоритм Бойера-Мура
@measure_execution_time
def boyer_moore(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0: return []
    if m > n: return []

    # --- 1. ПРЕДОБРАБОТКА: Таблица стоп-символов (Bad Character) ---
    bad_char = {pattern[i]: i for i in range(m)}

    # --- 2. ПРЕДОБРАБОТКА: Таблица хорошего суффикса (Good Suffix) ---
    suffix_shift = [0] * (m + 1)
    f = [0] * (m + 1)
    i, j = m, m + 1
    f[i] = j
    
    # Заполнение вспомогательного массива f (поиск повторов суффиксов)
    while i > 0:
        while j <= m and pattern[i-1] != pattern[j-1]:
            if suffix_shift[j] == 0:
                suffix_shift[j] = j - i
            j = f[j]
        i -= 1
        j -= 1
        f[i] = j
    
    # Заполнение оставшихся сдвигов на основе префиксов
    j = f[0]
    for i in range(m + 1):
        if suffix_shift[i] == 0:
            suffix_shift[i] = j
        if i == j:
            j = f[j]

    # --- 3. ОСНОВНОЙ ПОИСК ---
    res = []
    s = 0  # Текущий сдвиг шаблона относительно текста
    
    while s <= n - m:
        j = m - 1 # Начинаем проверку с конца шаблона
        
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        if j < 0:
            # Найдено полное совпадение
            res.append(s)
            # Сдвигаем на основе самого длинного префикса, который является суффиксом
            s += suffix_shift[0]
        else:
            # Произошло несовпадение на позиции j
            char_in_text = text[s + j]
            
            # Сдвиг по правилу плохой буквы
            bad_char_shift = j - bad_char.get(char_in_text, -1)
            
            # Сдвиг по правилу хорошего суффикса (индекс j+1, т.к. j - место ошибки)
            good_suffix_shift = suffix_shift[j + 1]
            
            # Главная магия: берем максимум из двух правил
            s += max(1, bad_char_shift, good_suffix_shift)
            
    return res

# 3.Алгоритм Рабина-Карпа 
@measure_execution_time
def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0 or m > n: return [] # Предохранитель 1: пустой паттерн или паттерн длиннее текста

    d = 256  # Размер алфавита
    q = 101  # Простое число
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    res = []

    # 1. Считаем хэш паттерна и первого окна
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # 2. Скользим окном
    for i in range(n - m + 1):
        # Если хэши совпали — проверяем символы
        if p == t:
            if text[i : i + m] == pattern:
                res.append(i)

        # 3. Пересчитываем хэш для следующего окна
        if i < n - m:
            # Магия Rolling Hash
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            
            # Если хэш отрицательный (такое бывает в Python с %), исправляем
            if t < 0:
                t += q
                
    return res

# 4.Алгоритм Кнута-Морриса-Пратта
@measure_execution_time
def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0: return []

    # --- ШАГ 1: Построение префикс-функции (таблицы LPS) ---
    lps = [0] * m
    length = 0  # длина предыдущего самого длинного префикса-суффикса
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # --- ШАГ 2: Сам поиск ---
    res = []
    i = 0  # индекс для текста
    j = 0  # индекс для шаблона
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:  # Нашли полное совпадение!
            res.append(i - j)
            j = lps[j - 1] # Ищем следующее возможное вхождение
        
        elif i < n and pattern[j] != text[i]: # Несовпадение
            if j != 0:
                j = lps[j - 1] # Умный сдвиг по таблице
            else:
                i += 1 # Если даже первая буква не совпала, просто идем дальше
    return res

# Тесты
class TestSubstringAlgorithms(unittest.TestCase):
    
    
    def setUp(self):
        """Подготовка данных перед каждым тестом"""
        self.pattern = "ABC"
        self.short_text = "ABABCABABC"
        self.expected_indices = [2, 7] # Индексы, где встречается "ABC"
        self.algos = [naive_search, boyer_moore, rabin_karp, kmp_search]
        
    def test_correctness(self):
        for algo in self.algos:
            with self.subTest(algo=algo.__name__):
                result = algo(self.short_text, self.pattern)
                print(f"Алгоритм {algo.__name__} вернул: {result}")
                self.assertEqual(result, self.expected_indices)

    def test_growing_text(self):
        """Замер времени: растет текст"""
        print("\n--- ТЕСТ: РОСТ ТЕКСТА ---")
        pattern = "ABCBA"
        for length in [1000, 5000, 10000]:
            print(f"\nДлина текста: {length}")
            test_text = ''.join(random.choice("ABC") for _ in range(length))
            for algo in self.algos:
                algo(test_text, pattern)

    def test_growing_pattern(self):
        """Замер времени: растет шаблон"""
        print("\n--- ТЕСТ: РОСТ ШАБЛОНА ---")
        text = ''.join(random.choice("ABC") for _ in range(10000))
        for p_len in [10, 100, 500]:
            print(f"\nДлина шаблона: {p_len}")
            pattern = ''.join(random.choice("ABC") for _ in range(p_len))
            for algo in self.algos:
                algo(text, pattern)

if __name__ == '__main__':
    unittest.main()