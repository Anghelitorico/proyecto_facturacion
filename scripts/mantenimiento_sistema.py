import os
import sys
import time

CARPETA_REPORTES = "./reportes_diarios"


def limpiar_reportes_antiguos():
    print("--- INICIANDO MANTENIMIENTO AUTOMATIZADO ---")

    # Verificar que exista la carpeta de reportes.
    if not os.path.exists(CARPETA_REPORTES):
        print("[ERROR CRÍTICO]: No existe la carpeta 'reportes_diarios'.")
        print("Por favor, créala y coloca un archivo dentro antes de ejecutar el script.")
        sys.exit(1)

    tiempo_actual = time.time()
    archivos_eliminados = 0

    # Escanear la carpeta de reportes.
    for archivo in os.listdir(CARPETA_REPORTES):
        ruta_completa = os.path.join(CARPETA_REPORTES, archivo)

        if os.path.isfile(ruta_completa) and archivo.endswith(".csv"):
            fecha_modificacion = os.path.getmtime(ruta_completa)

            # Eliminar archivos CSV con más de 5 segundos de antigüedad.
            if tiempo_actual - fecha_modificacion > 5:
                os.remove(ruta_completa)
                print(f"[CONSOLA] Archivo obsoleto eliminado: {archivo}")
                archivos_eliminados += 1

    print(
        f"--- MANTENIMIENTO FINALIZADO. "
        f"Se eliminaron {archivos_eliminados} archivos. ---"
    )
    sys.exit(0)


if __name__ == "__main__":
    limpiar_reportes_antiguos()

