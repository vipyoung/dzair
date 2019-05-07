import time
from datetime import datetime
import json
from collections import defaultdict
import sys


def to_ts(tw_time):
	return time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tw_time,'%a %b %d %H:%M:%S +0000 %Y'))

def to_ts_h(tw_time):
	return time.strftime('%Y-%m-%d %H', time.strptime(tw_time,'%a %b %d %H:%M:%S +0000 %Y'))

def to_ts_day(tw_time):
	return time.strftime('%Y-%m-%d', time.strptime(tw_time,'%a %b %d %H:%M:%S +0000 %Y'))



if __name__ == '__main__':
	fname = sys.argv[1]
	fout = sys.argv[2]
	h_ts = defaultdict(int)
	with open(fname) as f:
		for line in f:
			try:
				o = json.loads(line)
				h_ts[to_ts_day(o['created_at'])] += 1
			except:
				continue


	labels = []
	data = []	
	for k in sorted(h_ts.keys()):
		labels.append(k)
		data.append(h_ts[k])

	with open(fout, 'w') as g:
		g.write("var line_daily = {'labels': [%s], 'datasets': [{'label': 'Daily Volumes', 'data': [%s]}]}" % (','.join(labels), ','.join(map(str, data))))


	# # Combine the two files
	# tweets = dict()
	# with open('search.json') as f:
	# 	for line in f:
	# 		tweets[json.loads(line)['id']] = line
	# with open('search_new.json') as f:
	# 	for line in f:
	# 		tweets[json.loads(line)['id']] = line
	# print len(tweets)
	#
	# with open('search_comb.json', 'w') as g:
	# 	g.write(''.join(tweets.values()))
