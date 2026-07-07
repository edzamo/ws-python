import os
import io
import sys
import subprocess
import zipfile
import urllib.request
import ssl
from pathlib import Path

script_dir = Path(__file__).resolve().parent
project_dir = script_dir / "opengeo"
os.chdir(script_dir)

# 1. Descargar y extraer el proyecto
url = "https://www.py4e.com/code3/opengeo.zip"
print("Descargando opengeo.zip...")
context = ssl._create_unverified_context()
request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(request, context=context) as response:
    with zipfile.ZipFile(io.BytesIO(response.read())) as z:
        z.extractall(script_dir)

# 2. Modificar 'where.data' con una ubicación cultural/pública representativa
# (Sin revelar tu ubicación exacta residencial)
added_location = "Plaza Civica, Manta, Ecuador"
print(f"Modificando where.data añadiendo: {added_location}")

where_data_path = project_dir / "where.data"
with open(where_data_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Escribir la nueva ubicación al inicio
with open(where_data_path, "w", encoding="utf-8") as f:
    f.write(added_location + "\n")
    f.writelines(lines)

print("\n--- EJECUTANDO GEOLOAD.PY ---")
print("Espera a que procese la nueva ubicación y guarde en la BD...")
subprocess.run([sys.executable, str(project_dir / "geoload.py")], cwd=project_dir, check=True)

print("\n--- EJECUTANDO GEODUMP.PY ---")
print("Generando el archivo de visualización where.js...")
subprocess.run([sys.executable, str(project_dir / "geodump.py")], cwd=project_dir, check=True)

print("\n¡Proceso completado con éxito! Ahora sigue los pasos para las capturas.")