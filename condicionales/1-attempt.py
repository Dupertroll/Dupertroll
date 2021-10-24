print("Hola, gracias por llamar a DuperPizzas, a continuacion le mostraere nuestro menu")
print("1 = pizza normal");
print("2 = pizza vegetariana");
preguntar = int(input("¿Cual le gustaria ordenar señor? "));

if (preguntar >= 3):
    print("esa orden no existe por ahora, vuelva pronto.");
if(preguntar == 1):
    pizza1 = input("Esta pizza contiene peperoni, queso y jamon, asi esta bien? ");
    if(pizza1 == "si"):
        print("Esta bien, su orden ya esta en camino");
    else:
        print("Lamentamos no cumplir sus expectativas, fue un placer hablar con usted, tenga un buen dia.");
if(preguntar == 2):
    pizza2 = input("Esta pizza contiene tofu, queso y pimienta, ¿asi esta bien? ");
    if(pizza2 == "si"):
        print("Esta bien, su orden ya esta en camino");
    else:
        print("Lamentamos no cumplir sus expectativas, fue un placer hablar con usted");
        