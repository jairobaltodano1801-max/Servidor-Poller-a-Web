import os
import json

def verificar_integridad_sistema():
    """
    Modulo de control de calidad para el despliegue de la plataforma web.
    Verifica la existencia de los recursos estaticos del frontend y 
    simula la carga del diccionario de datos para los productos de la carta.
    """
    print("--- SISTEMA DE CONTROL DE CALIDAD - WEB POLERIA ---")
    
    # Rutas relativas del proyecto frontend
    archivos_requeridos = [
        "index.html",
        "css/style.css"
    ]
    
    estado_archivos = True
    print("\n[INFO] Validando rutas de archivos estaticos...")
    
    for archivo in archivos_requeridos:
        if os.path.exists(archivo):
            print(f"Recurso verificado: {archivo} [OK]")
        else:
            print(f"Error critico: No se encontro el recurso {archivo}")
            estado_archivos = False

    # Estructura de datos para simular respuesta de API local (JSON)
    print("\n[INFO] Cargando matriz de productos en memoria...")
    catalogo_combos = {
        "C001": {"denominacion": "1/4 Pollo a la Brasa + Papas + Ensalada", "precio": 24.90, "stock": True},
        "C002": {"denominacion": "1 Pollo a la Brasa Familiar", "precio": 68.90, "stock": True},
        "C003": {"denominacion": "Parrilla Personal Norkys", "precio": 45.00, "stock": False}
    }

    print("Lista de productos disponibles:")
    for codigo, datos in catalogo_combos.items():
        if datos["stock"]:
            print(f" Code: {codigo} | {datos['denominacion']} | S/. {datos['precio']:.2f}")

    print("\n--------------------------------------------------")
    if estado_archivos:
        print("RESULTADO DE AUDITORIA: Sistema listo para despliegue.")
    else:
        print("RESULTADO DE AUDITORIA: Error en la estructura de directorios.")
    print("--------------------------------------------------")

if __name__ == "__main__":
    verificar_integridad_sistema()