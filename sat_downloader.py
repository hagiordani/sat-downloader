import requests
import os

SAT_CSV_URLS = [
    "http://omawww.sat.gob.mx/cifras_sat/Documents/Listado_Completo_69-B.csv",
    "http://omawww.sat.gob.mx/cifras_sat/Documents/Definitivos.csv",
    "http://omawww.sat.gob.mx/cifras_sat/Documents/Desvirtuados.csv",
    "http://omawww.sat.gob.mx/cifras_sat/Documents/SentenciasFavorables.csv",
    "http://omawww.sat.gob.mx/cifras_sat/Documents/Presuntos.csv",
    "http://omawww.sat.gob.mx/cifras_sat/Documents/ListadoGlobalDefinitivo.csv"
]

DOWNLOAD_DIR = "/app/downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

print(f"Descargando archivos del SAT en: {DOWNLOAD_DIR}")

for url in SAT_CSV_URLS:
    try:
        file_name = url.split('/')[-1]
        file_path = os.path.join(DOWNLOAD_DIR, file_name)

        print(f"-> Descargando {file_name}...")

        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(file_path, "wb") as f:
            for chunk in response.iter_content(8192):
                f.write(chunk)

        print(f"   ✔ Guardado: {file_path}")

    except Exception as e:
        print(f"   ✖ Error: {e}")

print("\nProceso completado.")
