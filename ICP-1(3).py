

Text = input("Enter a sentence")
p = Text.split()
k = []
String = ''
for j in p:
    if j == 'python':
        k=j.split()
        k.append('s')

        j = ','.join(k)

        j = j.replace(',','')


    String += j + ' '
print(String)
