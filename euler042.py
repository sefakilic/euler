import urllib2

text = urllib2.urlopen('http://projecteuler.net/project/words.txt').read()
words = [w for w in text.replace('"', '').split(',')]
print len(words)

n_last = 1
triangles = [1]
triangle_words = 0

for w in words:
    value = sum(ord(c) - ord('A') + 1 for c in w)
    while value > triangles[-1]:
        n_last += 1
        triangles.append(n_last * (n_last+1) / 2)
    if value in triangles:
        triangle_words += 1
        
print triangles
print triangle_words
