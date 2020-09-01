P = 'Python'
r = P.replace('ho', '')
revString = []
print(r)
j = len(r)

# without using reverse()
while j > 0:
    revString += r[j - 1]
    j = j - 1
print(revString)
k = ','.join(revString)
print(k)

k = k.replace(',', '')
print(k)
