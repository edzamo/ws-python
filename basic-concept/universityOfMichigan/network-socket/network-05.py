import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignorar errores de certificado SSL si los hay
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)

# Leer los datos del XML remoto
html = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(html), 'characters')

# Parsear el árbol XML
tree = ET.fromstring(html)

# Buscar todos los elementos 'count' usando XPath
counts = tree.findall('.//count')

total_sum = 0
counter = 0

for item in counts:
    total_sum += int(item.text)
    counter += 1

print('Count:', counter)
print('Sum:', total_sum)