import sys

in_f = sys.argv[1]
out_f = sys.argv[2]

start = 'var users = ['
end = '];'
s= '{text: "%s", weight: %s, link: {href: "http://www.twitter.com/%s", target:"_blank"}},\n'
l = ''

with open(in_f) as f, open(out_f, 'w') as g:
	for i, line in enumerate(f):
		k,v = line.strip().split('\t')
		l += s % (v,k,v)
		if i > 80:
			break
	g.write(start + l[:-2] + end)
