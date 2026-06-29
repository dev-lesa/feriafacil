# ============================================================
# FERIAFÁCIL - Sistema de Gestión para Mercado Local
# ============================================================
# Impacto tecnológico:
# Los vendedores de ferias y mercados locales del Ecuador
# administran sus negocios con cuadernos y cálculos manuales.
# Este sistema digitaliza ese proceso, reduciendo errores
# y ahorrando tiempo al vendedor cada día.
# ============================================================

# Importamos la librería matemática para posibles cálculos
import math

# ============================================================
# DATOS INICIALES DEL SISTEMA
# ============================================================

# Diccionario principal: cada producto tiene precio, stock y categoría
# Estructura: nombre_producto -> {"precio": float, "stock": int, "categoria": str}
inventario = {
    "manzana":   {"precio": 0.50, "stock": 100, "categoria": "frutas"},
    "tomate":    {"precio": 0.30, "stock": 80,  "categoria": "verduras"},
    "papa":      {"precio": 0.25, "stock": 120, "categoria": "tuberculos"},
    "platano":   {"precio": 0.15, "stock": 60,  "categoria": "frutas"},
    "zanahoria": {"precio": 0.20, "stock": 90,  "categoria": "verduras"},
    "cebolla":   {"precio": 0.35, "stock": 70,  "categoria": "verduras"},
    "naranja":   {"precio": 0.40, "stock": 50,  "categoria": "frutas"},
    "lechuga":   {"precio": 0.45, "stock": 35,  "categoria": "verduras"},
}

# Lista que registra cada transacción del día
# Cada elemento es un diccionario con los datos de la venta
ventas_del_dia = []

# Tupla con las categorías válidas del sistema
# Se usa tupla porque estas categorías NO deben cambiar en ejecución
CATEGORIAS_VALIDAS = ("frutas", "verduras", "tuberculos", "otros")

# Stock mínimo antes de mostrar una alerta de reabastecimiento
LIMITE_MINIMO = 25

# Variable acumuladora del dinero recaudado en el día
total_recaudado = 0.0


# ============================================================
# FUNCIÓN: Mostrar el menú principal
# ============================================================
def mostrar_menu():
    """
    Imprime en pantalla el menú de opciones disponibles.
    No recibe parámetros ni retorna valores.
    """
    print("\n" + "=" * 50)
    print("       FERIAFÁCIL - MENÚ PRINCIPAL")
    print("  Sistema de Gestión para Mercado Local")
    print("=" * 50)
    print("  1. Ver inventario completo")
    print("  2. Registrar una venta")
    print("  3. Agregar producto nuevo")
    print("  4. Buscar un producto")
    print("  5. Ver alertas de stock bajo")
    print("  6. Ver resumen del día")
    print("  7. Ver categorías activas")
    print("  0. Salir del sistema")
    print("=" * 50)


# ============================================================
# FUNCIÓN: Mostrar el inventario completo
# ============================================================
def mostrar_inventario():
    """
    Recorre el diccionario de inventario con un bucle for
    y muestra cada producto con su precio, stock y categoría.
    """
    print("\n--- INVENTARIO ACTUAL ---")

    # Verificar si el inventario está vacío
    if len(inventario) == 0:
        print("No hay productos registrados.")
        return

    # Recorremos el diccionario usando .items() para obtener clave y valor
    for nombre, datos in inventario.items():
        precio    = datos["precio"]
        stock     = datos["stock"]
        categoria = datos["categoria"]

        # Condicional: mostrar alerta si el stock está bajo el límite
        alerta = ""
        if stock <= LIMITE_MINIMO:
            alerta = "  << STOCK BAJO"

        print(f"  {nombre}: ${precio:.2f} | stock: {stock} und | {categoria}{alerta}")

    print(f"\nTotal de productos registrados: {len(inventario)}")


