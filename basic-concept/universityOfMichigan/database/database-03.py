import json
import sqlite3
import ssl
import urllib.request
from pathlib import Path

script_dir = Path(__file__).resolve().parent
json_path = script_dir / 'roster_data.json'
db_path = script_dir / 'rosterdb.sqlite'

# 1. Conectar/Crear la base de datos local
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 2. Configurar el esquema limpio de la tarea
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# 3. Leer el archivo JSON; si no existe localmente, descargarlo desde el recurso del curso
if not json_path.exists():
    url = 'https://www.py4e.com/code3/roster_data.json'
    print(f'Descargando {json_path.name}...')
    context = ssl._create_unverified_context()
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(request, context=context) as response:
        json_path.write_bytes(response.read())

str_data = json_path.read_text(encoding='utf-8')
json_data = json.loads(str_data)

# 4. Procesar e insertar los datos
for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]  # Guardar el campo 'role' requerido

    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES ( ? )''', (name, ))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES ( ? )''', (title, ))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        (user_id, course_id, role))

conn.commit()

# 5. Ejecutar la query exacta para generar tu código de envío
query = '''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X 
FROM User JOIN Member JOIN Course 
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY X LIMIT 1;
'''

cur.execute(query)
codigo_final = cur.fetchone()[0]

print("\n" + "="*40)
print(f"TU CÓDIGO PARA EL FORMULARIO ES:\n{codigo_final}")
print("="*40 + "\n")

cur.close()
conn.close()