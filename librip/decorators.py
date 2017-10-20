
def print_result(function_to_decorate):
    def decorated_by_print_result(*args):
        print(function_to_decorate.__name__)
        returned_value = function_to_decorate(*args)
        if isinstance(returned_value, list):
            print('\n'.join(map(str, returned_value)))
        elif isinstance(returned_value, dict):
            print('\n'.join(map(lambda k: str(k) + ' = ' + str(returned_value[k]), returned_value)))
        else:
            print(returned_value)
        return returned_value
    return decorated_by_print_result

# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
# @print_result
# def test_1():
#     return 1
#
# @print_result
# def test_2():
#     return 'iu'
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
# @print_result
# def test_4():
#     return [1, 2]
#
# test_1()
# test_2()
# test_3()
# test_4()
#
# На консоль выведется:
# test_1
# 1
# test_2
# iu
# test_3
# a = 1
# b = 2
# test_4
# 1
# 2
