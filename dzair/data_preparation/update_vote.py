import json
import sys
"""
NAME_1: wilaya
NAME_2: commune
ID_1: wilaya
ID_2: commune
"""

ids_str = sys.argv[1]
ids = map(int, ids_str.split(','))

with open('communes_vote.geojson') as f:
	x = json.load(f)
	for _ in x['features']:
		p = _['properties']
		if p['ID_2'] in ids:
			p['VOTE'] = 0

json.dump(x, open('communes_vote.geojson', 'w'))
