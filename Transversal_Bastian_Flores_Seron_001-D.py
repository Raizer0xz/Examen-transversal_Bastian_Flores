productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
        '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
        'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
        'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
        'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
        '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
        '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
        'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def menu_principal():
    print("\n----MENU DE INICIO----")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

def mostrar_producto():
    if productos:
        print("Productos disponibles: ")
        for modelo, datos in productos.items():
            print(f"{modelo} - Marca: {datos[0]}")
    else:
        print("No hay productos registrados")

def mostrar_stock():
    if stock:
        print("Los modelos en stock son: ")
        for modelo, datos in stock.items():
            marca = productos[modelo][0] if modelo in productos else 'Desconocida'
            print(f"{modelo} - Marca: {marca}, Precio: {datos[0]}, Stock: {datos[1]}")
    else:
        print("No hay productos registrados")

def validar_clave(modelo):
    if len(modelo) < 6:
        print("La clave debe tener al menos 6 caracteres")
        return False
    mayusculas = sum(1 for c in modelo if c.isupper())
    numeros = sum(1 for c in modelo if c.isdigit())
    print(f"mayusculas: {mayusculas} - numeros: {numeros}.")
    if mayusculas > 6:
        print("Debe llevar menos de 6 mayusculas.")
        return False
    if numeros > 6:
        print("Debe llevar menos de 6 numeros.")
        return False
    return True

def stock_marca():
    mostrar_producto()
    while True:
        modelo = input("Ingresa la clave del modelo correspondiente: ").strip()
        if validar_clave(modelo):
            break
    if modelo in productos:
        if modelo in stock:
            print(f"Modelo: {modelo}, Marca: {productos[modelo][0]}, Stock: {stock[modelo][1]}")
        else:
            print("No hay stock para este modelo.")
    else:
        print("Modelo no encontrado.")

def buscar_precio():
    try:
        precio_buscar = int(input("Ingrese el precio a buscar: "))
    except ValueError:
        print("Debes ingresar solo valores enteros.")
        return
    encontrados = []
    for modelo, datos in stock.items():
        if datos[0] == precio_buscar:
            marca = productos[modelo][0] if modelo in productos else 'Desconocida'
            encontrados.append((modelo, marca, datos[0], datos[1]))
    if encontrados:
        print("Modelos encontrados con ese precio:")
        for modelo, marca, precio, cantidad in encontrados:
            print(f"{modelo} - Marca: {marca}, Precio: {precio}, Stock: {cantidad}")
    else:
        print("No se encontró ningún modelo con ese precio.")

def actualizar_precio():
    mostrar_producto()
    while True:
        modelo = input("Ingresa el modelo que deseas actualizar: ").strip()
        if validar_clave(modelo):
            break
    if modelo in stock:
        while True:
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                break
            except ValueError:
                print("Debes de ingresar solo valores enteros.")
        stock[modelo][0] = nuevo_precio
        print(f"Precio actualizado para {modelo}. Nuevo precio: {nuevo_precio}")
    else:
        print("Modelo no encontrado en stock.")

def stock_marca(marca):
    marca = marca.strip().lower()
    encontrados = []
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            stock_disp = stock[modelo][1] if modelo in stock else 0
            encontrados.append((modelo, stock_disp))
    if encontrados:
        print(f"Stock para la marca '{marca}':")
        for modelo, cantidad in encontrados:
            print(f"Modelo: {modelo}, Stock: {cantidad}")
    else:
        print(f"No se encontraron modelos para la marca '{marca}'.")

def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo, datos in stock.items():
        precio, cantidad = datos
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0] if modelo in productos else 'Desconocida'
            resultados.append(f"{marca}--{modelo}")
    if resultados:
        resultados.sort()
        print("Modelos encontrados en el rango de precios:")
        for item in resultados:
            print(item)
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False

def main():
    while True:
        menu_principal()
        opcion = input("Ingresa una de las opciones: ").strip()
        if opcion == "1":
            marca = input("Ingrese la marca a consultar: ")
            stock_marca(marca)
        elif opcion == "2":
            while True:
                try:
                    p_min = int(input("Ingrese el precio mínimo: "))
                    p_max = int(input("Ingrese el precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            busqueda_precio(p_min, p_max)
        elif opcion == "3":
            while True:
                modelo = input("Ingrese el modelo a actualizar: ").strip()
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                except ValueError:
                    print("Debe ingresar valores enteros!!")
                    continue
                resultado = actualizar_precio(modelo, nuevo_precio)
                if resultado:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")
                otra = input("¿Desea actualizar otro precio de notebook? (si/no): ").strip().lower()
                if otra != "si":
                    break
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción válida!!")

main()
