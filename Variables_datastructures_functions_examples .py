#!/usr/bin/env python
# coding: utf-8

# # Variables

# In[13]:


val=10
anyName="data training"
key_values= {"India": 29, "USA":50}


# ## Standard Data Structures in python

# ### immutable data types

# In[14]:


#Tuple data type
Tuple_val=(1,2,3)
print(id(Tuple_val))


# In[15]:


Tuple_val=(1,2,)
print(id(Tuple_val))


# In[16]:


#string data type
string_val="big data training"
print(id(string_val))


# In[17]:


string_val="data training"
print(id(string_val))


# # mutable data types

# In[18]:


#list data type
list_val=[1,2,3,4]
print(id(list1))
print(type(list1))


# In[19]:


list_val=[1,2,3,4]
print(id(list1))
print(type(list1))


# In[21]:


#dictionary
dict_val = {
    'a': 'alpha',
    'b': 'bravo',
    'c': 'charlie',
    'd': 'delta',
    'e': 'echo'
}
print(id(dict_val))


# In[22]:


dict_val.update({
    'f': 'foxtrot'
})
print(id(dict_val))


# ## Functions- Explaination

# In[24]:


salary=50000; # This is global variable.
# Function definition is here
def salary_calculator( salary, number_of_months ):
   # multiply both the parameters and return them."
   salary = salary * number_of_months; # Here salary is local variable.
   print("local salary : ", salary)
   return salary;


# In[26]:


# Now you can call salary_calculator function
salary_calculator( 50000, 5 );
print("global salary value : ", salary)


# In[ ]:




