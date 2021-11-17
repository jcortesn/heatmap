#!/usr/bin/env python
# coding: utf-8

# Proyecto para crear un heatmap en Python a partir de un csv con datos de la AEMAT sobre la lluvia y las horas de sol en una estación del Retiro

# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("C:/Users/josej/Desktop/Datos precipitacion&horas sol Retiro 6.xlsx")


# In[18]:


# Hacemos un primer grid sin valores, pero en la que se pueden ver ya correlacion entre los diferentes valores.
# Como en el caso de los coches, año, no tendría mucho sentido, pero lo mantengo para ver los resultados
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(data.corr(), center=0, cmap='Blues')
ax.set_title('Relacion precipitacion - horas de sol')


# In[19]:


# Ahora lo hacemmos con valores para ver las correlaciones concretas
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(data.corr(), center=0, cmap='BrBG', annot=True)


# In[2]:


# Hacemos lo mismo con más variables
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_excel("C:/Users/josej/Desktop/Datos precipitacion&horas sol Retiro (3) - TC.xlsx")


# In[3]:


fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(data.corr(), center=0, cmap='Blues')
ax.set_title('Relacion multivariable clima')


# In[4]:


fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(data.corr(), center=0, cmap='BrBG', annot=True)


# In[6]:


# Y otra forma de representarlo
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from datetime import datetime

data = pd.read_excel("C:/Users/josej/Desktop/Datos precipitacion&horas sol Retiro (3) - TC.xlsx")

plt.figure(figsize=(10,10))
heat_map = sns.heatmap(data.corr(), linewidth = 1 , annot = True)
plt.title( "HeatMap using Seaborn Method" )
plt.show()


# In[ ]:




