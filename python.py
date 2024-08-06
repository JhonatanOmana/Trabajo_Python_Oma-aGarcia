import json

def abrirArchivo():
    miJSON=[]
    with open('info.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("info.json","w") as outfile:
        json.dump(miData,outfile)



print("     ______________________ ")
print("    | BIENVENIDO A PanCamp |")
print("    |______________________|")

print("\n1.Ventas\n2.Compras\n3.Informes")
opc=int(input("Elige una opción: "))
miInfo=[]

if(opc==1):
    nuevaVenta = {}
    nuevaVenta["fechaVenta"] = input("fecha de venta: ")
    nuevaVenta["nombreCliente"] = input("Nombre del cliente: ")
    nuevaVenta["nombreEmpleado"] = input("nombre del nuevo empleado: ")
    nuevaVenta["producto"] = (input("nombre del producto: "))
   

    miInfo = abrirArchivo()
    miInfo[0]["ventas"].append(nuevaVenta)
    guardarArchivo(miInfo)
    print("venta registrada exitosamente.")

elif(opc==2):
     miInfo=abrirArchivo()
     for i in miInfo[0]["ventas"]:
        print("################")
        print("DETALLES DE VENTA")
        print("")
        print("Fecha de venta:",i["fechaVenta"])
        print("Nombre del cliente:",i["nombreCliente"])
        print("Nombre empleado:",i["nombreEmpleado"])
        print("Producto vendido:",i["producto"])
        
        