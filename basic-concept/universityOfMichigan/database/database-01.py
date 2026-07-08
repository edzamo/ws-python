import sqlite3
import ssl
import urllib.request

# 1. Descargar el archivo mbox.txt automáticamente si no existe localmente
url = "https://www.py4e.com/code3/mbox.txt"
data_file = "mbox.txt"
print("Descargando mbox.txt... (esto puede tardar unos segundos)")

# Some servers block the default Python user-agent or require HTTPS.
# We create a request with a browser-like user-agent and a context that accepts the certificate.
context = ssl._create_unverified_context()
request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(request, context=context) as response:
    with open(data_file, "wb") as file_handler:
        file_handler.write(response.read())

# 2. Conectar a la base de datos (creará el archivo automáticamente)
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# 3. Limpiar y estructurar la tabla según el esquema solicitado
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# 4. Procesar el archivo mbox.txt
with open(data_file, 'r') as f:
    for line in f:
        if not line.startswith('From '): 
            continue
        pieces = line.split()
        if len(pieces) < 2:
            continue
        email = pieces[1]
        
        # Extraer únicamente el dominio de la organización
        try:
            org = email.split('@')[1]
        except IndexError:
            continue

        # Verificar si la organización ya existe en la BD
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

# 5. Guardar los cambios (Commit fuera del loop para máxima velocidad)
conn.commit()

# 6. Validar el Hint del ejercicio en consola
print("\nVerificando los resultados top:")
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 2')
for row in cur.fetchall():
    print(f"Organización: {row[0]} -> Conteo: {row[1]}")

cur.close()
conn.close()
print("\n¡Proceso terminado! Sube el archivo 'emaildb.sqlite' generado.")