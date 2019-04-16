import json
import sys
"""
NAME_1: wilaya
NAME_2: commune
ID_1: wilaya
ID_2: commune
"""

name = sys.argv[1]
x = json.load(open('communes_vote.geojson'))
for _ in x['features']:
	p = _['properties']
	if name in p['NAME_2'].lower():
		print 'W: ', p['NAME_1'], '\tC: ',p['NAME_2'], '\tID: ',p['ID_2'] 
