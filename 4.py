import pandas as pd
from functools import reduce
d={
    "Number":[1,2,3,4,5],
    "Letters":['A','B','C','D','E']
}
df=pd.DataFrame(d)
sq=df['Number'].map(lambda x:x**2)
ev=list(filter(lambda x:x%20,df['Number']))
po=reduce(lambda x,y:x*y,df['Number'])
print("\n Dataframe:\n",df)
print("\n map for squaring:\n",sq)
print("\n reduce for producting:\n",po)
print("\n filter for evennumber:\n",ev)
