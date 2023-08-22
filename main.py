name="Mustafa"
surname= "Yildiz"
surnames =["Yildiz", "Aksoy","Demir"]

if surname in surnames:
    print(True)
elif surname not in surnames:
    print(False)
    
for soyad in surnames:
    #print(soyad)
    if surname ==soyad:
        print(True)
        print(soyad)
    else:
        print(False)
        print(soyad)

a=0
while 1:
    print("Elma")
    print(a)
    a+=a
    if a>4:
        break
while a<4:
    print("Elma")
    print(a)
    a+=a


 while a<5:
    print("Elma")
    print(a)
    if a == 2:
        continue #buradan sonra asagi girmeden whiledan devam ediyor
    a+=a   
print(name[0])

print(surnames[0])

