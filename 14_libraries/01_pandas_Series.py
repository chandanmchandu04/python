import pandas as pd
import numpy as np

#converting a list into serires
l = [1,  23, 45, 6]
s = pd.Series(l)
print(type(s)) 

#DataFrame
data = {
    "Name": ["Tom", "Nick", "John"],
    "Age": [20, 21, 19],
    "Score": [90, 85, 88]
}
df = pd.DataFrame(data)
print(df)

#Series
# converting a string into series, snd in Pandas we call string as object.
c1 = "Bharath simha reddy"
data_string = pd.Series(list(c1))
print(data_string)

# Converting a dictionary into seies
data_dict = {"a": 1, "b": 2, "c": 3}
d1 = pd.Series(data_dict)
print(d1)

# Series using Index with some common Terms of methods used in pandas library.
marks = [70, 80, 88, 90, 99, 100]
subjects = ["DAA", "SE", "DM", "CS", "R-programming", "R-Lab"]
m1 = pd.Series(marks, index = subjects, name = "student_marks")
print(m1)
print(m1.head(2))
print(m1.tail(1))
print(m1.describe())
print(m1.info())
print(m1.shape)
print(m1.values)
print(m1.name)
print(m1.is_unique)
print(m1.size)
print(m1.memory_usage)

Marks_data = {
    'Chandan': 90,
    'sanajy': 96,
    'Tharun': 100,
    'charanraj': 100,
    'DM bharath': 101,
    'Grace': np.nan
}
marks = pd.Series(Marks_data)
print(marks)
print(marks.astype(object)) #Converts the datatype of the series to the specified type to an object type.
print(marks.between(80, 100)) #Returns a boolean series indicating whether each element in the serirs falls within the specified range
print(marks.clip(80,100)) #Limits the value of the series to specified range.
print(marks.drop_duplicates())#Returns a series with duplicate values removed, keeping only first occurrence of each unique value.
print(marks.isnull())#Returns a boolean Series indicating whether each element in the Series is null (NaN).
print(marks.dropna())#Returns a Series with all null (NaN) values removed.
print(marks.fillna(96))#Replaces all null (NaN) values in the Series with the specified value
print(marks.isin([20,101]))#Returns a boolean Series indicating whether each element in the Series is contained in the specified list of values.
print(marks.copy())#Creates a deep copy of the Series
print(marks.replace(101, 70))#Replaces all occurrences of the specified value (101) in the Series with a new value
print(marks.sort_values())# Returns a Series sorted in ascending order based on the values.

#INDEXING AND SLICING USING SERIES
series = pd.Series([10, 20, 30, 40, 50], index=['A', 'B', 'C', 'D', 'E'])
print(series)
print(series['D'])
print(series.iloc[4])
print(series.loc['A'])
print(series.unique())
print(series.value_counts())
print(series.groupby)

#STATISTICAL METHODS
Num = pd.Series([200, 300, 400, 500, 600, None, -30])
print(Num)
print(Num.sum())
print(Num.mean())
print(Num.median())
print(Num.max())
print(Num.var())
print(Num.to_numpy())
print(Num.to_frame())
print(Num.describe())
print(Num.to_string())
print(Num.to_list())

#TO save in different file formate
print(Num.to_csv("pandas_series_data.csv"))
print(Num.to_excel("pandas_series_data.xlsx"))
print(Num.to_json("pandas_series_data.json"))

#Operation betweeen two series
series1 = pd.Series([12, 13, 14, 15, 16])
series2 = pd.Series([200, 300, 400, 500, 600])
print(series1.add(series2))
print(series1.sub(series2))
print(series1.mul(series2))
print(series1.pow(series2))
print(series1.abs())#abstract value 
cd = pd.concat([series1, series2])
print(cd)