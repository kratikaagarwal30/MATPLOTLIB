#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-darkgrid') 


# 2D Line Plot
# 
# Used for:
# 1. Bivariate Analysis
# 2. Can be used for numerical numerical data but usually prefered for numerical- categorical data.
# 3. Usually ploted on time series data( data that is recorded over consistent intervals of time).
# 

# In[2]:


#plotting a simple function
price = [48000,54000,57000,49000,47000,45000]
year = [2015,2016,2017,2018,2019,2020]
plt.plot(year, price, label='Price Trend')
#on x axis put categorical column 


# In[3]:


batsman = pd.read_csv("sharma-kohli.csv")
batsman


# In[4]:


batsman.info()


# In[5]:


plt.plot(batsman["index"], batsman["V Kohli"] )


# In[6]:


#plotting multiple plots
plt.plot(batsman["index"], batsman["RG Sharma"], color = 'blue')
plt.plot(batsman["index"], batsman["V Kohli"], color = "red")


# In[7]:


#labels title 
#plotting the same above graph only but with titles on graph
plt.plot(batsman["index"], batsman["RG Sharma"], color = 'blue')
plt.plot(batsman["index"], batsman["V Kohli"], color = "red")
plt.title("Rohit Sharma vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")


# In[8]:


#plotting dashed lines
plt.plot(batsman["index"], batsman["RG Sharma"], color = 'blue', linestyle = "dashed")
plt.plot(batsman["index"], batsman["V Kohli"], color = "red", linestyle = "dashed")
plt.title("Rohit Sharma vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")


# In[9]:


#plotting dotted graph
plt.plot(batsman["index"], batsman["RG Sharma"], color = 'blue', linestyle = "dotted")
plt.plot(batsman["index"], batsman["V Kohli"], color = "red", linestyle = "dotted")
plt.title("Rohit Sharma vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")


# In[10]:


#plotting dashed dotted
plt.plot(batsman["index"], batsman["RG Sharma"], color = 'blue', linestyle = "dashdot")
plt.plot(batsman["index"], batsman["V Kohli"], color = "red", linestyle = "dashdot")
plt.title("Rohit Sharma vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")


# In[11]:


#altering the linewidth of graphs also
plt.plot(batsman["index"], batsman["RG Sharma"], color = 'blue', linewidth = 5)
plt.plot(batsman["index"], batsman["V Kohli"], color = "red", linewidth = 2)
plt.title("Rohit Sharma vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")


# In[12]:


#adding markers on the graph
plt.plot(batsman["index"], batsman["RG Sharma"], color = 'blue', linestyle = "dotted",marker = "X")
plt.plot(batsman["index"], batsman["V Kohli"], color = "red", marker = "X")
plt.title("Rohit Sharma vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")


# In[13]:


#adding markers size also on the graph
plt.plot(batsman["index"], batsman["RG Sharma"], color = 'blue', linestyle = "dotted",marker = "X", markersize = 10)
plt.plot(batsman["index"], batsman["V Kohli"], color = "red", marker = "P", markersize = 10)
plt.title("Rohit Sharma vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")


# In[14]:


#legend location
plt.plot(batsman["index"], batsman["RG Sharma"], color = 'blue', label = "Virat",marker = "X")
plt.plot(batsman["index"], batsman["V Kohli"], color = "red", label = "Rohit", marker = "X")
plt.title("Rohit Sharma vs Virat Kohli Career Comparison")
plt.xlabel("Season")
plt.ylabel("Runs Scored")
plt.legend()


# In[15]:


#limiting axes
price = [48000,54000,57000,49000,47000,45000,4500000]
year = [2015,2016,2017,2018,2019,2020,2021]
plt.plot(year, price, color = 'blue',marker = "X")
#herec we have one outlier, so the remaining curve will start looking flat in comparison to outliers
#the variation of the remaining graph will not be captured


# In[16]:


price = [48000,54000,57000,49000,47000,45000,4500000]
year = [2015,2016,2017,2018,2019,2020,2021]
plt.plot(year, price, color = 'blue',marker = "X")
plt.ylim(0, 100000)
plt.xlim(2015,2020)


# If you are writing code in another text editor, then you have to write plt.show() to display graphs

# SCATTER PLOTS
# 
# USED FOR:
# 1. BIVARIATE ANALYSIS
# 2. USED ON NUMERICAL VS NUMERICAL COLUMNS MOSTLY
# 3. USE CASE: FINDING CORRELATION

# In[17]:


#plot scatter simple function
x = np.linspace(-10,10,50)
y = 10*x +3 + np.random.randint(0,300,50)
plt.scatter(x,y)


