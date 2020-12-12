
from numpy import * 
from tkinter import * 
def CFG():
    f=open("Test4.txt","r") 
    vercount=1;i=0;start=1;end1=1;end2=1;predicates=0;

    vertices=[1] 
    Edge1=[]

    Edge2=zeros((15,15),int)

    lines=[] 
    for var in f:
        lines.append(var)
    while(i<len(lines)):
        if(lines[i].find('if')!=-1):
            vercount+=1 
            vertices.append(vercount)
            start=vercount
            Edge2[vercount-1][vercount]=1
            Edge1.append(str(vercount-1)+"-->"+str(vercount))
            vercount+=1
            vertices.append(vercount)
            Edge2[vercount-1][vercount]=1; end1=vercount;
            Edge1.append(str(vercount-1)+"-->"+str(vercount))
            while(lines[i].find('}')==-1):
                i+=1
            i+=1 
            if(lines[i].find('else')!=-1):
                vercount+=1
                vertices.append(vercount)
                end2=vercount
                Edge2[start][end2]=1
                Edge1.append(str(start) + "-->" + str(end2))
                vercount += 1
                vertices.append(vercount)
                Edge2[end1][vercount]=1
                Edge1.append(str(end1) + "-->" + str(vercount))
                Edge2[end2][vercount]=1
                Edge1.append(str(end2) + "-->" + str(vercount))
                while(lines[i].find('}')==-1):
                    i+=1
                i+=1
            else:
                vercount += 1
                vertices.append(vercount)
                Edge2[end1][vercount]=1
                Edge1.append(str(end1) + "-->" + str(vercount))

        elif(lines[i].find('for')!=-1):
            vercount += 1
            vertices.append(vercount)
            Edge2[vercount-1][vercount]=1
            Edge1.append(str(vercount-1)+"-->"+str(vercount))
            vercount += 1
            vertices.append(vercount)
            Edge2[vercount - 1][vercount] = 1
            Edge1.append(str(vercount-1)+"-->"+str(vercount))
            Edge2[vercount-2][vercount] = 1
            Edge1.append(str(vercount-2)+"-->"+str(vercount))
            while(lines[i].find('}')==-1):
                i+=1
            i+=1

        elif(lines[i].find('while')!=-1):
            vercount += 1
            vertices.append(vercount)
            Edge2[vercount - 1][vercount] = 1
            Edge1.append(str(vercount-1)+"-->"+str(vercount))
            vercount += 1
            vertices.append(vercount)
            Edge2[vercount - 1][vercount] = 1
            Edge1.append(str(vercount-1)+"-->"+str(vercount))
            Edge2[vercount - 2][vercount] = 1
            Edge1.append(str(vercount-2)+"-->"+str(vercount))
            while (lines[i].find('}') == -1):
                i += 1
            i += 1

        else:
            i+=1

    

    f.close()

    g=open("Test4.txt","r")

    for vars in g:
        if(vars.find('if')!=-1 or vars.find('for')!=-1 or vars.find('while')!=-1):
            predicates+=1
     
    g.close()

    return vercount,predicates,vertices,Edge2,Edge1

def Return(frame):
    frame.destroy()
    main()

def testinput(frame):
    frame.destroy()
    frame = Frame(root)
    frame.pack(fill=X)
    f = open("Test4.txt", "r")
    label = Label(frame, text=f.read(),font='Verdana 10 bold')
    label.grid()
    f.close()
    ret=Button(frame,text='Return',height=5,width=30,font='Verdana 12 bold',command=lambda: Return(frame))
    ret.grid()

def Noodes(frame):
    values=CFG()
    frame.destroy()
    frame = Frame(root)
    frame.pack(fill=X)
    s="Total no. of Nodes are =" + str(values[0])
    label = Label(frame,text=s,font='Verdana 30 bold')
    label.grid()
    label = Label(frame, text=str(values[2]), font='Verdana 30 bold')
    label.grid()
    ret = Button(frame, text='Return', height=5, width=30, font='Verdana 12 bold', command=lambda: Return(frame))
    ret.grid()


def Edge1(frame):
    values = CFG()
    r=1;c=0;
    frame.destroy()
    frame = Frame(root)
    frame.pack(fill=X)
    s = "Edges of the Control Flow Graph are "
    label = Label(frame, text=s, font='Verdana 30 bold')
    label.grid()
    for i in values[4]:
        label = Label(frame, text=i, font='Verdana 30 bold')
        label.grid(row=r,column=c)
        c+=1
        if(c>3):
            r+=1
            c=0

    ret = Button(frame, text='Return', height=5, width=30, font='Verdana 12 bold', command=lambda: Return(frame))
    ret.grid()


def main():


    frame=Frame(root)

    frame.pack(fill=X)

    TestInput=Button(frame,text='Testinput',height=5,width=30,font='Verdana 12 bold',command=lambda: testinput(frame))

    TestInput.pack(side='top')

    Nodes=Button(frame,text='Nodes',height=5,width=30,font='Verdana 12 bold',command=lambda: Noodes(frame))

    Nodes.pack(side='top')

    Edge2=Button(frame,text='Edges',height=5,width=30,font='Verdana 12 bold',command=lambda: Edge1(frame))

    Edge2.pack(side='top')

root = Tk()

root.title('Control Flow Graph')

main()

root.mainloop()
