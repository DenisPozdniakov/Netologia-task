y = ['2018-01-01', 'yandex', 'cpc', 100]

x = y[-1]

for i in range(len(y)-1, 0, -1):
    z = y[i-1]
    p = {z : x}
    x = p
    
print(p)   
    
