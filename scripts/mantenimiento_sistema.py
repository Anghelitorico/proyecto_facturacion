import os
import sys
import time

CARPETA_REPORTES = "./reportes_diarios"


def limpiar_reportes_antiguos():
    print("--- INICIANDO MANTENIMIENTO AUTOMATIZADO ---")

    if not os.path.isdir(CARPETA_REPORTES):
        print("[ERROR CRÍTICO]: No existe la carpeta 'reportes_diarios'.")
        print("Por favor, crea la carpeta antes de ejecutar este script.")
        sys.exit(1)

    tiempo_actual = time.time()
    archivos_eliminados = 0

    for archivo in os.listdir(CARPETA_REPORTES):
        ruta_completa = os.path.join(CARPETA_REPORTES, archivo)

        if not os.path.isfile(ruta_completa) or not archivo.endswith(".csv"):
            continue

        fecha_modificacion = os.path.getmtime(ruta_completa)

        if tiempo_actual - fecha_modificacion > 5:
            os.remove(ruta_completa)
            print(f"[CONSOLA] Archivo obsoleto eliminado: {archivo}")
            archivos_eliminados += 1

    print(
        "--- MANTENIMIENTO FINALIZADO. "
        f"Se eliminaron {archivos_eliminados} archivos. ---"
    )


if __name__ == "__main__":
    limpiar_reportes_antiguos()
