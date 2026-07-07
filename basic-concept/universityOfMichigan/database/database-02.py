import sqlite3
import ssl
import urllib.request
import zipfile
import io
import csv
import os

# 1. Descargar y extraer el archivo tracks.csv oficial del curso
url = "https://www.py4e.com/code3/tracks.zip"
print("Descargando e inicializando los datos de iTunes (tracks.csv)...")

context = ssl._create_unverified_context()
request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(request, context=context) as response:
    with zipfile.ZipFile(io.BytesIO(response.read())) as z:
        z.extractall()

# The zip may contain the CSV in the current folder or in a subfolder.
# We search for the file in the current directory and its children.
possible_files = ["tracks.csv", os.path.join("database", "tracks.csv")]
for root, _, files in os.walk('.'):
    for name in files:
        if name == 'tracks.csv':
            possible_files.append(os.path.join(root, name))

csv_path = None
for candidate in possible_files:
    if os.path.exists(candidate):
        csv_path = candidate
        break

if csv_path is None:
    raise FileNotFoundError("No se encontró tracks.csv después de extraer el ZIP")

# 2. Conectar a SQLite y estructurar las tablas según el esquema exacto solicitado
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# 3. Leer y parsear el archivo CSV
with open(csv_path) as csvfile:
    # Saltar el encabezado si existe o parsear de forma limpia
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) < 7: continue
        
        # El formato esperado del CSV es: Title, Artist, Album, Count, Rating, Length, Genre
        # (Nos saltamos la línea de encabezado típica comparando el tipo de dato)
        if row[0] == 'Name': continue
        
        title = row[0]
        artist = row[1]
        album = row[2]
        count = row[3]
        rating = row[4]
        length = row[5]
        genre = row[6]

        # Insertar Artista (ignorando si ya existe por el constraint UNIQUE)
        cur.execute('''INSERT OR IGNORE INTO Artist (name) 
            VALUES ( ? )''', ( artist, ) )
        cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
        artist_id = cur.fetchone()[0]

        # Insertar Género (ignorando duplicados)
        cur.execute('''INSERT OR IGNORE INTO Genre (name) 
            VALUES ( ? )''', ( genre, ) )
        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
        genre_id_row = cur.fetchone()
        genre_id = genre_id_row[0] if genre_id_row else None

        # Insertar Álbum vinculando el artist_id correspondiente
        cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
            VALUES ( ?, ? )''', ( album, artist_id ) )
        cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
        album_id = cur.fetchone()[0]

        # Insertar la pista musical con sus respectivas relaciones mapeadas
        cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, genre_id, len, rating, count) 
            VALUES ( ?, ?, ?, ?, ?, ? )''', 
            ( title, album_id, genre_id, length, rating, count ) )

# 4. Guardar cambios en el almacenamiento físico
conn.commit()

# 5. Validación rápida en consola emulando la consulta del validador de la tarea
print("\n[Validación] Verificando las primeras líneas según la consulta esperada:")
query = '''
SELECT Track.title, Artist.name, Album.title, Genre.name
FROM Track JOIN Genre JOIN Album JOIN Artist 
ON Track.genre_id = Genre.id AND Track.album_id = Album.id 
AND Album.artist_id = Artist.id
ORDER BY Artist.name LIMIT 3
'''
cur.execute(query)
for res in cur.fetchall():
    print(f"Track: {res[0]} | Artist: {res[1]} | Album: {res[2]} | Genre: {res[3]}")

cur.close()
conn.close()
print("\n¡Todo listo! Sube el archivo 'trackdb.sqlite' que se ha generado en tu carpeta.")