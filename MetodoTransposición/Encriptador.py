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
        #Lista que almacena el numero decimal de los caracteres de la clave con un orden de menor a mayor para formar la cadena cifrada  
        orden=[]
        for e in datos:
            orden.append(e[0]['numero'])
            
        orden.sort(reverse=False) 
        
        cifrada=''
        c=0
        #Se forma la cadena cifrada segun el orden definido en la lista 'orden', se compara el numero de orden con numero del diccionario dentro de la lista de cada caracter en 'datos' 
        for i in orden:
            for e in datos:
                if i==e[c]['numero']:
                    for l in e:
                        if type(l)==str:
                            cifrada+=l
                else:
                    c+1
        
        s = ''
        return s.join(cifrada)
            

