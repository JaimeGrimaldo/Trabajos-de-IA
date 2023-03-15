import os
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import *

#Datos iniciales
class AG_Paqueteria:

     def __init__(self,Tam_Pob_Inic,Tam_Pob_Max,Prob_Mut_Ind,Prob_Mut_Gen,numgeneraciones,espacio_contenedor):

          self.Tam_Pob_Inic= Tam_Pob_Inic  
          self.Tam_Pob_Max = Tam_Pob_Max # Debe ser mayor que Tam_Pob_Inic 
          self.Prob_Mut_Ind= Prob_Mut_Ind
          self.Prob_Mut_Gen= Prob_Mut_Gen
          self.numgeneraciones= numgeneraciones
          self.espacio_contenedor=espacio_contenedor

          

          self.num_de_categorias=5
          self.categorias=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

          self.tamaño=[7,11,9,5,7]
          self.precio_publico=[100,50,50,100,60]
          self.costo_de_envio=[35,28,29,28,31]
          self.cantidad_paqs_por_cat=[9,10,9,10,9]

          self.gan_gen_cat=np.zeros((self.numgeneraciones,len(self.tamaño)))

     def setTam_Pob_Inic(self,Tam_Pob_Inic):
          self.Tam_Pob_Inic = Tam_Pob_Inic

     def setTam_Pob_Max(self,Tam_Pob_Max):
          self.Tam_Pob_Max = Tam_Pob_Max

     def setProb_Mut_Ind(self,Prob_Mut_Ind):
          self.Prob_Mut_Ind = Prob_Mut_Ind

     def setProb_Mut_Gen(self,Prob_Mut_Gen):
          self.Prob_Mut_Gen = Prob_Mut_Gen

     def setnumGeneraciones(self,numGeneraciones):
          self.numgeneraciones = numGeneraciones

     def setEspacio_contenedor(self,espacio_contenedor):
          self.espacio_contenedor = espacio_contenedor
     
     def setPaqueteA(self,lista):
          self.tamaño[0]=lista[0]
          self.cantidad_paqs_por_cat[0]=lista[1]
          self.precio_publico[0]=lista[2]
          self.costo_de_envio[0]=lista[3]

     def setPaqueteB(self,lista):
          self.tamaño[1]=lista[0]
          self.cantidad_paqs_por_cat[1]=lista[1]
          self.precio_publico[1]=lista[2]
          self.costo_de_envio[1]=lista[3]

     def setPaqueteC(self,lista):
          self.tamaño[2]=lista[0]
          self.cantidad_paqs_por_cat[2]=lista[1]
          self.precio_publico[2]=lista[2]
          self.costo_de_envio[2]=lista[3]

     def setPaqueteD(self,lista):
          self.tamaño[3]=lista[0]
          self.cantidad_paqs_por_cat[3]=lista[1]
          self.precio_publico[3]=lista[2]
          self.costo_de_envio[3]=lista[3]

     def setPaqueteE(self,lista):
          self.tamaño[4]=lista[0]
          self.cantidad_paqs_por_cat[4]=lista[1]
          self.precio_publico[4]=lista[2]
          self.costo_de_envio[4]=lista[3]

     
     def getPaqueteA(self):
          lista=[]
          lista.append(self.tamaño[0])
          lista.append(self.cantidad_paqs_por_cat[0])
          lista.append(self.precio_publico[0])
          lista.append(self.costo_de_envio[0])
          
          return lista

     def getPaqueteB(self):
          lista=[]
          lista.append(self.tamaño[1])
          lista.append(self.cantidad_paqs_por_cat[1])
          lista.append(self.precio_publico[1])
          lista.append(self.costo_de_envio[1])
          
          return lista

     def getPaqueteC(self):
          lista=[]
          lista.append(self.tamaño[2])
          lista.append(self.cantidad_paqs_por_cat[2])
          lista.append(self.precio_publico[2])
          lista.append(self.costo_de_envio[2])
          
          return lista

     def getPaqueteD(self):
          lista=[]
          lista.append(self.tamaño[3])
          lista.append(self.cantidad_paqs_por_cat[3])
          lista.append(self.precio_publico[3])
          lista.append(self.costo_de_envio[3])
          
          return lista

     def getPaqueteE(self):
          lista=[]
          lista.append(self.tamaño[4])
          lista.append(self.cantidad_paqs_por_cat[4])
          lista.append(self.precio_publico[4])
          lista.append(self.costo_de_envio[4])
          
          return lista

     def iniciar_programa(self):

          pp=[]     #precio al público
          ce=[]     #costo de envio
          ta=[]     #tamaño
          individuo=[] # servirá para construir los primeros individuos al azar
          nppi=1 #número de paquetes por individuo
          #Cálculo de paquetes por individuo de la poblacion
          for k in range(len(self.cantidad_paqs_por_cat)):
               for m in range(self.cantidad_paqs_por_cat[k]):
                    ta.append(self.tamaño[k])
                    pp.append(self.precio_publico[k])
                    ce.append(self.costo_de_envio[k])
                    individuo.append(nppi)
                    nppi=nppi+1
          nppi=nppi-1

          # servirán para guardar al mayor, medio y menor     
          genmayorxi=[]
          genmayorfxi=[]
          genmedioxi=[]
          genmediofxi=[]
          genmenorxi=[]
          genmenorfxi=[]

          print('Población inicial= ',self.Tam_Pob_Inic)
          print('Población máxima= ',self.Tam_Pob_Max) 
          print('Probabilidad de mutación de un Individuo= ',self.Prob_Mut_Ind)
          print('Probabilidad de mutación Genética= ',self.Prob_Mut_Gen)
          print('No. de paquetes por individuo= ',nppi)
          print('Se van a trabajar ',self.numgeneraciones,' generaciones')
          print("")
          print("Tamaño de los paquetes (individuo)")
          print(ta)
          print("")
          print("Precio al público por paquete (individuo)")
          print(pp)
          print("")
          print("Costo de envío por paquete (individuo)")
          print(ce)
          print("")
          print("")
          print("Generamos al azar los ",self.Tam_Pob_Inic," primeros individuos de la población")
          poblacion=[]
          for m in range(self.Tam_Pob_Inic):
               indix=individuo[:]
               indiy=[]
               for k in range(nppi):
                    y=random.randint(0,len(indix)-1)
                    indiy.append(indix[y])
                    indix.remove(indix[y])
               poblacion.append(indiy)
               
          print("")
          print("Individuos de la población inicial")
          print("")
          for m in range(len(poblacion)):
               print("Individuo No.",m+1)
               print(poblacion[m])

          # Calculamos ahora el fitnes de estos individuos
          print("")
          print("Espacio del contenedor: ",self.espacio_contenedor)
          print("--------------------------------------------------")
          print(" Individuo numgens espacio  precio  costo de envio")
          print("--------------------------------------------------")
          for m in range(len(poblacion)):
               #Determinamos el número de genes sin rebasar el espacio del contenedor
               espacio=0
               precio=0
               costo=0
               k=0
               bandera=0
               while espacio<=self.espacio_contenedor and k<=41 and bandera==0:
                    paq=poblacion[m][k]-1
                    if espacio+ta[paq]<=self.espacio_contenedor:
                         espacio=espacio+ta[paq]
                         precio=precio+pp[paq]
                         costo=costo+ce[paq]
                    else:
                         bandera=1
                    k=k+1
               print("    ",m+1, "      ",k-1,"   ",espacio,"   ",precio,"   ", costo)


          #A partir de aquí ya debe ser iterativo el proceso
          #cruza-> mutación-> ordenamiento por fitnes -> Poda
          #cruzaremos en 4 puntos, dividiendo los genes de cada individuo: nppi
          puntos=[]
          puntos.append(int(nppi*1/5))
          puntos.append(int(nppi*2/5))
          puntos.append(int(nppi*3/5))
          puntos.append(int(nppi*4/5))
          for generacion in range(self.numgeneraciones):
               # ---------------------------------------------------------------
               # Generamos cruzas de un contra todos y viceversa
               # acorde a la población actual determinamos como se cruzan
               totalganancia=0
               Tam_Pob=len(poblacion)
               cruza_A=[]
               cruza_B=[]
               for k in range(Tam_Pob):
                    for m in range(k+1,Tam_Pob):
                         cruza_A.append(k)
                         cruza_B.append(m)
                         cruza_A.append(m)
                         cruza_B.append(k)
               print(cruza_A)
               print(cruza_B)
               print("Puntos de cruza: ",puntos)
               for k in range(len(cruza_A)):
                    print("")
                    print("cruzamos: ",cruza_A[k]," con: ",cruza_B[k])
                    print("Padre 1: ",poblacion[cruza_A[k]])
                    print("Padre 2: ",poblacion[cruza_B[k]])
                    nuevo=poblacion[cruza_A[k]][0:puntos[0]]
                    nuevo=nuevo+poblacion[cruza_B[k]][puntos[0]:puntos[1]]
                    nuevo=nuevo+poblacion[cruza_A[k]][puntos[1]:puntos[2]]
                    nuevo=nuevo+poblacion[cruza_B[k]][puntos[2]:puntos[3]]
                    nuevo=nuevo+poblacion[cruza_A[k]][puntos[3]:]
                    
                    print("")
                    print("Hijo nuevo", nuevo)
                    print("Si tiene genes repetidos, estos se eliminan")
                    #Verificamos si este hijo tiene genes repetidos
                    #Si los tiene los eliminamos
                    bandera=0
                    nuevo2=[nuevo[0]]
                    for m in range(1,len(nuevo)):
                         if not nuevo[m] in nuevo2:
                              nuevo2.append(nuevo[m])
                         else:
                              print("Repetido: ",nuevo[m])
                              bandera=1
                    print("Se agregan los genes que faltan al final")
                    #Ahora incluimos a los genes faltantes
                    for m in range(len(individuo)):
                         if not individuo[m] in nuevo2:
                              nuevo2.append(individuo[m])     
                              print("Falta: ",individuo[m])
                    nuevo=nuevo2[:]
                    if bandera==1:
                         print("Hijo nuevo ya corregido", nuevo)
                         print("")

                    # -------------------Aqui inicia mutación

                    #¿Debe mutar el nuevo hijo?
                    Prob=random.randint(0, 10000)/10000
                    if self.Prob_Mut_Ind>=Prob:
                         for m in range(nppi):
                              #¿Debe mutar este gen?
                              Prob=random.randint(0, 10000)/10000
                              if self.Prob_Mut_Gen>=Prob:
                                   gentemp=random.randint(0,nppi-1)
                                   temp=nuevo[m]
                                   nuevo[m]=nuevo[gentemp]
                                   nuevo[gentemp]=temp    
                         print("Este hijo nuevo debe mutar --> Nuevo hijo mutado:", nuevo)
                    else:
                         print("Este Hijo nuevo no muta: ", nuevo)     
                    poblacion.append(nuevo)    

               # ------Hemos agregado el nuevo hijo a la población
               
               #mostramos la nueva población ampliada       
               # Calculamos ahora el fitnes de estos nuevos individuos
               print("")
               print("Población de la generación: ",generacion+1)
               print("Espacio del contenedor: ",self.espacio_contenedor)
               print("-------------------------------------------------------------")
               print(" Individuo numgens espacio  precio  costo de envio   ganancia")
               print("-------------------------------------------------------------")
               ganancia=[]
               for m in range(len(poblacion)):
                    #Determinamos el número de genes sin rebasar el espacio del contenedor
                    espacio=0
                    precio=0
                    costo=0
                    k=0
                    bandera=0
                    while espacio<=self.espacio_contenedor and k<=41 and bandera==0:
                         paq=poblacion[m][k]-1
                         if espacio+ta[paq]<=self.espacio_contenedor:
                              espacio=espacio+ta[paq]
                              precio=precio+pp[paq]
                              costo=costo+ce[paq]
                         else:
                              bandera=1
                         k=k+1
                    ganancia.append(precio-costo)    
                    print( "  ",'{0:3d}'.format(m+1), "    ",'{0:3d}'.format(k-1),"   ",'{0:4d}'.format(espacio),"   ",'{0:4d}'.format(precio),"       ", '{0:4d}'.format(costo),"       ", '{0:4d}'.format(ganancia[m]))

               #------------ Vamos a ordenar las tablas por ganancia
                    
               for m in range(len(ganancia)):
                    mayor=ganancia[m]
                    posmay=m
                    
                    for y in range(m,len(ganancia)):
                         #print('Vamos a maximizar')-->Se ordena de mayor a menor
                         if ganancia[y]>mayor:
                              mayor=ganancia[y]
                              posmay=y

                    tempmayor=ganancia[m]
                    ganancia[m]=ganancia[posmay]
                    ganancia[posmay]=tempmayor
                    
                    #Intercambiamos la población
                    tempmayor=poblacion[m][:]
                    poblacion[m]=poblacion[posmay][:]
                    poblacion[posmay]=tempmayor[:]


               print("")
               print("Ordenados de mayor a menor por ganancia")
               print("Espacio del contenedor: ",self.espacio_contenedor)
               print("-------------------------------------------------------------")
               print(" Individuo numgens espacio  precio  costo de envio   ganancia")
               print("-------------------------------------------------------------")
               ganancia=[]
               for m in range(len(poblacion)):
                    #Determinamos el número de genes sin rebasar el espacio del contenedor
                    espacio=0
                    precio=0
                    costo=0
                    k=0
                    bandera=0
                    while espacio<=self.espacio_contenedor and k<=41 and bandera==0:
                         paq=poblacion[m][k]-1
                         if espacio+ta[paq]<=self.espacio_contenedor:
                              espacio=espacio+ta[paq]
                              precio=precio+pp[paq]
                              costo=costo+ce[paq]
                         else:
                              bandera=1
                         k=k+1
                    ganancia.append(precio-costo)    
                    print( "  ",'{0:3d}'.format(m+1), "    ",'{0:3d}'.format(k-1),"   ",'{0:4d}'.format(espacio),"   ",'{0:4d}'.format(precio),"       ", '{0:4d}'.format(costo),"       ", '{0:4d}'.format(ganancia[m]))

               #Ahora sobre estos datos debemos aplicar la PODA con base en Tam_Pob_Max
               poblacion=poblacion[0:self.Tam_Pob_Max]

               #Verificamos si se realizo bien la PODA

               print("")
               print("Población despues de aplicar PODA ")
               print("Población de la generación: ",generacion+1)
               print("Espacio del contenedor: ",self.espacio_contenedor)
               print("-------------------------------------------------------------")
               print(" Individuo numgens espacio  precio  costo de envio   ganancia")
               print("-------------------------------------------------------------")
               ganancia=[]

               for m in range(len(poblacion)):
                    #Determinamos el número de genes sin rebasar el espacio del contenedor
                    espacio=0
                    precio=0
                    costo=0
                    k=0
                    bandera=0
                    while espacio<=self.espacio_contenedor and k<=41 and bandera==0:
                         paq=poblacion[m][k]-1
                         if espacio+ta[paq]<=self.espacio_contenedor:
                              espacio=espacio+ta[paq]
                              precio=precio+pp[paq]
                              costo=costo+ce[paq]
                              #checamos en que categoria cae
                              rangoini=1
                              rangofin=self.cantidad_paqs_por_cat[0]
                              for z in range(self.num_de_categorias):
                                   if paq>=(rangoini-1) and paq<=(rangofin-1):
                                        #print(paq,"  ",categorias[z],"  ",rangoini,"  ",rangofin)
                                        self.gan_gen_cat[generacion][z] = self.gan_gen_cat[generacion][z]+pp[paq]-ce[paq]
                                   rangoini=rangofin+1
                                   if z<self.num_de_categorias-1:
                                        rangofin=rangofin+self.cantidad_paqs_por_cat[z+1]    
                         else:
                              bandera=1
                         k=k+1
                    ganancia.append(precio-costo)
                    totalganancia=totalganancia+precio-costo
                    print( "  ",'{0:3d}'.format(m+1), "    ",'{0:3d}'.format(k-1),"   ",'{0:4d}'.format(espacio),"   ",'{0:4d}'.format(precio),"       ", '{0:4d}'.format(costo),"       ", '{0:4d}'.format(ganancia[m]))
                    if m==0: #el primero de la lista
                         genmayorxi.append(generacion+1)
                         genmayorfxi.append(ganancia[m])
                    if m==int(len(poblacion)/2): #el de enmedio de la lista
                         genmedioxi.append(generacion+1)
                         genmediofxi.append(ganancia[m])
                    if m==len(poblacion)-1: #el último de la lista
                         genmenorxi.append(generacion+1)
                         genmenorfxi.append(ganancia[m])
                         
               print("                     Ganancia total de la generación: ",'{0:4d}'.format(totalganancia))

          print("")
          print("Ganancias por categorias por generación ")
          texto="Generación      "
          texto3="      "
          for z in range(self.num_de_categorias):
               texto=texto+self.categorias[z]+"      "
          texto=texto+"Total"     

          texto2="-"
          for z in range(len(texto)):
               texto2=texto2+"-"          
          print (texto2)
          print (texto)
          print (texto2)
          for y in range(self.numgeneraciones):
               texto3="    "+str('{0:2d}'.format(y))+"    "
               suma=0
               for z in range(self.num_de_categorias):
                    texto3=texto3+ "  "+str('{0:5d}'.format(int(self.gan_gen_cat[y][z])))
                    suma=suma+self.gan_gen_cat[y][z]
               texto3=texto3+"     "+str('{0:5d}'.format(int(suma)))
               print(texto3)




          # De todas las generaciones
          print('')
          print('mayor')
          print(genmayorxi)
          print(genmayorfxi)
          print('medio')
          print(genmedioxi)
          print(genmediofxi)
          print('menor')
          print(genmenorxi)
          print(genmenorfxi)

          try:

               os.mkdir("Resultados")

          except:
               print("\n La carpeta ya existe.\n")

          for y in range(self.numgeneraciones):
               fig, gnt = plt.subplots() 
               gnt.set_title("Generación {}".format(y+1))
               gnt.set_ylim(0, 60) 
          
               gnt.set_xlim(0, 3000) 
               
               gnt.set_xlabel('Costo') 
               gnt.set_ylabel('Tipos de Paquete') 
               
               gnt.set_yticks([15, 25, 35,45,55,65]) 
               gnt.set_yticklabels(['A', 'B', 'C','D','E',' ']) 
               for z in range(self.num_de_categorias):
                    gnt.broken_barh([(0, self.gan_gen_cat[y][z])],(11+z*10, 8), facecolors =('tab:blue'))
               

               plt.savefig("Resultados/A_{}".format(y+1)) 
               plt.clf()
          
          plt.plot(range(1,self.numgeneraciones+1),genmayorfxi,color="green",label="Mejor")
          plt.plot(range(1,self.numgeneraciones+1),genmediofxi,color="orange",label="Promedio")
          plt.plot(range(1,self.numgeneraciones+1),genmenorfxi,color="red",label="Peor")
          plt.suptitle('Historico Maximizacion')
          plt.legend(loc='lower right',frameon=False)
          plt.xlabel("No. de Generaciones")
          plt.ylabel("Ganancia")
          plt.savefig("Resultados/Historico_Paqueteria")

          clip = ImageSequenceClip("Resultados", fps=1.5)
          clip.write_gif('Resultados/Maximizacion_video.gif')
     
