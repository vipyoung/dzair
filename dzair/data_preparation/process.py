import json

x = json.load(open('communes.geojson'))
for _ in x['features']:
	p = _['properties']
	print p['ID_2'] 
