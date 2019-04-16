import json
import sys
"""
NAME_1: wilaya
NAME_2: commune
ID_1: wilaya
ID_2: commune
"""

x = json.load(open('communes.geojson'))
for _ in x['features']:
	p = _['properties']
	print u'' + p['NAME_1'].encode('utf8') + u','+p['NAME_2'].encode('utf8') + u','+ str(p['ID_2']) 
	#print u'%s,%s,%s\n' % (p['NAME_1'] ,p['NAME_2'] ,p['ID_2']) 
	# print p['NAME_1'],',',p['NAME_2'],',', p['ID_2'] 
