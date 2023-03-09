def año_bisiesto(año):
    if (año % 4) == 0:
        if (año % 100) == 0:
            if (año % 400) == 0:
                print("Este año es un año BISIESTO")
            else:
                print("Este año NO es un año BISIESTO")   
        else:
            print("Este año es un año BISIESTO")
    else:
        print("Este año NO es un año BISIESTO")        

año_bisiesto(2000)