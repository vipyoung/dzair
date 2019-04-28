import json
import sys
from collections import defaultdict


"""
NAME_1: wilaya
NAME_2: commune
ID_1: wilaya
ID_2: commune
"""

ids_file = sys.argv[1]
output_file = sys.argv[2]
output_file_wilaya = sys.argv[3]

ids = dict()
with open(ids_file) as f:
	f.readline()
	for line in f:
		x = line.strip('\n').split('\t') 
		ids[int(x[0])] = x[5]

features = []
w_ids = defaultdict(int)
with open('communes.geojson') as f:
	x = json.load(f)
	for _ in x['features']:
		p = _['properties']
		if p['ID_2'] in ids:
			p['VOTE'] = 0
			p['PARTY'] = ids[p['ID_2']]
			features.append(_)
			w_ids[p['ID_1']] += 1
x['features'] = features

# Write commune js
with open(output_file, 'w') as g:
	g.write('var commData = %s;' % json.dumps(x))

# write wilaya js
print('nb wilayas:%s' % (len(w_ids)))
features = []
with open('wilayas.geojson') as f:
	x = json.load(f)
	for _ in x['features']:
		p = _['properties']
		if p['ID_1'] in w_ids:
			p['VOTE'] = 0
			p['NAME_2'] = w_ids[p['ID_1']]
			features.append(_)

x['features'] = features

with open(output_file_wilaya, 'w') as g:
	g.write('var wilaData = %s;' % json.dumps(x))
# json.dump(x, open('communes_vote.geojson', 'w'))
