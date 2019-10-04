#!/usr/bin/env python
# coding: utf-8

# In[27]:


class Encriptador:
    
    def __init__(self):   
        self.texto=''
        self.clave=''
        
        
    def cifrar(self, texto, clave):        
        largoClave=int(len(clave))
        datos=[]
        
        #Se agregan los caracteres de la clave en una lista con su respectivo numero decimal equivalente(ASCII)        
        for col in range(largoClave):            
            datos.append([{'letra':clave[col],'numero':ord(clave[col])}])           
        
        #Se llena la lista de listas
        for col in range(largoClave):
            puntero=col
            while puntero<len(texto):
                datos[col].append(texto[puntero])
                puntero+=largoClave
        
            
       
        
        cifrada=''
        datos.sort(key = lambda x:x[0]['numero'])
       
        for e in datos:            
                for l in e:
                    if type(l)==str:
                        cifrada+=l
            
        
        s = ''
        return s.join(cifrada)
            