# In[18]:


df = pd.read_csv("batter.csv")
df


# In[19]:


#avg tells that batsman is more reliable
#strike rate tells that batsman is more destructible
#you are an IPL Team owner and you want to decide that which batsman you need to buy for your team
#so you will use this dataset to decide the same


# In[23]:


df = df.head(50)


# In[28]:


plt.scatter(df["avg"], df["strike_rate"], linewidth = 5, color = "red", marker = "+" )
plt.title("Avg and strike rate analysis of top 50" )
plt.xlabel("Avg")
plt.ylabel("Strike Rate")
#you want to chose a batsman who is superreliable and super desteructive


# In[30]:


#plotting scatter plot using plt.plot
#it is faster as compared to plt.scatter()
plt.plot(df["avg"], df["strike_rate"], "o")


# BAR CHART
# 
# USED FOR:
# 1. Bivariate/univariate analysis
# 2. Generally used for num-cat column
# 3. USE CASE: Aggregate analysis of groups

# In[31]:


#simple bar chart
children = [10,20,40,10,30]
colors = ["red", "blue", "green", "yellow", "pink"]
plt.bar(colors, children)


# In[32]:


#horizontal bar chart
plt.barh(colors, children)


# In[33]:


df = pd.read_csv("batsman_season_record.csv")
df


# In[39]:


#bar chart
plt.bar(df["batsman"], df["2015"])


# In[40]:


#multiple bar charts 
#plotting in this way won't look much good 
plt.bar(df["batsman"], df["2015"])
plt.bar(df["batsman"], df["2016"])
plt.bar(df["batsman"], df["2017"])


# In[42]:


plt.bar(df["batsman"], df["2015"], width = 0.1)


# In[45]:


plt.bar(np.arange(df.shape[0]) - 0.2, df["2015"], width = 0.2, color = "yellow")
plt.bar(np.arange(df.shape[0] ), df["2016"], width = 0.2, color = "red")
plt.bar(np.arange(df.shape[0]) + 0.2, df["2017"], width = 0.2, color = "blue")

plt.xticks(np.arange(df.shape[0]), df["batsman"])

 plt.show()


# In[48]:


#usage of xticks
plt.bar(np.arange(df.shape[0]) - 0.2, df["2015"], width = 0.2, color = "yellow")
plt.bar(np.arange(df.shape[0] ), df["2016"], width = 0.2, color = "red")
plt.bar(np.arange(df.shape[0]) + 0.2, df["2017"], width = 0.2, color = "blue")

plt.xticks(np.arange(df.shape[0]), df["batsman"], rotation = "vertical")

plt.show()


# In[51]:


# Stacked Bar chart
plt.bar(df['batsman'],df['2017'],label='2017')
plt.bar(df['batsman'],df['2016'],bottom=df['2017'],label='2016')
plt.bar(df['batsman'],df['2015'],bottom=(df['2016'] + df['2017']),label='2015')

plt.legend()
plt.show()


# HISTOGRAM
# 
# USED FOR:
# 1. Univariate analysis
# 2. Numerical column
# 3. USE CASE: Frequency counts 

# In[53]:


#simple data
data = [32,45,56,10,15,27,61]
plt.hist(data)


# In[54]:


df = pd.read_csv("vk.csv")


# In[55]:


df


# In[57]:


plt.hist(df["batsman_runs"], bins = [0,10,20,30,40,50,60,70,80,90,100,110,120])
plt.show()


# PIE CHART
# 
# USED FOR :
# 1. Univariate/Bivariate Analysis
# 2. Categorical vs numerical
# 3. Use case - To find contibution on a standard scale

# In[72]:


data = [23,45,100,20,49]
subjects = ['eng','science','maths','sst','hindi']
plt.pie(data, labels = subjects)

plt.savefig("sample1.png")


# In[62]:


df = pd.read_csv("gayle-175.csv")
df


# In[65]:


plt.pie(df["batsman_runs"], labels = df["batsman"], autopct='%0.1f%%')
plt.show()


# In[66]:


# percentage and colors
plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%',colors=['blue','green','yellow','pink','cyan','brown'])
plt.show()


# In[70]:


# explode shadow
plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%',explode=[0.3,0,0,0.5,0,0.1],shadow=True)
plt.show()
plt.savefig("sample.png")


# In[74]:


iris = pd.read_csv("iris.csv")


# In[80]:


iris.sample(5)


# In[79]:


plt.scatter(iris["SepalLengthCm"], iris["PetalLengthCm"])
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")


# In[82]:


iris["Species"] = iris["Species"].replace({"Iris-setosa" : 0, "Iris-versicolor" : 1, "Iris-virginica": 2})


