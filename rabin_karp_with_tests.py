#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python3

"""
Реализация алгоритма Рабина-Карпа с модульными тестами
"""

import unittest

def rabin_karp(text, pattern):
    """
    Поиск всех вхождений алгоритмом Рабина-Карпа
    Параметры:
    ----------
        text: str
            текст
        pattern: str
            образец
    Возвращаемое значение
    ---------------------
        список позиций в тексте, с которых начинаются вхождения образца
    """
    result = []
    if pattern == "":
        return [i for i in range(len(text))]
    if text == "":
        return result
    text = text + ' '
    patternsum = sum(ord(s) for s in pattern)
    textwindowsum = sum(ord(text[j]) for j in range(len(pattern)))
    for i in range(len(text) - len(pattern)):
        if patternsum == textwindowsum:
            if text.startswith(pattern, i):
                result.append(i)
        textwindowsum = textwindowsum - ord(text[i]) + ord(text[i + len(pattern)])
    return result

class RabinKarpTest(unittest.TestCase):
    """Тесты для метода Рабина-Карпа"""

    def setUp(self):
        """Инициализация"""
        self.text1 = 'axaxaxax'
        self.pattern1 = 'xax'
        self.text2 = 'bababab'
        self.pattern2 = 'bab'

    def test_return_type(self):
        """Проверка того, что функция возвращает список"""
        self.assertIsInstance(
            rabin_karp(self.text1, "x"), list,
            msg="Функция должна возвращать список"
        )

    def test_returns_empty(self):
        """Проверка того, что функция, когда следует, возвращает пустой список"""
        self.assertEqual(
            [], rabin_karp(self.text1, "z"),
            msg="Функция должна возвращать пустой список, если нет вхождений"
        )
        self.assertEqual(
            [], rabin_karp("", self.pattern1),
            msg="Функция должна возвращать пустой список, если текст пустой"
        )
        self.assertEqual(
            [], rabin_karp("", ""),
            msg="Функция должна возвращать пустой список, если текст пустой, даже если образец пустой"
        )

    def test_finds(self):
        """Проверка того, что функция ищет все вхождения непустых образцов"""
        self.assertEqual(
            [1, 3, 5], rabin_karp(self.text1, self.pattern1),
            msg="Функция должна искать все вхождения"
        )
        self.assertEqual(
            [0, 2, 4], rabin_karp(self.text2, self.pattern2),
            msg="Функция должна искать все вхождения"
        )

    def test_finds_all_empties(self):
        """Проверка того, что функция ищет все вхождения пустого образца"""
        self.assertEqual(
            list(range(len(self.text1))), rabin_karp(self.text1, ""),
            msg="Пустая строка должна находиться везде"
        )

# Должно выдать:
# --------------
# Ran ... tests in ...s
# OK

# Запуск тестов
if __name__ == '__main__':
    unittest.main()


# In[ ]:




