#!/usr/bin/env python
# coding: utf-8

# **[Python Basics](#1)**
# 1. [List, Tuple, Dictionary](#2)
# 2. [For Loop,  lambda and anonymous function, zip,  list compreherension](#3)
# 3. [Numpy Array, Pandas Series](#4)
#     
# 
# **[Working with Dataframes](#5)**
# 1.  [Pandas Dataframes](#6)
# 2.  [Read Data(info, columns, head...)](#7)
# 3.  [Regulating Data (NaN values, String values to Numeric)](#8)
# 4.  [Indexing & Slicing (Reach and change index names, values; getting column names and values..)](#9)
# 5.  [Filtering and Transforming (Lambda, Defining column, Creating boolen series, filters )](#10)
# 6.  [Data Analysis (describe: max, min, Q, IQR, std...)](#11)
# 7.  [Concatenating](#12)
# 8.  [Pivoting (Reshaping dataframes)](#13)
# 9.  [Melting (Reshaping dataframes)](#14)
# 10. [Stacking and Unstacking (Reshaping dataframes)](#15)
# 11. [Groupby (basic functions: sum(), min(), max(), mean())](#16)
# 11. [Merging](#17)
#      

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# <a id="1"></a>
# # PYTHON BASICS

# <a id="2"></a>
# **1.1. LIST**

# In[2]:


#Create list
num = [1,2,3,4,5,6]
num


# In[3]:


#Let's see its attribute
print(dir(num))


# In[4]:


#Add new element
num.append("foo") 
num


# In[5]:


#Remove element
num.remove('foo') 
num


# In[7]:


print("All elements : ", num)
print("First 3 elements : ", num[:3])
print("Except first 3 elements  : ", num[3:])
print("4 to 6 elements: ", num[3:6])
print("5 to 2 elements: ", num[1:-2])


# **1.2. TUPLE**
# 
# Tuple has less attributes than compared to list.

# In[8]:


#Creating Tuple
t1 = (6,"str",15,12,"foo",6)
t1


# In[9]:


print("count(6)", t1.count(6)) # How many '6' does tuple have?
print("index('foo')", t1.index('foo')) # What's index of 'foo'


# **1.3. DICTIONARY**

# In[19]:


dic = {"alice" : 23, "bob" : 12, "steve": 45}
dic


# In[20]:


#Get Steve value
dic["steve"]


# In[21]:


#Get bob value
dic.get("bob")


# In[22]:


print(dic.keys())
print(dic.values())
dic.pop("steve") # remove steve


# In[23]:


#Another way to create a dic
x = dict([("Mad Men", "Drama"), ("The Office", "Comedy")])
x


# <a id="3"></a>
# **2.1. FOR LOOP**

# In[24]:


#Create list 
names = ["alice","bob","eva", "steve","jane", "billy"]

#print each element of list
for name in names:
    print(name)


# In[25]:


#print each element of string
for i in 'alice':
    print(i)


# In[29]:


#split() function is  return a list of word strings. 
for i in "alice and bob".split():
    print(i)


# **2.2. LAMBDA AND ANONYMOUS FUNTION**
# 
# Like writing a function in a short way.

# In[32]:


#Lambda Function
cube = lambda x: x**3
cube(3)


# In[33]:


#Anonymous function is likely to lambda but it takes more arguments.
numbers = [2,3,4,5,6,7,8]
results = list(map(cube, numbers))
results


# **2.3. ZIP**
# 
# It's like mapping two list. Lıst of tuples.

# In[35]:


num1 = [1,2,3,4,5,6,7]
num2 = [5,'foo',8, 1.0, 'trathaka', 7]
z = zip(num1,num2)
print(z)
print(list(z))
type(z)


# **2.4. LIST COMPREHENSION**

# In[39]:


#Create a dictionary
dic1= { "Name":["alice","bob","clarke", "steve","eva", "jason"],
        "Ages":[15,16,20,23,13,18],
        "Salary":[100,232, 300, 50, 140,500] }
import pandas as pd
d = pd.DataFrame(dic1)
d


# In[40]:


for i in dic1['Ages']:
    dic1["Ages"] = i + 1
    print(i)


# In[ ]:





# In[43]:


#Creating new column, if salary > avarage write 'high' else 'low'
avg = sum(dic1["Salary"]) / len(dic1["Salary"]) #Avarage
dic1["new_column"] = ["high" if salary > avg else "low" for salary in dic1["Salary"]]
dic1


# In[44]:


#Creating new column, if salary > avarage write 'high' else 'low'
avg = sum(d["Salary"]) / len(d["Salary"]) #Avarage
d["new_column"] = ["high" if salary > avg else "low" for salary in d["Salary"]]
d


# In[45]:


d.drop('new_column', 1)


# In[46]:


#Change column name
dic1["Status"] = dic1.pop("new_column")
dic1


# In[48]:


d


# <a id="4"></a>
# **3.1. NUMPY ARRAY** 

# In[49]:


a = np.array([1,2,3,4,5,6,7,8,])
a


# In[50]:


a = a.reshape(2,4)
a


# In[51]:


print("shape : ", a.shape)
print("dimension : ", a.ndim)
print("data type : ", a.dtype.name)
print("size : ", a.size)
print("type", type(a))


# In[52]:


#Create 3x4 matris and fill it with zeros
zeros = np.zeros((3,4))
zeros


# In[53]:


np.ones((3,4))


# In[55]:


#Create a array: range of elements 5 to 20, increase 2
c = np.arange(5,20,2).reshape(4,2)
c


# In[56]:


#Create a array, put into the 20 numbers to between 1 and` 10.
np.linspace(1,10,20)


# In[60]:


#To sum arrays
a = np.array([1,2,3])
b = np.array([4,5,6])
a + b


# In[61]:


a**2


# In[62]:


np.sin(a)


# In[63]:


c > 12


# In[64]:


c[c>12]


# In[65]:


#Element wise
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])
a*b


# In[66]:


#Dot product
a.dot(b.T) #b.T = b's tranpose


# In[67]:


#Create random matrix 2x3
np.random.randint(2, 10,(2,3))


# In[68]:


print("a : \n", a)
print("Sum of a:", a.sum())
print("Max of a: ", a.max())
print("Min of a: ", a.min())


# In[69]:


print("Sum rows : ", a.sum(axis=1))
print("Sum columns : ", a.sum(axis=0))


# In[70]:


#Indexing and Slicing
a = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
print(a)
print("\n",a[0:2,1:4])
print("\n", a[-1:])


# In[72]:


#SHAPE MANIPULATION
b = a.ravel()
b


# In[73]:


b = b.reshape(5,3)
b


# In[74]:


#ARRAY CONCAT
array1 = np.array([ [1,2], [3,4] ])
array2 = np.array([ [4,5], [6,7] ])
#VERTICAL
np.vstack((array1, array2))


# In[76]:


#HORIZONTAL
np.hstack((array1, array2))


# In[77]:


#Convert
l = [1,2,3,4]
a = np.array(l)
a


# In[78]:


list(a)


# In[79]:


tuple(a)


# In[80]:


#Copy
a = np.array(a)
b = a #Same address a and b
b


# In[81]:


a[0] = 5
b


# In[82]:


c = a.copy() # New address for c
c


# In[83]:


a[0] = 1
c


# **3.2. PANDAS SERIES**
# 
#     Understanding of series is important because it will be needed while working with dataframes. 
#     Series is similar to one-dimensional labeled array.  
#     It consist of indexes and their corresponding values.

# In[84]:


#Creating a series
my_series = pd.Series([1,3,'string', 'f', 7.1, 10])
my_series


# In[85]:


#Reaching values, index and rows
print("First 3 values : ", my_series[0:2].values)
print("Last 2 rows :")
my_series[-2:]


# In[86]:


#Changing index names.
indexes = [3, "foo", 5, "float", 1, 10]
my_series.index = indexes
my_series


# In[87]:


#Getting the value with index name.
my_series["foo"]


# In[88]:


#A dictionary can be put into  to series.
dictionary = {"Alice":25, "Bob" : 15, "Clarke": 19}
new_series= pd.Series(dictionary)
new_series


# In[89]:


#Comprehension : new_series > 18 is return true or false
new_series[new_series>18]


# In[90]:


#One another way to create series.
indexes = ["str", "float", "int"]
new_series = pd.Series([20,30,40], index=indexes)
new_series


# <a id="5"></a>
# # WORKING WITH DATAFRAMES

# <a id="6"></a>
# **1.PANDAS DATAFRAMES**

# In[91]:


dic1= { "Name":["alice","bob","clarke", "steve","eva", "jason"],
        "Ages":[15,16,20,23,13,18],
        "Salary":[100,232, 300, 50, 140,500] }
#Creating a dataframe
dt= pd.DataFrame(dic1)
dt


# In[92]:


for i in dt.index:
    print(i)


# In[95]:


for i in (dt.Name, dt.Ages):
    print(i)


# <a id="7"></a>
# **2.READ DATA**

# In[96]:


#Read Data from csv file
data = pd.read_csv(r"E:\Python\Machine Learning Projects\Python Basics, Numpy, Pandas for Data Science/Iris.csv")

data.info()


# In[97]:


#Show columns names
data.columns


# In[102]:


#Show first 7 rows
data.head(7)


# In[104]:


#Show last 5 rows
data.tail()


# <a id="8"></a>
# **3. REGULATING DATA**

# In[105]:


#If numbers are defined as a string, we can change them to numeric
data.SepalLengthCm = pd.to_numeric(data.SepalLengthCm, errors='coerce')


# In[106]:


##If there is a null its values returns True
data.isnull().head()


# In[107]:


#If there is a null its values returns False
data.notnull().head(5)


# In[108]:


#It shows is there any nan values in the columns
data.notnull().all()


# In[109]:


#It drops nan values
data.SepalLengthCm.dropna(inplace = True) 


# In[110]:


#It fills nan values with 0
data.SepalLengthCm.fillna(0, inplace = True)


# <a id="9"></a>
# **4.INDEXING & SLICING**

# In[111]:


data.head()


# In[115]:


#Get a column as a series
data["SepalLengthCm"].head()


# In[116]:


#Get a column as a dataframe
data[["SepalLengthCm"]].head()


# In[117]:


#Get columns
data[["SepalLengthCm", "PetalLengthCm"]].head()


# In[118]:


#Set id column as a index.
data = data.set_index('Id')
data.head()


# In[119]:


#Change labels index and columns
data.index.names = ['index']
data.head()


# In[120]:


#Add one more index
data.set_index('Species', append=True).head()


# In[121]:


#Change the index values
#data.index = range(100,len(data.index)+100)
#data.head()


# In[122]:


#Changing column names
data = data.rename(columns={'SepalLengthCm':'SLCM','SepalWidthCm':'SWCM', 'PetalLengthCm':'PLCM', 'PetalWidthCm': 'PWCM'})
data.columns


# In[124]:


#Indexing and Slicing
data.loc[2:4, ["PLCM"]]


# In[127]:


data.loc[2:4, "PLCM":]


# In[126]:


data.loc[1:5,"PLCM": ]


# In[128]:


data.loc[1:3 , ["PLCM", "Species"]]


# <a id="10"></a>
# **5.FILTERING & TRANSFORMING**

# In[129]:


data.head()


# In[130]:


#Applying lambda function SLCM column
data.SLCM = data.SLCM.apply(lambda n : n/2)
data.head()


# In[131]:


# Defining column using other columns
data["total_lengthCM"] = data.SLCM + data.PLCM
data.head(3)


# In[132]:


