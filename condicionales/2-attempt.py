print("1 = multiplicacion");
print("2 = suma");
print("3 = resta");
num1 = int(input("¿Que accion deseas realizar? "));

if(num1 == 1):
    mult1 = int(input("Dime el primer numero que quieras multiplicar "));
    mult2 = int(input("Dime el segundo numero que quieras multiplicar "));
    print("El resultado de tu multiplicacion es", mult1 * mult2);
    
elif(num1 == 2):
    suma1 = int(input("Dime el primer numero que quieras sumar "));
    suma2 = int(input("Dime el segundo numero que quieras sumar "));
    print("El resultado de tu suma es", suma1 + suma2);
    
elif(num1 == 3):
    rest1 = int(input("Dime el primer numero que quieras restar "));
    rest2 = int(input("Dime el segundo numero que quieras restar "));
    print("El resultado de tu resta es", rest1 - rest2);
else :
    print("esta operacion no existe por ahora");

