from turtle import*
while True:
    print("valeur")
    x=int(input())
    print("choisir entre dessin et md")
    c=input()
    if(c=="dessin"):
        reset()
        b=0
        while(b<20):
            a=0
            while(a<4):
                forward(100)
                left(90)
                a=a+1
            left(x)
            while(a<4):
                forward(100)
                left(100)
                a=a+1
            b=b+1
    if(c=="md"):
            g=0
            while(g<5):
                a=0
                while(a<3):
                    forward(100)
                    left(x)
                    a=a+1
                b=0
                while(b<3):
                    forward(100)
                    left(x)
                    b=b+1
                g=g+1          