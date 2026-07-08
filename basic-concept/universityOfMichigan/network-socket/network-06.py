import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignorar errores de certificado SSL si es necesario
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)

# Leer los datos crudos del JSON remoto
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')

# Parsear los datos de texto a un diccionario/objeto de Python
info = json.loads(data)

total_sum = 0
counter = 0

# Iterar sobre la lista de elementos bajo la propiedad "comments"
for item in info['comments']:
    total_sum += int(item['count'])
    counter += 1

print('Count:', counter)
print('Sum:', total_sum)