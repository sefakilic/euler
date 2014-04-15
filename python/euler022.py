import urllib2
u = urllib2.urlopen('http://projecteuler.net/project/names.txt')
names = sorted(u.read().replace('"','').split(','))
scores = sum(sum(ord(c)-ord('A')+1 for c in name)*(i+1) for i,name in enumerate(names))
print scores

