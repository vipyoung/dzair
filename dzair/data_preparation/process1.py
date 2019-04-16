import json

x = json.load(open('communes.geojson'))
for _ in x['features']:
	p = _['properties']
	p1 = {'NAME_1': p['NAME_1'],
		'NAME_2': p['NAME_2'],
		'ID_1': p['ID_1'],
		'ID_2': p['ID_2'],
		'VOTE': 1}
	_['properties'] = p1

json.dump(x, open('communes_vote.geojson', 'w')) 
