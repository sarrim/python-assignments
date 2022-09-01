def test_fun(fname):
    print(fname + ' name')

test_fun('test')
test_fun('test1')
test_fun('test2')


def infinite_args(*args):
    print(args)
infinite_args('sarmad', 'sarmad@mail.com', '323232', 'home addresss')