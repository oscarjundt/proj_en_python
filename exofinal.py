from tkinter import*
f=Tk()
m=StringVar()
hel=0
bert=0
me=1
merde=["0","1","2","3","4","5","6","7","8","9"]
chien=[]
a=Label(f,text="entre code")
a.pack()
b=Entry(f,textvariable=m)
b.configure(show="*")
b.pack()
c=Canvas(f,height=289,width=289)
c.configure(bg="white")
c.pack()
d=Button(f,text="appuyer")
d.pack()
for i in range(0,10):
    if(i<5):
        l=c.create_text(50*(i+1),50,text=merde[i],font="arial 20")
    else:
        hel=hel+1       
        l=c.create_text(50*hel,100,text=merde[i],font="arial 20")
def ch(event):
    if(event.x<69):
        if(event.y<=70):
            chien.append("0")
            print(chien)
    if(event.x>90 and event.x<114):
        if(event.y<=70): 
            chien.append("1")
            print(chien)
    if(event.x>120 and event.x<180):
        if(event.y<=70):
            chien.append("2")
            print(chien)
    if(event.x>190 and event.x<230):
        if(event.y<=70):
            chien.append("3")
            print(chien)
    if(event.x>240):
        if(event.y<=70):
            chien.append("4")
            print(chien)
    if(event.x<=50):
        if(event.y>90):
            chien.append("5")
            print(chien)
    if(event.x>80 and event.x<130):
        if(event.y>90): 
                chien.append("6")
                print(chien)
    if(event.x>=140 and event.x<180):
        if(event.y>90):
                chien.append("7")
                print(chien)
    if(event.x>190 and event.x<220):
        if(event.y>90):
            chien.append("8")
            print(chien)
    if(event.x>=245):
        if(event.y>90):
                chien.append(9)
                print(chien)    
c.bind("<Button-1>",ch)
def mert(event):
    print(event.x)
    print(event.y)
c.bind("<Button-3>",mert)
def mer(event):
    global chien
    global bert
    def lef():
        a.configure(text="entre code")
    x=list(m.get())
    for o in range(0,4):
        if(chien[o]==x[o]):
            lie=c.create_oval(20*(o+10),200,30*(o),300,fill="red")
            bert=bert+1
    def oval():
        lie=11
        for eh in range(0,4):
            c.delete(lie)
            lie=lie+1
    c.after(1000,oval)     
    if(bert==4):
        a.configure(text="juste")
        chien=[]
        bert=0
        f.after(1000,lef)
    else:
        a.configure(text="faute {} erreur".format(4-bert))
        chien=[]
        f.after(1000,lef)  
d.bind("<ButtonPress-1>",mer)
f.mainloop()