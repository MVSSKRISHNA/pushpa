class test_class():
    def test_func(spark,args_list):
        print('This is a test script')
        test_arg1 = args_list[0]
        test_arg2 = args_list[1]
        test_arg3 = args_list[2]
        print('Printing test argument : ',test_arg1)
        print('\n',test_arg2)
        print('\n',test_arg3)
if __name__ == '__main__':
    test_class().test_func()
