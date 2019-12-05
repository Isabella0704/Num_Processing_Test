import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#test1: Arrays (or Series)
s = pd.Series([1,3,5,np.nan,6,8])

#test2: Data_Frame
dates = pd.date_range('20130101', periods=6) #date_range()为时间序列函数
print(dates)
df=pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD')) #use list() to name columns
print(df)

#test3:Creating a DataFrame by passing a dict of objects that can be converted to series-like
df2=pd.DataFrame(
        {'A':1,
         'B':pd.Timestamp('20130102'),
         'C':pd.Series(1,index=list(range(4)),dtype='float32'),
         'D':np.array([3]*4, dtype='int32'),
         'E':pd.Categorical(["test","train","test","train"]),
         'F':'foo'
                })
print(df2)

# You can use cls to clear the iPython console

# Console operation
df2.dtypes # 居然还有category和objects类型
df.head() # use df.head(1) rather than df.head(0)取第一行数据
df.tail(3)
