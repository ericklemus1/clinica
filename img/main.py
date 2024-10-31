import time

# Datos de la tienda
logo = "Farmacia Los Almendros"
menu_opciones = ["Inicio", "Cuenta", "Categorías", "Carrito"]
subcategorias = ["Medicamentos", "Farmacia", "Alimentos"]

# Funcionalidad de "buscar"
def buscar_producto():
    query = input("\nIngrese el producto que desea buscar: ")
    print(f"Buscando '{query}' en la tienda...\n")
    # Simulación de búsqueda (reemplazable por lógica real)
    time.sleep(1)
    print(f"Resultados de búsqueda para '{query}':\n1. {query} - Producto de ejemplo")

# Función para mostrar el menú principal
def mostrar_menu():
    print(f"\n{logo}")
    print("=" * len(logo))
    print("Menú principal:")
    for i, opcion in enumerate(menu_opciones, 1):
        print(f"{i}. {opcion}")
    print("\n5. Salir")

# Función para mostrar categorías
def mostrar_categorias():
    print("\nCategorías:")
    for i, cat in enumerate(subcategorias, 1):
        print(f"{i}. {cat}")

# Simulación de carrusel de anuncios
def mostrar_carrusel():
    anuncios = ["Anuncio 1: Descuento en medicamentos", 
                "Anuncio 2: Oferta en productos de farmacia", 
                "Anuncio 3: Promoción en alimentos saludables"]
    for anuncio in anuncios:
        print(f"\n{anuncio}")
        time.sleep(3)

# Menú interactivo principal
def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\nBienvenido a la tienda virtual de la Farmacia Los Almendros.\n")
            mostrar_carrusel()
        elif opcion == "2":
            print("\nAccediendo a su cuenta...\n")
            time.sleep(1)  # Simulación de carga
            print("Cuenta de usuario no disponible en esta versión de consola.")
        elif opcion == "3":
            mostrar_categorias()
        elif opcion == "4":
            buscar_producto()
        elif opcion == "5":
            print("\nGracias por visitar la farmacia. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida, por favor seleccione una opción del menú.")

if __name__ == "__main__":
    main()
