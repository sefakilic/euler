s = ""
cur = 1

while len(s) < 1000000:
    s += str(cur)
    cur += 1

lst = [s[0], s[9], s[99], s[999], s[9999], s[99999], s[999999]]
print reduce(lambda x, y: x*y, map(int, lst))
