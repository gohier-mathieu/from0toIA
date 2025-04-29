
#fonction pour convertir les celsius en fahrenheit

def CelsiusToFahrenheit(celsius):
    fahrenheit = (celsius*9/5)+32
    return fahrenheit
    
#fonction pour convertir les fahrenheit en celsius 

def FahranheitToCelsius(fahrenheit):
    celsius = ( fahrenheit-32)*5/9
    return celsius

def main():
    print("choisissez votre conversion :")
    print("1 : °c to °f")
    print("2 : °f to °c")

    choice = float(input("choice : "))

    if choice == 1:
        value_celsius = float(input("entrez la valeur en celsius :"))
        value_fahrenheit = CelsiusToFahrenheit(value_celsius)
        print(f"{round(value_fahrenheit, 2)} °F")
    
    elif choice == 2:
        value_fahrenheit = float(input("entrez la valeur en fahrenheit :"))
        value_celsius = FahranheitToCelsius(value_fahrenheit)
        print(f"{round(value_celsius, 2)} °C")

    else:
        print("choix invalide")




if __name__ == "__main__":
    main()
