nombre=str(input("ingrese nombre del estudiante: "))
codigo=int(input("ingrese codigo del estudiante: "))
primerp=float(input("ingrese nota primer parcial: "))
segundop=float(input("ingrese nota segundo parcial: ")) 
examenf=float(input("ingrese nota examen final: "))

definitiva= round(primerp*0.35 +segundop*0.35 + examenf*0.35)

if primerp>50 or segundop>50 or examenf>50:
   print("valores no validos, recuerde que las notas van desde 0.0 a 5.0")

elif definitiva >3.5:
    print("el estudiante ",nombre, " con codigo" ,codigo," aprobo con ",definitiva)
else:
    print("el estudiante ",nombre, " con codigo" ,codigo, "no aprobo, su definitiva es de ",definitiva)