# ============================================================
# FUNCIÓN: Registrar una venta
# ============================================================
def registrar_venta():
    """
    Solicita al vendedor el nombre del producto y la cantidad.
    Valida que el producto exista y que haya stock suficiente.
    Descuenta del inventario, registra la venta y actualiza
    el total recaudado del día.
    """
    # Usamos global para modificar la variable total_recaudado
    global total_recaudado

    print("\n--- REGISTRAR VENTA ---")
    mostrar_inventario()

    # Input: pedimos el nombre del producto (todo en minúsculas)
    producto = input("\nNombre del producto a vender: ").lower().strip()

    # Condicional: verificar si el producto existe en el inventario
    if producto not in inventario:
        print(f"Error: El producto '{producto}' no existe en el inventario.")
        return

    # Obtenemos los datos del producto del diccionario
    precio_unit  = inventario[producto]["precio"]
    stock_actual = inventario[producto]["stock"]

    print(f"\nProducto encontrado: {producto}")
    print(f"Precio unitario: ${precio_unit:.2f}")
    print(f"Stock disponible: {stock_actual} unidades")

    # Input: pedimos la cantidad y la convertimos a entero (casteo)
    cantidad = int(input("Cantidad de unidades a vender: "))

    # Condicional: validar que la cantidad sea positiva
    if cantidad <= 0:
        print("Error: La cantidad debe ser mayor a cero.")
        return

    # Condicional: validar que haya suficiente stock
    if cantidad > stock_actual:
        print(f"Error: Stock insuficiente. Solo hay {stock_actual} unidades disponibles.")
        return

    # Proceso: calcular el subtotal de esta venta
    subtotal = precio_unit * cantidad

    # Actualizar el stock en el diccionario
    inventario[producto]["stock"] = stock_actual - cantidad

    # Crear el registro de la venta como diccionario
    nueva_venta = {
        "producto": producto,
        "cantidad": cantidad,
        "precio":   precio_unit,
        "subtotal": subtotal
    }

    # Agregar la venta a la lista de ventas usando .append()
    ventas_del_dia.append(nueva_venta)

    # Sumar el subtotal al total acumulado del día
    total_recaudado = total_recaudado + subtotal

    # Output: mostrar confirmación al vendedor
    print("\nVENTA REGISTRADA CORRECTAMENTE")
    print(f"  Producto:  {producto}")
    print(f"  Cantidad:  {cantidad} unidades")
    print(f"  Subtotal:  ${subtotal:.2f}")
    print(f"  Total del día hasta ahora: ${total_recaudado:.2f}")

    # Condicional: verificar si quedó poco stock después de la venta
    stock_nuevo = inventario[producto]["stock"]
    if stock_nuevo <= LIMITE_MINIMO:
        print(f"\n  AVISO: '{producto}' tiene stock bajo ({stock_nuevo} unidades).")
        print("  Se recomienda reabastecer pronto.")


# ============================================================
# FUNCIÓN: Agregar un producto nuevo
# ============================================================
def agregar_producto():
    """
    Solicita los datos de un nuevo producto: nombre, precio,
    stock inicial y categoría. Valida cada dato antes de
    agregarlo al diccionario de inventario.
    """
    print("\n--- AGREGAR PRODUCTO NUEVO ---")

    # Input: nombre del producto
    nombre = input("Nombre del nuevo producto: ").lower().strip()

    # Condicional: validar que el nombre no esté vacío
    if nombre == "":
        print("Error: El nombre del producto no puede estar vacío.")
        return

    # Condicional: verificar que el producto no exista ya
    if nombre in inventario:
        print(f"Error: El producto '{nombre}' ya existe en el inventario.")
        return

    # Input: precio con casteo a flotante
    precio = float(input("Precio unitario en dólares ($): "))

    # Condicional: validar que el precio sea positivo
    if precio <= 0:
        print("Error: El precio debe ser mayor a cero.")
        return

    # Input: stock inicial con casteo a entero
    stock = int(input("Cantidad inicial en stock: "))

    # Condicional: validar que el stock no sea negativo
    if stock < 0:
        print("Error: El stock inicial no puede ser negativo.")
        return

    # Mostrar categorías válidas usando la tupla CATEGORIAS_VALIDAS
    print(f"Categorías válidas: {CATEGORIAS_VALIDAS}")
    categoria = input("Categoría del producto: ").lower().strip()

    # Condicional: si la categoría no es válida, usar "otros"
    if categoria not in CATEGORIAS_VALIDAS:
        print("Categoría no reconocida. Se asignará automáticamente 'otros'.")
        categoria = "otros"

    # Agregar el nuevo producto al diccionario
    inventario[nombre] = {
        "precio":    precio,
        "stock":     stock,
        "categoria": categoria
    }

    # Output: confirmación del producto agregado
    print(f"\nProducto '{nombre}' agregado exitosamente:")
    print(f"  Precio:    ${precio:.2f}")
    print(f"  Stock:     {stock} unidades")
    print(f"  Categoría: {categoria}")


# ============================================================
# FUNCIÓN: Buscar un producto específico
# ============================================================
def buscar_producto():
    """
    Busca un producto por nombre en el diccionario de inventario
    y muestra toda su información si existe. Si no existe,
    notifica al vendedor.
    """
    print("\n--- BUSCAR PRODUCTO ---")

    # Input: nombre del producto a buscar
    nombre = input("Nombre del producto a buscar: ").lower().strip()

    # Condicional: verificar si el producto está en el inventario
    if nombre in inventario:
        datos = inventario[nombre]

        print(f"\nProducto encontrado: {nombre}")
        print(f"  Precio:    ${datos['precio']:.2f}")
        print(f"  Stock:     {datos['stock']} unidades")
        print(f"  Categoría: {datos['categoria']}")

        # Sub-condicional: advertir si el stock está bajo
        if datos["stock"] <= LIMITE_MINIMO:
            print("  AVISO: Stock bajo. Se recomienda reabastecer.")
        else:
            print("  Estado: Stock suficiente.")

    else:
        print(f"\nEl producto '{nombre}' no se encontró en el inventario.")
        print("Revisa el inventario completo con la opción 1.")


