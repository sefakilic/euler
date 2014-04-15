"""
Use dynamic programming
"""

triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

tr = []
rows = triangle.split('\n')
for row in rows[1:-1]: # first and last lines are empty
    tr.append(map(int, row.split()))

best_path = [] # sum of numbers from top to i'th number in current row
best_path = [75]
for row in tr[1:]: # after first row
    print best_path
    new_path = []
    # the leftmost number of current row
    new_path.append(best_path[0] + row[0])
    for i,num in enumerate(row[1:-1]): # until rightmost number
        new_path.append(max(best_path[i], best_path[i+1]) + row[i+1])
    # the rightmost number of current row
    new_path.append(best_path[-1] + row[-1])
    best_path = new_path[:]
        
print best_path

print max(best_path)
