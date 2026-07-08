import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

print('Retrieving:', url)

# Repetir el proceso el número de veces indicado en "count"
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    
    # Obtener el enlace en la posición indicada (restando 1 para el índice de Python)
    url = tags[position - 1].get('href', None)
    print('Retrieving:', url)

# Al finalizar, extraemos el nombre desde la última URL limpia o el texto del tag
# Las URLs tienen el formato ".../known_by_Nombre.html"
last_name = url.split('_')[-1].split('.')[0]
print('\nLast name in sequence:', last_name)