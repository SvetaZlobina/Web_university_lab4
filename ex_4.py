from librip.decorators import print_result

# Необходимо верно реализовать print_result
# и задание будет выполнено

@print_result
def decor_test_1():
    return 1


@print_result
def decor_test_2():
    return 'iu'


@print_result
def decor_test_3():
    return {'a': 1, 'b': 2}


@print_result
def decor_test_4():
    return [1, 2]


decor_test_1()
decor_test_2()
decor_test_3()
decor_test_4()
