def pi_organizer(pi):
    if pi>3:
        print("buyuktur uc")
        return True
    elif pi 3<=3:
        print("buyuk degıldır uc")
        return False
    else:
        print("tanımsız")
        return False
    

input=[3, 6, 12,4,324,1.435,3.1415]

for inp in input:

output= pi_organizer(pi=inp)
print(output)