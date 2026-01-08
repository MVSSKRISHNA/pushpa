import boto3
import os
import pandas as pd
 
class test_class():
    def test_func(spark,args_list):
        print('This is a test script')
        test_arg = args_list[args_list.index("--test_arg") +1]
        print('Printing test argument : ',test_arg)
        
if __name__ == '__main__':
    test_class().test_func()          