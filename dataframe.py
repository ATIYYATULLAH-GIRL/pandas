import pandas as pd
import numpy as np

dataset={
    "cars":["BMW","FORD","VOLVO"],
    "passings":[3,7,2]
}

myvar=pd.DataFrame(dataset)
print(myvar)

a=[1,5,9]
series=pd.Series(a)
print(series)

label1=pd.Series(a,index=["x","y","z"])
print(label1)

calories={
    "day1":100,
    "day2":90,
    "day3":50
}
label2=pd.Series(calories)
print(label2)

data1={
    "calories":[100,90,50],
    "duration":[50,30,16]
}
df=pd.DataFrame(data1)
print(df)

exam_data={"name":["Lindani","Atiyyatullah","Sana","Iranzi","Nateeq","Sulayman"],
           "score":[12.5,20,9,16,np.nan,10],
           "attempts":[2,1,7,9,4,6],
           "qualify":["yes","yes","no","yes","no","yes"]}
labels=["A","B","C","D","E","F"]

df=pd.DataFrame(exam_data,index=labels)
print(df)