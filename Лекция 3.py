g=''
for po in range(10):
    slovar={'Sochi':'AD123', 'Sochi':'DN345', 'Sochi':'JO098','MinVod':'DS098','MinVod':'DI098'}
    for i in range(10):
        s1=slovar
        g1=slovar.get('Sochi')
        g=g+g1
        del slovar['Sochi']
    print(g)