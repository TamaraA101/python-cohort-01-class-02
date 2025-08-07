# %% [markdown]
# # Python Syntax
# 
# ## What is Syntax?
# 
# 
# 

# %%
a = 20
print(a)

# %%
crypto = input("Enter your favorite crypto asset: ")
print(f'Your favorite crypto asset is: {crypto}')

# %%
name = "Alice"
age = 30
print("My name is + name")


# %%
a = 20
b = 30

#Adding a and b to get c
c = a + b
print(a + b)

# %%
# f-strings
crypto_asset = "Bitcoin"
print(f'My favorite crypto asset is {crypto_asset}')

# %%
crypto = input("Enter your favorite crypto asset: ")
print("My favorite crypto asset is " + crypto)

# %%
age=int(input("Enter your age: "))
print(age)
print(f'Your are {age} years old')

# %% [markdown]
# # Variables
# 
# ## What is a Variables ?
# 
# A named container that stores data (like a labelled box)

# %%
# Assignment

x = 10
y = 20

# Multiple assignment
x, y = 10, 20

# %% [markdown]
# # Data Types
# 
# ## What are Data Types
# 
# A Python data type specifies the category of data a variable can cab store, determinig its behaviour and allowed operations
# 
# ### Common Types
# 
# ### Text Data Type

# %%
# Text Data Type
# Also known as string, are used to represent text

place = "Lagos"         # This is a string variable
country = "Nigeria"     # This is another string variable
print(f'I live in {place}, {country}')

# %% [markdown]
# ### Numeric Data Type
# 

# %%
# Numeric Data Type

number = 10     # This is an integer variable
height = 4.7    # This is a float variabl

# %% [markdown]
# ### Boolen Data Type

# %%
# Boolen Data Type

is_valid = True  # This is a boolean variable (True)
invalid = False  # This is another boolean variable (False)

# %% [markdown]
# ### Sequence Data Type
# 

# %%
cryptos = ["Bitcoin", "Ethereum", "Litecoin"]  # This is a list variable
cryptos


# %%
dict = {'btc': 90000, 'eth': 2000, 'ltc': 150}  # This is a dictionary variable
print(dict)

# %%
# Sequence Data Type

list_example = [1, 2, 3, 4, 5]  # A list is an ordered collection of items

tuple_example = (1, 2, 3)  # A tuple is an ordered collection of items that cannot be changed

dictionary_example = {"key1": "value1", "key2": "value2"}  # A dictionary is a collection of key-value pairs

set_example = {1, 2, 3}  # A set is an unordered collection of unique items


# %% [markdown]
# ### None Data Types

# %%
none_value = None  # This is a NoneType variable, represents the absence of a value

# %% [markdown]
# ### Checking Data Types

# %%
age = 90
print(type(age))  # This will print <class 'int'>


# %%
name = "Alice"
print(type(name))  # This will print <class 'str'>

age = 30
print(type(age))  # This will print <class 'int'>

names= ["Alice", "Bob", "Charlie"]
print(type(names))  # This will print <class 'list'>

data= {"name": "Alice", "age": 30}
print(type(data))  # This will print <class 'dict'>

# %% [markdown]
# ### Converting Data Type

# %%
age = '90'
age = int(age)  # Convert string to integer
print(age)  # This will print 90


# %%
print(type(age))  # This will print <class 'int'>


# %%
number = 10
number = str(number)  # Convert integer to string
print(number)  # This will print '10'

# %%
print(type(number))  # This will print <class 'int'>


