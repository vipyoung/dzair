import json
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
x = json.load(open(input_file))
new_features = []
for _ in x['features']:
	p = _['properties']
	if p['VOTE'] != 1:
		new_features.append(_)
x['features'] = new_features
with open(output_file, 'w') as g:
	g.write('var commData = %s;' % json.dumps(x))
