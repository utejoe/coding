def test_args(first, second, *args):
    print(first)
    print(second)
    print(args)
test_args(1, 2, 3, 4, 5)
