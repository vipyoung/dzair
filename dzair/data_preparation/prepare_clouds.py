import sys

in_f = sys.argv[1]
out_f = sys.argv[2]

start = 'var hashtags = ['
end = '];'
s = '{text: "%s", weight: %s},\n'
l = ''
with open(in_f) as f, open(out_f, 'w') as g:
	for i, line in enumerate(f):
		k,v = line.strip().split('\t')
		l += s % (v,k)
		if i > 80:
			break
	g.write(start + l[:-2] + end)
