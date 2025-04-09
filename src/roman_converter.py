def decimal_to_romano(num):
    romanos={1:"I", 4:"IV",5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
    resultado=""
    for i in [1000,900,500,400,100,90,50,40,10,9,5,4,1]:
        while num>=i:
            resultado+=romanos[i]
            num-=i
    return resultado

def main():
    vuelta="y"
    while vuelta=="y":
        val=int(input("ingrese el valor a convertir a romano"))
        while val>3999:
            val=int(input("ingrese de nuevo valor a convertir a romano"))
        romano=decimal_to_romano(val)
        print(f"{val} en romano es {romano}")
        vuelta=str(input("si desea continuar ponga y, del contrario ponga cualquier letra"))
        

if __name__ == "__main__":
    main()