import pandas as pd
student_marks = [[40, 60],
                 [70, 80],
                 [90, 95],
                 [100, 100]]
cd = pd.DataFrame(student_marks, columns=['physics', 'chemistry']) #Columns are the vertical divisions of a DataFrame that represent specific variables or features of the dataset.
cd.index = ['M', 'N', 'O', 'P'] #Index serves as a unique identifier for each row in the dataset.
#pd.Series(student_marks)
print(cd)

#Using Dictionaries
student_marks_dict = {
    'Names':['vishnu', 'sanjay', 'charan', 'Tharun'],
    'subjects':['physics', 'maths', 'science', 'English'],
    'marks':[93, 99, 98, 100]
        }
Df = pd.DataFrame(student_marks_dict)
Df.index = ['A', 'B', 'C', 'D']
print(Df)
 

student_dict = {
    'iq':[100, 200, 190, 220, 330],
    'marks':[100, 70, 90, 99, 60],
    'age':[20, 21, 19, 22, 23]
    }
md = pd.DataFrame(student_dict)
md.index = [1, 2, 3, 4, 5]
print(md)


student_marks = [[40, 60],
                 [70, 80],
                 [90, 95],
                 [100, 100]]
scd = pd.DataFrame(student_marks, columns=['Maths', 'chemistry']) 
scd.index = ['M', 'N', 'O', 'P'] 
scd = scd.rename(columns={'Maths':'DSA'})
scd = scd.sum()
scd = scd.max()
print(scd)

# Indexing and slicing with iloc and loc
#iloc = Used for integer-based indexing, where can access rows and columns by their integer positions(0-based).
data = {
    'A': [11, 12, 13, 14, 15],
    'B': ['BMW', 'Kawasaki ZX10RR', 'Trimph', 'Ducati', 'Z900']
}
ds = pd.DataFrame(data)
print(ds)
print(ds[1:2])
first_value = ds.iloc[0, 1]
print(first_value)
ds_slice = ds.iloc[1:4, :1]
ds_slice = ds.iloc[3: , :]
ds_slice = ds.iloc[[0, 2, 4], [0, 1]] # For particular row and column
print(ds_slice)

#loc
# loc = Used for label-based indexing, where can access rows and columns by their labels(index and column names).
ds.index = ['super sport', 'sport', 'speed', 'liter class', 'inline4']
print(ds)
ds_value = ds.loc['super sport', 'B'] # For particular element
print(ds_value)
ds_label = ds.loc['sport':'liter class', 'A':'B'] # for range, from this element to this element (Row and Column)
print(ds_label)
ds_index = ds.loc[['super sport', 'inline4'], ['A']] # Selected rows and column more for more than one element
print(ds_index)

student_dict = {
    'name':['Arjun', 'Manju', 'Rahul', 'Virat', 'Rohith'],
    'iq':[100, 200, 190, 220, 330],
    'marks':[100, 70, 90, 99, 60],
    'age':[20, 21, 19, 22, 23]
    }
md = pd.DataFrame(student_dict)
md.index = [1, 2, 3, 4, 5]
print(md)
#The set_index method is used to set one or more columns of a DataFrame as the index. and it serves as unique identifier for each row in the DataFrame.
md.set_index('name', inplace=True) #We use inplace because to change it permentaly.
md = md.loc[['Arjun', 'Rahul', 'Virat']]
md = md.iloc[[0, 1, 2]] 
print(md)