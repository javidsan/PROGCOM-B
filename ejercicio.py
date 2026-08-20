print("----- Crea tu login para la clase de progamacion II------\n")
usu=input("ingresa tu nombre de usuario: ")
print("")
print(f"¡listo {usu}! Ahora creemos una contraseña segura...\n") 
n=0
while True:
    print("1. Tener una mayuscula \n2. Tener minimo 10 caracteres \n3. Poseer un valor alfanumerico \n4. Tener al menos un valor numerico\n")
    contra=input("Digite una conttraseña segura: ")
    print("")
    if len(contra)<10:
        print(f"Creo que ers un poco taradit@ {usu} jeje. ¡MAS DE 10 CARACTERES! \n")
    elif not any(mayus.isupper() for mayus in contra):
        print("¿No sabes que es una mayuscula? ¡LEE ENTONCES ANALFABETA!\n")
    elif not any(number.isdigit() for number in contra):
        print("¡SE NOTA QUE NO TE DIERON TABLA PARA QUE TE APRENDIERAS QUE SON LOS NUMEROS!\n")
    else:
        print("¡listo tu contraseña se guardo correctamente!")
        print("")
        break
    n+=1
if n==1:
    print(f"Nota: Te falta comprension lectora no? mr {usu}")
elif n==2:
    print("Nota: {usu} ¿tu eras de los que ni estudiando aprobabas?")
elif n>=3:
    print(f"NOTA: {usu} Creo que entras en el top 10 de los mas PENDEJOS...")
