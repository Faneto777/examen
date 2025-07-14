productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def stock_marca(marca):
    total = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            total += stock.get(modelo, [0, 0])[1]
            print(f"El stock es de {total}")

def busqueda_precio(p_min,p_max):
    resultados = []
    for modelo, (precio, _) in stock.items():
        if p_min <= precio <= p_max:
            marca = productos[modelo][0]
            resultados.append(f"{marca} - {modelo}")
            if resultados:
                print("Notebooks en rango de precio: ")
                for r in resultados:
                    print(r)
                else:
                    print("No hay notebooks en ese rango de precio.")


def actualizar_precio(modelo, p):
    if modelo not in stock:
        print("El modelo no existe.")
        return False
    confirmacion = input("¿Desea actualizar el precio? (s/n): ").lower()
    if confirmacion == "s":
        stock[modelo][0] = p
        print("Actualizacion exitosa.")
        return True
    else:
        print("Cancelado")
        return False

def main_menu():
    while True:
        print("[1] - Stock marca.")
        print("[2] - Busqueda por precio.")
        print("[3] - Actualizar precio.")
        print("[4] - Salir.")

        opcion = input("Ingrese una opcion: ")
    

        if opcion == "1":
            marca = input("Ingrese la marca: ")
            stock_marca(marca)
        
        elif opcion == "2":
            try:
                p_min = int(input("Ingrese precio minimo de la compra: "))
                p_max = int(input("Ingrese precio maximo de la compra: "))
                busqueda_precio(p_min, p_max)
            except ValueError:
                print("Solo debe ingresar valores numericos.")
                break

        elif opcion == "3":
            modelo = input("Ingresar el modelo que quiera actualizar: ")
            try:
                p = int(input("Ingrese el nuevo precio: "))
                p_nuevo = actualizar_precio(modelo, p)
                if not p_nuevo:
                    continue
            except ValueError:
                print("El precio debe ser un numero.")

        elif opcion == "4":
            print("Programa finalizado.")
            break
        
        else:
            print("Debe seleccionar una opcion valida!!")
            continue

main_menu()