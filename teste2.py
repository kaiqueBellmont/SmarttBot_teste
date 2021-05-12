from datetime import datetime

a = str(datetime.now())
print(a)
a = a.split()
data = a[0]
hora = a[1].split('.')[0]
print(data)
print(hora)
