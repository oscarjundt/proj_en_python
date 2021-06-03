from math import*
while True:
    print("fonction du polinome du seconde degre")
    p=input()
    if(p=="oui"):
        print("la fonction est ax^2+bx+c")
        print("l'autre facon et a(x-alpha)^2+beta")
        print("calculer alpha est beta")
        print("a")
        a=int(input())
        print("b")
        b=int(input())
        print("c")
        c=int(input())
        print("alpha")
        alpha=((-b)/(2*a))
        print(alpha)
        print("beta")
        def f(x):
            print(a*x*x+b*x+c)
        f(alpha)
        print("trouver le discriminant")
        hello=input()
        if(hello=="oui"):
            discriminant=b*b-4*a*c
            if(discriminant<0):
                print("impossible")
                print(discriminant)
            elif(discriminant>0):
                print("deux solution")
                print(discriminant)
            else:
                print("une seule solution -b/2*a")
                print(discriminant)                
            print("vouler vous avoir les racins")
            chose=input()
            if(chose=="oui"):
                if(discriminant>0):
                    print(((-b)+sqrt(discriminant))/(2*(a)))
                    print(((-b)-sqrt(discriminant))/(2*(a)))
                elif(discriminant==0):
                    print((-b)/(2*a))
                else:
                    print("impossible")
    if(p=="non"):
        break