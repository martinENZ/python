#Calcular la masa corporal de una persona mediante el peso y altura 
peso=float(input("Por favor ingrese su peso en KG: "))
altura=float(input("por favor ingrese su altura en Mts: "))
imc=round(peso/(altura**2))
print("su IMC es de: ", str(imc))
