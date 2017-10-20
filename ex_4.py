from librip.decorators import print_result

# Необходимо верно реализовать print_result
# и задание будет выполнено


@print_result
def decor_test1():
    return 1


@print_result
def decor_test2():
    return 'iu'


@print_result
def decor_test3():
    return {'a': 1, 'b': 2}


@print_result
def decor_test4():
    return [1, 2]


decor_test1()
decor_test2()
decor_test3()
decor_test4()
