#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# For this project, you will act as a data researcher for the **I**nternational **H**eadquarter of **E**mpathy **A**nd **L**ogic (**IHEAL**) . You will be helping them analyze data on GDP and life expectancy from the World Health Organization and the World Bank to support their case that there is a correlation or pattern between the GDP and life expectancy of a country.
# 
# To quote the Vice President of Intuition and Systems at **IHEAL:**
# 
# > "We know in our hearts and minds that there is an unjust connection between the wealth of a nation, and the life of its people, but we can't get buy in from the people in power without the data to support this."
# 
# During this project, you will analyze, prepare, and plot data,  and seek to answer questions in a meaningful way.
# 
# After you perform analysis, you'll be creating a blog post to share on the **IHEAL** website.
# 
# **BIG Question**: Is there a correlation between GDP and life expectancy of a country?
# 
# GDP Source:[World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)national accounts data, and OECD National Accounts data files.
# 
# Life expectancy Data Source: [World Health Organization](vhttp://apps.who.int/gho/data/node.main.688)
# 

# ## Step 1

# Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# ## Step 2

# Load the dataset and inspect it:

# Load **gdp_data_washed.csv** into a DataFrame called `gdp`. Then, quickly inspect the DataFrame using `.head()`.
# 
# (Hint: Use the `pd.read_csv()`function).
# 

# In[20]:


df = pd.read_csv('../all_data.csv')
print(len(df.index))


# Load **life_expectancy_data_washed.csv** into a DataFrame called `life`. Then, quickly inspect the DataFrame using `.head()`.

# In[21]:


print(df.head(10))


# ## Step 3

# Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.
# 
# - GDP stands for **G**ross **D**omestic **P**roduct. GDP is a monetary measure of the market value of all final goods and services produced in a time period. 
# - The GDP values are in current US dollars.

# Answer the following questions by inspecting the data in the file **gdp_data_washed.csv**.

# What five countries are represented in the data?

# In[23]:


print(df.groupby("Country").count())


# What years are represented in the data?

# In[22]:


print(df.groupby("Year").count())


# Answer the following questions by inspecting the data in the file **life_expectancy_data_washed.csv**.

# Check that the same five countries are represented in the data. 
# 
# Which of the five countries represented in the data, do you think would win in a soccer (futbol) tournament?

# In[ ]:


'Germany'


# How many rows are there for each country (careful, this one can be a bit tricky)?

# In[24]:


print(df.groupby("Country").count())


# What determines the order that each countries row entries are in. (What order are the 'China' entries in?)

# In[ ]:


"Alphabetical"


# ## Step 4
# 
# Look at the column names of the DataFrame `life` using `.head()`. 

# In[26]:


print(df.columns)


# What do you notice? The first two column names are one word each, and the third is five whole words long! `Life expectancy at birth (years)` is descriptive, which will be good for labeling the axis, but a little difficult to wrangle for coding the plot itself. 
# 
# Use Pandas to change the name of the last column to `LEABY`.
# 
# (Hint: Use `.rename()`. [You can read the documentation here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html). Make sure to pass ` inplace=True` as the second argument).

# In[32]:


df.rename(columns={'Life expectancy at birth (years)' : 'LEABY'}, inplace= True)


# Run `life.head()` again to check your new column name worked.

# In[33]:


print(df.head())


# Call `.head()` on the DataFrame `gdp`.

# In[ ]:





# If you look at the two DataFrames, you can see that the `Year` column is in a different position in each one. It will be easier to work with these DataFrames if they are set up as similarly as possible. 
# 
# Using Pandas rearrange the columns so that `Year` is the second (named) column in `gdp`. Then check your work with `.head()`.

# In[ ]:





# ## Step 5
# 
# We want to compare the GDPs of the countries over time, in order to eventually look for correlation between GDP and life expectancy. 
# 
# Plot the `gdp` DataFrame on a Seaborn `.pointplot()`
# 

# Start by setting the variables `f, ax` equal to `plt.subplots()`. This will instantiate a figure and give us access to the axes through the variable name `ax`. 
# 
# Then, set the size of the figure to 15x6 by passing `figsize=(15, 6)` to `plt.subplots()`.
# 

# The syntax for a Seaborn point plot is:
# ```python
# sns.pointplot(x="", y="", hue = "", data=)
# ```
# Create a point plot from the DataFrame `gdp`, using the "Year" column for the `x` argument, the "GDP" column for the `y` argument, and the "Country" column for the `hue` argument. Use the variable `ax` for your plot, like this:
# ```python
# ax = sns.pointplot()
# ```
# 

# In[44]:


f, ax = plt.subplots(figsize=(15,6))
ax = sns.pointplot(x= df.Year, y= df.GDP, hue= df.Country)
plt.xticks(rotation=70)
ax.set(ylabel="GDP in Trillions of U.S. Dollars")
plt.show()


# The years across the x-axes are difficult to read because there are so many values. One way to address this issue is to rotate the tick labels. Rotate the x-axes tick labels in your plot using `plt.xticks(rotation=70)`
# 
# Also set the label of the y-axis using the following line of code:
# `ax.set(ylabel="GDP in Trillions of U.S. Dollars")`

# In[ ]:





# Because the values of GDP are so high, the tick labels on the y-axis can be a little confusing. You can reformat the values to be in trillions using the code we've put in the cell for you below. Run the code to see the difference.

# In[45]:


from matplotlib.ticker import FuncFormatter
def trillions(x, pos):
    'The two args are the value and tick position'
    return '$%1.1fT' % (x*1e-12)

formatter = FuncFormatter(trillions)


f, ax = plt.subplots(figsize=(15, 6)) 
ax = sns.pointplot(x="Year", y="GDP", hue = "Country", data=df)
plt.xticks(rotation=70)
ax.yaxis.set_major_formatter(formatter)


# What are your first impressions looking at the visualized data?
# 
# - Which countries' line changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in GDP over time? 
# - Can you think of any reasons that the data looks like this for particular countries?

# In[ ]:





# ## Step 6

# To compare GDP and life expectancy over time we also need to plot the life expectancy data. 

# Start again by  setting the variables `f, ax ` equal to `plt.subplots()`. Set the size of the figure to 12x6.
# 
# Create a point plot from the DataFrame `life`, using the "Year" column for the `x` argument, the "LEABY" column for the `y` argument, and the "Country" column for the `hue` argument. Use the variable `ax` for your plot, like this:
# ```python
# ax = sns.pointplot()
# ```
# 
# Set the y-axis label back to "Life expectancy at birth (years)" using `ax.set()`.

# In[47]:


f, ax = plt.subplots(figsize=(15, 6)) 
ax = sns.pointplot(x="Year", y="LEABY", hue = "Country", data=df)
plt.xticks(rotation=70)
ax.set(ylabel= "Life expectancy at birth (years)")


# What are your first impressions looking at the visualized data?
# 
# - Which countries' line changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in life expectancy over time? 
# - Can you think of any reasons that the data looks like this for particular countries?

# In[ ]:


"From 2000 to 2015, even if we can say that life expectancy increased in most country, we can mostly say that it plateaued and didn`t improve by much. It even decreased in Mexico from 2007 to 2010. Zimbabwe is an outliner and still has poor life expectancy"


# ## Step 7

# To create a visualization that will make it easier to see the possible correlation between GDP and life expectancy, you can plot each set of data on its own subplot, on a shared figure.
# 
# To make this easier, we have created a CSV file that has columns for both GDP and life expectancy for the years 2000-2015.
# 
# Use `pd.read_csv()` to import the file **combined_data.csv** to a variable named `combined_data`. Then, check the new DataFrame using `.head()`.
# 

# In[ ]:





# ## Step 8

# Create a figure with two subplots, divided into 2 rows and 1 column. 
# 
# - We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()`
#     - `2`-- the number of rows for the subplots
#     - `1` -- the number of columns for the subplots
#     - `figsize=(15, 15)` -- the size of the figure
# 
# 
# Use the `combined_data` DataFrame to create point plots for the GDP and Life expectancy over the same 16 years.
# 
# The code for `pointplot()` will be the same as you have previously used in this project, with the addition of the `ax` argument which can be added after the `data` argument.
# - Set the `ax` argument for one `pointplot()` to `ax1`, and the other to `ax2`.
# 
# You can also give each plot a title using
# - `ax2.set_title("")`
# - `ax1.set_title("")`

# In[54]:


from matplotlib.ticker import FuncFormatter
def trillions(x, pos):
    'The two args are the value and tick position'
    return '$%1.1fT' % (x*1e-12)

formatter = FuncFormatter(trillions)


f, (ax1, ax2) = plt.subplots(2, 1, figsize= (15,15))
ax1 = sns.pointplot(x="Year", y="GDP", hue = "Country", data=df, ax=ax1)
plt.xticks(rotation=70)
ax.yaxis.set_major_formatter(formatter)
ax2 = sns.pointplot(x="Year", y="LEABY", hue = "Country", data=df, ax=ax2)

plt.xticks(rotation=70)
ax2.set(ylabel= "Life expectancy at birth (years)")


# You may have to look closely to see the GDP difference between Zimbabwe and the Dominican Republic, as they are very similar over this time period. 

# Which countries have the highest and lowest GDP?

# 

# Which countries have the highest and lowest life expectancy?

# 

# ## Step 9

# ### Researching Data Context 
# Based on the visualization, choose one part the data to research a little further so you can add some real world context to the visualization. You can choose anything you like, or use the example question below.
# 
# What happened in China between 1991-2016 that increased the GDP so drastically?

# In[ ]:





# ## Step 10

# Use the content you have created in this Jupyter notebook to create a blog post on this data.

# In[ ]:




