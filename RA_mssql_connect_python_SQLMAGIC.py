#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd
get_ipython().run_line_magic('load_ext', 'sql')


# In[84]:


import pyodbc


# In[89]:


import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-4E75C8B;'
                      'Database=Rob;'
                     'Connections=true;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM student')

for row in cursor:
    print(row)


# In[74]:


cursor.execute('Insert into student
Values(3,'Gunner','Arnold', 9217652233, 'gggg@gmail.com')')
for row in cursor:
    print(row)


# In[53]:


get_ipython().run_cell_magic('sql', '', 'select * from Student')


# In[54]:


Integrated Security=SSPI;Persist Security Info=False;Initial Catalog=Rob;Data Source=DESKTOP-4E75C8B;


# In[56]:


get_ipython().run_line_magic('sql', "postgresql:Server='DESKTOP-4E75C8B';Database='Rob';Trusted_Connection=True;")


# In[55]:


get_ipython().run_line_magic('sql', 'postgresql://DESKTOP-4E75C8B/Rob')


# In[43]:


postgresql://user:secret@localhost


# In[98]:


get_ipython().run_line_magic('sql', "dict_keys([Server='DESKTOP-4E75C8B';Database='Rob'])")


# In[99]:


import pandas as pd
import pyodbc
import numpy as np
import sqlalchemy


# In[100]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[101]:


import urllib
params = urllib.parse.quote_plus("DRIVER={SQL SERVER};SERVER=DESKTOP-4E75C8B;DATABASE=Rob;TRUSTED_CONNECTION=YES")
"mssql+pyodbc:///?odbc_connect=%s" % params


# In[104]:


get_ipython().run_cell_magic('sql', 'mssql+pyodbc:///?odbc_connect=DRIVER%3D%7BSQL+SERVER%7D%3BSERVER%3DDESKTOP-4E75C8B%3BDATABASE%3DRob%3BTRUSTED_CONNECTION%3DYES', 'select * from student')


# In[105]:


get_ipython().run_cell_magic('', 'sql', 'select * from student')


# In[106]:


connection_str = "DRIVER={SQL SERVER};SERVER=DESKTOP-4E75C8B;DATABASE=Rob;TRUSTED_CONNECTION=YES"
connection_str_quoted = urllib.parse.quote_plus(connection_str)
connection_uri = 'mssql+pyodbc:///?odbc_connect={}'.format(connection_str_quoted)

# this is how you would connect in sqlalchemy
import sqlalchemy
conn = sqlalchemy.create_engine(connection_uri)

get_ipython().run_line_magic('sql', '{connection_uri}')


# In[107]:


get_ipython().run_cell_magic('sql', '', 'select * from student')


# In[108]:


get_ipython().run_cell_magic('sql', '', "Insert into student \nvalues(3,'Priya','John',9811841133,'zy@gamil.com')")


# In[109]:


get_ipython().run_cell_magic('sql', '', 'select * from student')


# In[ ]:




