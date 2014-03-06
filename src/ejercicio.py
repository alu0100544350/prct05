#!/usr/bin/python
#!encoding: UTF-8
import sys

argumentos=sys.argv[1:]
if(len(argumentos)==1):
    n=int(argumentos[0])
else:       
    print"Introduzca el nº de intervalos (n>0) : "
    n=int(raw_input())
if(n>0):
  PI35= 3.1415926535897931159979634685441852
  iniciointervalo=0
  suma=0
  intervalos=1.0/float(n)
  for i in range(n):
     x_i=((i+1)-1.0/2.0)/n
     fx_i=4.0/(1.0 + x_i*x_i)
     print "Subintervalo :[", iniciointervalo, ",", iniciointervalo+intervalos, "] x_i:", x_i, "fx_i:", fx_i
     iniciointervalo+=intervalos
     suma+=fx_i
  aproximacion_pi=suma/n
  print "El valor aproximado de pi es: ", aproximacion_pi
  print "El valor de Pi con 35 decimales es : %10.35f" % PI35
  
else:
  print" El vaor de los intervalos tiene que ser positivo"
  
  