# In[83]:


iris


# In[89]:


plt.scatter(iris["SepalLengthCm"], iris["PetalLengthCm"], c = iris["Species"], cmap = "jet")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.colorbar()


# PLOT SIZE

# In[91]:


plt.figure(figsize = (15,7))
plt.scatter(iris["SepalLengthCm"], iris["PetalLengthCm"], c = iris["Species"], cmap = "jet")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.colorbar()


# ANNOTATIONS

# In[92]:


batters = pd.read_csv("batter.csv")


# In[93]:


batters


# In[94]:


#we will work on 25 batsman
sample_df = batters.head(100).sample(25,random_state=5)


# In[ ]:


plt.scatter(sample_df["avg"], sample_df["strike_rate"])


# In[100]:


x = [1,2,3,4]
y = [5,6,7,8]
plt.scatter(x,y)
plt.text(1,5,"Point 1")
plt.text(2,6,"Point 2")
plt.text(3,7,"Point 3")
plt.text(4,8,"Point 4", fontdict  = {'size': 12, "color" : "brown"})


# In[102]:


plt.figure(figsize = (18,10))
plt.scatter(sample_df["avg"], sample_df["strike_rate"])
for i in range(sample_df.shape[0]):
  plt.text(sample_df["avg"].values[i], sample_df["strike_rate"].values[i], sample_df['batter'].values[i])  


# Horizontal and Vertical lines

# In[103]:


plt.figure(figsize=(18,10))
plt.scatter(sample_df['avg'],sample_df['strike_rate'],s=sample_df['runs'])

plt.axhline(130,color='red')
plt.axhline(140,color='green')
plt.axvline(30,color='red')

for i in range(sample_df.shape[0]):
  plt.text(sample_df['avg'].values[i],sample_df['strike_rate'].values[i],sample_df['batter'].values[i])


# SUBPLOTS

# In[104]:


batters.head()


# In[106]:


fig, ax = plt.subplots()
ax.scatter(batters["avg"], batters["strike_rate"])
ax.set_title("Something")


# In[110]:


fig, ax = plt.subplots(figsize = (18,9))
ax.scatter(batters["avg"], batters["strike_rate"])
ax.set_title("Something")
ax.set_xlabel("Average")
ax.set_ylabel("strike_rate")
fig.show()


# In[118]:


#Creating side-by-side visual comparisons of average vs. strike rate, and runs vs. average.
fig, ax = plt.subplots(nrows = 2, ncols = 1, sharex = True, figsize = (10,6))
ax[0].scatter(batters["avg"], batters["strike_rate"], color = "red")
ax[1].scatter(batters["avg"], batters["runs"])
ax[0].set_title("AVG VS STRIKE RATE")
ax[0].set_ylabel("Strike Rate")
ax[1].set_xlabel("Average")
ax[1].set_title("AVG VS RUNS")
ax[1].set_ylabel("RUNS")


# In[125]:


fig, ax = plt.subplots(nrows = 2, ncols= 2)
ax[0,0].scatter(batters["avg"], batters["strike_rate"])
ax[0,1].scatter(batters["avg"], batters["runs"])
ax[1,0].hist(batters["avg"])
ax[1,1].hist(batters["avg"])
ax[0,0].set_title("AVG VS STRIKE RATE")
ax[0,1].set_title("AVG VS RUNS")
ax[1,0].set_title("RUNS ")
ax[1,1].set_title( "STRIKE RATE")


# In[126]:


fig = plt.figure()

ax1 = fig.add_subplot(2,2,1)
ax1.scatter(batters['avg'],batters['strike_rate'],color='red')

ax2 = fig.add_subplot(2,2,2)
ax2.hist(batters['runs'])

ax3 = fig.add_subplot(2,2,3)
ax3.hist(batters['avg'])


# HEATMAP

# In[128]:


delivery = pd.read_csv("IPL_Ball_by_Ball_2008_2022 (1).csv")
delivery


# In[ ]:


#jitne bhi matches hue hein ipl mein usme hrr over ki hrr baal pr kine sixes lge hein
#y axis : overs
#x axis : balls


# In[130]:


temp_df = delivery[(delivery['ballnumber'].isin([1,2,3,4,5,6])) & (delivery['batsman_run']==6)]


# In[131]:


grid = temp_df.pivot_table(index='overs',columns='ballnumber',values='batsman_run',aggfunc='count')


# In[132]:


grid


# In[135]:


plt.figure(figsize = (20,10))
plt.imshow(grid, cmap = "jet")
plt.colorbar()


# In[ ]:




