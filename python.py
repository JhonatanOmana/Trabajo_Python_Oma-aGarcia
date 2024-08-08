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
    nuevaVenta["direccionCliente"] = input("Dirección del cliente: ")
    nuevaVenta["nombreEmpleado"] = input("nombre del empleado: ")
    nuevaVenta["producto"] = (input("nombre del producto: "))
    nuevaVenta["cantProducto"] = int(input("cantidad del producto: "))
    nuevaVenta["preProducto"] = int(input("precio del producto: "))
   

    miInfo = abrirArchivo()
    miInfo[0]["ventas"].append(nuevaVenta)
    guardarArchivo(miInfo)
    print("venta registrada exitosamente.")


elif(opc==2): 
    nuevaCompra = {}
    nuevaCompra["fechaVenta"] = input("fecha de venta: ")
    nuevaCompra["nombreProveedor"] = input("Nombre del proveedor: ")
    nuevaCompra["contactoProveedor"] = input("Contacto del proveedor: ")
    nuevaCompra["productoComprado"] = (input("nombre del producto comprado: "))
    nuevaCompra["cantProductoComprado"] = int(input("cantidad del producto: "))
    nuevaCompra["preProductoComprado"] = int(input("precio del producto: "))
   

    miInfo = abrirArchivo()
    miInfo[1]["compras"].append(nuevaCompra)
    guardarArchivo(miInfo)
    print("Compra registrada exitosamente.")  

elif(opc==3):
     miInfo=abrirArchivo()
     for i in miInfo[0]["ventas"]:
        print("---------------------------------------")
        print("INFORMES DE VENTAS")
        print("")
        
        print("Productos vendidos:",i["producto"])
        print("Precio del producto:",i["preProducto"])


     miInfo=abrirArchivo()
     for i in miInfo[1]["compras"]:
        print("---------------------------------------")
        print("INFORMES DE VENTAS")
        print("")
        
        print("Productos vendidos:",i["productoComprado"])
        print("Cantidad de producto comprado:",i["cantProductoComprado"])
        print("Ingresos totales:",i["preProductoComprado"])    
       
        
        