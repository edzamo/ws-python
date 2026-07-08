import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Endpoint proporcionado por las instrucciones del ejercicio
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# Ignorar errores de certificado SSL si aplica
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

# Definir los parámetros requeridos
params = dict()
params['q'] = address
params['key'] = 42

# Generar la URL final con los parámetros codificados
url = serviceurl + urllib.parse.urlencode(params)
print('Retrieving', url)

# Realizar la petición HTTP
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

# Extraer el plus_code del primer elemento de los resultados
if js and 'features' in js and len(js['features']) > 0:
    plus_code = js['features'][0]['properties'].get('plus_code', None)
    print('Plus code', plus_code)
else:
    print('==== Failure To Retrieve ====')