#!/usr/bin/env python
# coding: utf-8

# In[16]:


from Encriptador import Encriptador
from IPython.display import clear_output
e1=Encriptador()
print("Ingrese texto a cifrar")
texto = input()
print("Ingrese clave")
clave = input()
clear_output()
print('Texto cifrado:',e1.cifrar(texto,clave))


# In[ ]:





# In[ ]:




