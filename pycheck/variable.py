import numpy as np
import pandas as pd
import re


class color():
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def print_(text, exe, c=color.RED):
    print(c + text + color.END + ' : ' + str(exe))

def info(v):
    print(color.YELLOW + '----------------------------------------' + color.END)
    print_('str()', '\n' + str(v), color.BLUE)
    print_('type()', type(v), color.BLUE)
    # list
    if type(v) in (list, tuple, set, dict, str):
        print_('len', len(v))
    # dictionary
    if (type(v) is not pd.core.series.Series) and (type(v) is not pd.core.frame.DataFrame) == True:
        print_('dir()', dir(v))
        if 'items' in dir(v):
            for key, value in v.items():
                print_('key', key)
                print_('type and value', str(type(value)) + '   ' + str(value))
        elif 'keys' in dir(v):
            print_('.keys()', v.keys())
            if 'values' in dir(v):
                print_('.values()', v.values())
    # numpy
    if 'dtype' in dir(v):
        print_('.dtype', v.dtype)
    if 'shape' in dir(v):
        print_('.shape', v.shape)
    if 'size' in dir(v):
        print_('.size', v.size)
    if 'ndim' in dir(v):
        print_('.ndim', v.ndim)
    if type(v) is np.ndarray:
        try:
            print_('np.isnan()', np.isnan(v))
        except:
            pass
    # dataframe
    if 'dtypes' in dir(v):
        print_('.dtype', v.dtypes)
    if 'columns' in dir(v):
        print_('.columns', v.columns)
    if 'dtypes' in dir(v):
        print_('.index', v.index)
    if 'isnull' in dir(v):
        print_('check number of nan (.isnull().sum().sum())', v.isnull().sum().sum())
        if v.isnull().values.any():
            print('nan ', v.isnull().sum(axis=0))
    # object
    if re.match('<(.*). object at (.*)>' , str(v)):
        print_('.__class__', v.__class__)
        print_('.__dict__', v.__dict__)
        # if issubclass(v, object):
        #     print('oya')

    print(color.YELLOW + '----------------------------------------' + color.END)

# if __name__ == '__main__':
#     from pycheck import variable
#     v = 'asdfg'
#     info(v)
#     variable.info(v)

#     v = 24
#     info(v)
#     v = ['aa','b']
#     info(v)
#     v = {'a':233,'b':'adfa','c':'124'}
#     info(v)
#     v =  np.array([1, 2,1])
#     info(v)
#     '''
#     class
#     '''
#     class Dog(object):
#         def __init__(self, name):
#             self.name = name

#     class SuperDog(Dog):
#         def __init__(self, name, function):
#             super(SuperDog, self).__init__(name)
#             self.function = function

#     p = Dog('Poodle')
#     info(p)
#     pp = SuperDog('Robin', 'sit down')
#     info(pp)
#     v = pd.Series([1,3,5,np.nan,6,8])
#     info(v)

#     v = pd.DataFrame({ 'A' : 1.,
#                         'B' : pd.Timestamp('20130102'),
#                         'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
#                         'D' : np.array([3] * 4,dtype='int32'),
#                         'E' : pd.Categorical(["test","train","test","train"]),
#                         'F' : 'foo' })
#     info(v)