# ============================================================
# FUNCIÓN: Mostrar alertas de stock bajo
# ============================================================
def mostrar_alertas():
    """
    Recorre el inventario y muestra solamente los productos
    cuyo stock sea menor o igual al límite mínimo configurado.
    Ayuda al vendedor a saber qué necesita reabastecer.
    """
    print("\n--- ALERTAS DE STOCK BAJO ---")
    print(f"Límite mínimo configurado: {LIMITE_MINIMO} unidades\n")

    # Variable booleana: nos dice si hay alguna alerta
    hay_alertas = False

    # Recorremos el inventario con un bucle for
    for nombre, datos in inventario.items():
        if datos["stock"] <= LIMITE_MINIMO:
            print(f"  ALERTA: '{nombre}' - solo {datos['stock']} unidades restantes")
            hay_alertas = True

    # Condicional: mensaje cuando no hay alertas
    if not hay_alertas:
        print("Todos los productos tienen stock suficiente. Sin alertas.")


# ============================================================
# FUNCIÓN: Ver el resumen del día
# ============================================================
def resumen_del_dia():
    """
    Muestra la lista completa de ventas realizadas durante
    el día y el total de dinero recaudado.
    Recorre la lista ventas_del_dia con un bucle for.
    """
    print("\n--- RESUMEN DEL DÍA ---")

    # Condicional: verificar si hubo ventas
    if len(ventas_del_dia) == 0:
        print("No se han registrado ventas durante el día.")
        return

    print(f"Número de transacciones realizadas: {len(ventas_del_dia)}\n")

    # Variable contador para numerar las ventas
    numero = 1

    # Recorremos la lista de ventas con un bucle for
    for venta in ventas_del_dia:
        print(f"  {numero}. {venta['producto']} "
              f"x {venta['cantidad']} unidades "
              f"@ ${venta['precio']:.2f} "
              f"= ${venta['subtotal']:.2f}")
        numero = numero + 1

    # Output: total recaudado del día
    print(f"\n  TOTAL RECAUDADO HOY: ${total_recaudado:.2f}")

    # Calcular el promedio de venta usando math
    promedio = total_recaudado / len(ventas_del_dia)
    print(f"  Promedio por transacción: ${promedio:.2f}")


# ============================================================
# FUNCIÓN: Ver categorías activas
# ============================================================
def ver_categorias():
    """
    Usa un conjunto (set) para identificar las categorías
    únicas que actualmente están en uso en el inventario.
    El set automáticamente elimina los duplicados.
    """
    print("\n--- CATEGORÍAS ACTIVAS EN EL INVENTARIO ---")

    # Creamos un set vacío para almacenar categorías únicas
    categorias_activas = set()

    # Recorremos el inventario y usamos .add() para agregar al set
    for nombre, datos in inventario.items():
        categorias_activas.add(datos["categoria"])

    print(f"Total de categorías encontradas: {len(categorias_activas)}\n")

    # Para cada categoría activa, contamos cuántos productos tiene
    for categoria in categorias_activas:
        conteo = 0

        # Bucle interno para contar productos de esa categoría
        for nombre, datos in inventario.items():
            if datos["categoria"] == categoria:
                conteo = conteo + 1

        print(f"  {categoria}: {conteo} producto(s)")

    # Mostrar también las categorías disponibles (tupla)
    print(f"\nCategorías disponibles en el sistema: {CATEGORIAS_VALIDAS}")


# ============================================================
# PROGRAMA PRINCIPAL - PUNTO DE ENTRADA DEL SISTEMA
# ============================================================

# Mensaje de bienvenida al iniciar el sistema
print("=" * 50)
print("  Bienvenido a FERIAFÁCIL")
print("  Sistema de Gestión para Mercado Local")
print("  Tecnología al servicio del vendedor")
print("=" * 50)
print("\nEste sistema te ayuda a gestionar tu negocio")
print("de manera digital: inventario, ventas y resumen.")

# Variable de control del bucle principal (booleano)
sistema_activo = True

# Bucle principal: se mantiene activo hasta que el usuario elija salir
while sistema_activo:

    # Mostramos el menú y pedimos la opción al usuario
    mostrar_menu()
    opcion = input("\nElige una opción (0-7): ").strip()

    # Estructura condicional: ejecutar la función correspondiente
    if opcion == "1":
        mostrar_inventario()

    elif opcion == "2":
        registrar_venta()

    elif opcion == "3":
        agregar_producto()

    elif opcion == "4":
        buscar_producto()

    elif opcion == "5":
        mostrar_alertas()

    elif opcion == "6":
        resumen_del_dia()

    elif opcion == "7":
        ver_categorias()

    elif opcion == "0":
        # Al salir: mostrar resumen final antes de cerrar
        print("\n" + "=" * 50)
        print("  CERRANDO SISTEMA - RESUMEN FINAL DEL DÍA")
        print("=" * 50)
        resumen_del_dia()
        print("\nGracias por usar FeriaFácil.")
        print("Que tenga excelentes ventas. ¡Hasta pronto!")
        sistema_activo = False

    else:
        print("\nOpción no válida. Por favor ingresa un número del 0 al 7.")
