import sqlite3
import json
import codecs

conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')

fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")

geojson = {
    "type": "FeatureCollection",
    "features": []
}

count = 0
for row in cur :
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue

    if len(js['features']) == 0: continue

    try:
        lat = js['features'][0]['geometry']['coordinates'][1]
        lng = js['features'][0]['geometry']['coordinates'][0]
        where = js['features'][0]['properties']['display_name']
        where = where.replace("'", "")
    except:
        print('Unexpected format')
        print(js)

    try :
        print(where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)

        geojson["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lng, lat]
            },
            "properties": {
                "name": where
            }
        })
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()

with open('where.geojson', 'w', encoding='utf-8') as geo_f:
    json.dump(geojson, geo_f, indent=2)

print(count, "records written to where.js")
print("GeoJSON written to where.geojson")
print("Open where.html to view the data in a browser")

