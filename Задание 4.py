str = 'Follow your heart'
d = {}
for i in str:
    d[i] = str.count(i)
d.pop(' ')
print(d)