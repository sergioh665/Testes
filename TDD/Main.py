import ModDiv as md
import Calculadora
import Fatorial as ft

def main():
    
    a = md.ModDiv()
    f = ft.Fatorial()
    
    
    print("ModDiv - DIV")
    print(a.div(5,2))
    print(a.div(10,3))
    print(a.div(15,4))
    print(a.div(20,5))
    print(a.div(25,6))
    print(a.div(30,7))
    print(a.div(35,8))
    print(a.div(40,9))
    
    print("\nModDiv - MOD")
    print(a.mod(30,7))
    print(a.mod(35,8))
    print(a.mod(40,9))
    print(a.mod(45,10))
    print(a.mod(50,11))
    print(a.mod(55,12))
    print(a.mod(60,13))
    print(a.mod(65,14))
    
    
    print("\nFATORIAL")
    print(f.calcular(7))
    
main()