import json
import sys
"""
NAME_1: wilaya
NAME_2: commune
ID_1: wilaya
ID_2: commune
"""

x = json.load(open('communes.geojson'))
with open('communes.csv', 'w') as g:
	for _ in x['features']:
		p = _['properties']
		g.write('%s,%s,%s\n' % (p['ID_2'], p['NAME_1'].encode('utf8') ,p['NAME_2'].encode('utf8'))) 