# Creating boolean series
boolean = data.SLCM > 3.5
data[boolean]


# In[134]:


#Apply two filters
filter1 = data.SLCM > 3.5
filter2 = data.PLCM > 6.5
data[filter1 & filter2]


# <a id="11"></a>
# **6.DATA ANALYSIS**
# 
#     -count: number of entries
#     -mean: average of entries
#     -std: standart deviation
#     -min: minimum entry
#     -25%: first quantile (Q1)
#     -50%: median or second quantile
#     -75%: third quantile (Q3)
#     -max: maximum entry
#     
#     And IQR = (Q3-Q1)
#     If there is a data smaller than Q1 - 1.5(IQR) or bigger than Q3 + 1.5(IQR), we can drop them. Those datas are irrelevant.

# In[135]:


data.describe()


# <a id="12"></a>
# **7. CONCATENATING**

# In[136]:


#CONCAT ROWS
data1 = data.head()
data2= data.tail()
rows_concat = pd.concat([data1,data2])
rows_concat


# In[138]:


#CONCAT COLUMNS
data1 = data['SLCM'].head()
data2= data['PLCM'].head()
cols_concat = pd.concat([data1,data2], axis=1) 
cols_concat


# <a id="13"></a>
# **8. PIVOTING**

# In[139]:


dic = {"treatment":["A","B","B","A"],"gender":["F","M","F","M"],"response":[10,45,5,9],"age":[15,4,72,65]}
df = pd.DataFrame(dic)
df


# In[140]:


#PIVOTING
df.pivot(index="gender", columns="treatment", values=["response", "age"])


# <a id="14"></a>
# **9.MELTING**
# 
# Reverse of pivoting

# In[141]:


df


# In[142]:


pd.melt(df, id_vars="treatment", value_vars=["gender","age"])


# <a id="15"></a>
# **10. STACKING AND UNSTACKING**
# 
# It reshapes dataframes.

# In[143]:


df


# In[144]:


df1 = df.set_index(["treatment","gender"])
df1


# In[145]:


#UNSTACKING
# level determines indexes
df1.unstack(level=1)


# In[146]:


df1.unstack(level=0)


# In[147]:


# change inner and outer level index position
df2 = df1.swaplevel(0,1)
df2


# <a id="16"></a>
# **11.GROUPBY**

# In[148]:


data.head()


# In[149]:


#Group by according to Species and calculate the mean
data.groupby('Species').mean()


# In[150]:


#Groupby and sum
data.groupby('Species').sum()


# In[151]:


#print setosa's summed values
data.groupby('Species').sum().loc["Iris-setosa"] #It returns series


# In[152]:


data.groupby('Species').sum().loc[["Iris-setosa"]] #It returns dataframe


# In[154]:


#print max SWCM, PLCM,PWCM values of versicolor
data.groupby('Species').max().loc[["Iris-versicolor"], "SWCM":"PWCM"]


# In[155]:


#print PLCM,PWCM and total_lengthCM values of 1 and 2 rows
data.groupby('Species').max().iloc[[1,2] , -3:]


# In[159]:


df


# In[160]:


df.groupby("treatment")[["response", "age"]].min()


# In[161]:


df.groupby(["treatment", "gender"]).mean()


# <a id="17"></a>
# **11.MERGE**

# In[162]:


dic1= { "Name":["alice","bob","clarke", "steve","eva", "jason"],
        "Ages":[25,36,40,44,33,28],
        "Salary":[100,232, 300, 50, 140,500] }
#Creating a dataframe
dt1= pd.DataFrame(dic1)
dt1


# In[163]:


dic2= { "Name":["eva", "clarke", "bob", "steve", "jason", "alice"],
         "Experience" : [4, 2, 5, 10, 2, 3 ] }
#Creating a dataframe
dt2= pd.DataFrame(dic2)
dt2


# In[164]:


#Merging 2 dataframes according to names
dt = pd.merge(dt1, dt2)
dt


# **--END--**
