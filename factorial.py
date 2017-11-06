'''
Created on Nov 4, 2017

@author: vagrant
'''
def mostrarProducto (matriz):
    for a in range(0,len(matriz[0])):
        print(str(a)+ " - "+matriz[0][a]+" - $"+str(matriz[1][a]))
    
def mostrarTicket (matriz):
    for a in range(0,len(matriz[0])):
        print(str(a), " - ",matriz[0][a]," - $",(matriz[1][a]))
    
producto = [["pan","yerba","azucar","leche"],[23,100,200,40]]

mostrarProducto(producto)

ticket = [[],[],[]]
 
termina = "no"
 
while termina == "no":
    mostrarProducto(producto)
    codigo = input("ingresar codigo de articulo")
    cantidad = input("ingresa cantidad de articulo")
    ticket[0].append(int(cantidad))
    ticket[1].append(producto[0][int(codigo)])
    ticket[2].append(int(cantidad)*producto[1][int(codigo)])
    termina = input("termina? si|no")
mostrarTicket(ticket)  
    