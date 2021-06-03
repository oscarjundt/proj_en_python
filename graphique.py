from turtle import*
a=0
print("distance")
b=int(input())
print("boucle")
c=int(input())
print("angle")
d=int(input())
print("fois")
h=int(input())

while(a<c):
    color("blue")
    forward(b)
    color("white")
    forward(b)
    color("red")
    forward(b)
    left(d)
    print((d),":","degre", ";" , b , ":" ,"cm")
    a,b,d=a+1,b+1,d+h