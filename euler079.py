import urllib2
import itertools

def main():
    
    text = urllib2.urlopen('http://projecteuler.net/project/keylog.txt').read()
    logins = text.split()

    d = 4
    while True:
        print 'd:', d
        for p in itertools.product(xrange(10), repeat=d):
            for login in logins:
                try:
                    i = p.index(login[0])
                    j = p.index(login[1], i+1)
                    k = p.index(login[2], j+1)
                    print p
                    return
                except ValueError:
                    break
        
        d += 1
    
    
    
