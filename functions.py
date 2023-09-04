def pi_organizer(pi=0):

    if pi == 3.1415:
        print("Pi NUMBER IS Correct")
        return True
    elif pi <= 3 :
        print("Pi NUMBER IS NOT Correct")
        return False
    else :
        print("Not any information") 
        return False
    return pi

def is_capital(city_name,capitals):
    if city_name in capitals:
        print(city_name + " yes it is!")
        return True
    elif city_name.capitalize() in capitals:
        print(city_name.capitalize() + " yes but not actualy")
        return True
    else:
        return False


def my_filter(input,cptls):
    if isinstance(input,str):
        out = is_capital(input,capitals=cptls)
    else:
        out = pi_organizer(input)
    return out

capitals = ["Seul","Berlin","Tokyo"]

inputs = ["İstanbul",2,64,"berlin",3.1415,"tokyo",3,2,3,"Seul"]

for input in inputs:

    output= my_filter(input,capitals)
    print(output)