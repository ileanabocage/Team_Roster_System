import tkinter as tk
root=tk.Tk()
root.geometry("720x310")
root.title('Home')

frame=tk.Frame(root)
frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)

class Roster(object):
    def __init__(self,name,gender,age,number,email,eventstr,eventfloat):
        self.name = name
        self.gender = gender
        self.age = age
        self.number = number
        self.email = email
        self.eventstr = eventstr
        self.eventfloat = eventfloat
        
class Girls(Roster):
    def __init__(self,name,gender,age,number,email,eventstr,eventfloat):
        self.gender = 'Girl'
        super().__init__(name,gender,age,number,email,eventstr,eventfloat)

class _10AndUnderG(Girls):
    def __init__(self,name,gender,age,number,email,eventstr,eventfloat):
        super().__init__(name,gender,age,number,email,eventstr,eventfloat)

class _11To12G(Girls):
    def __init__(self,name,gender,age,number,email,eventstr,eventfloat):
        super().__init__(name,gender,age,number,email,eventstr,eventfloat)

class _13To14G(Girls):
    def __init__(self,name,gender,age,number,email,eventstr,eventfloat):
        super().__init__(name,gender,age,number,email,eventstr,eventfloat)

class _15AndOverG(Girls):
    def __init__(self,name,gender,age,number,email,eventstr,eventfloat):
        super().__init__(name,gender,age,number,email,eventstr,eventfloat)

class Boys(Roster):
    def __init__(self,name,gender,age,number,email,eventstr,eventfloat):
        self.gender = 'Boy'
        super().__init__(name,gender,age,number,email,eventstr,eventfloat)

class _10AndUnderB(Boys):
    def __init__(self,name,gender,age,number,email,eventstr,eventfloat):
        super().__init__(name,gender,age,number,email,eventstr,eventfloat)

class _11To12B(Boys):
    def __init__(self,name,gender,age,number,email,eventstr,eventfloat):
        super().__init__(name,gender,age,number,email,eventstr,eventfloat)

class _13To14B(Boys):
    def __init__(self,name,gender,age,number,email,eventstr,eventfloat):
        super().__init__(name,gender,age,number,email,eventstr,eventfloat)

class _15AndOverB(Boys):
    def __init__(self,name,gender,age,number,email,eventstr,eventfloat):
        super().__init__(name,gender,age,number,email,eventstr,eventfloat)

f = open('Roster.txt','r')

p1 = []
p2 = []
p3 = []
p4 = []
p5 = []
p6 = []
p7 = []
p8 = []
for i in range (0,32):
    name1 = f.readline()
    name1 = name1.strip()
    gender1 = f.readline()
    gender1 = gender1.strip()
    age1 = f.readline()
    age1 = int(age1)
    number1 = f.readline()
    number1 = int(number1)
    email1 = f.readline()
    email1 = email1.strip()
    e1 = f.readline()
    e1 = e1.strip()
    t1 = f.readline()
    x=0
    y=2
    a=0 
    b=1
    ch=':'
    event1str={}
    event1float={}
    num = t1.count(' ') + 1         #Uses spaces to determine the number of elements in t1
    for i in range(num):
        events1 = e1.split()[x:y]
        events1 = ' '.join(events1) #Joins list values into a string
        t2 = t1.split()[a:b]
        t2 = ' '.join(t2)
        if ch in t2:
            times1=t2.split(':')
            tmin=int(times1[0])*60
            ts=float(times1[1])
            times1=tmin+ts 
        else:
            t2.strip()
            times1 = float(t2)
        event1str[events1]=t2
        event1float[events1]=times1
        x+=2
        y+=2
        a+=1
        b+=1
    
    p = Roster(name1,gender1,age1,number1,email1,event1str,event1float)
    if (p.gender == 'Girl'):
        if (p.age <= 10):
            P1 = _10AndUnderG(name1,gender1,age1,number1,email1,event1str,event1float)
            p1.append(P1)
            
        elif ((p.age >= 11) and p.age <=12):
            P2 = _11To12G(name1,gender1,age1,number1,email1,event1str,event1float)
            p2.append(P2)
            
        elif ((p.age >= 13) and p.age <=14):
            P3 = _13To14G(name1,gender1,age1,number1,email1,event1str,event1float)
            p3.append(P3)
            
        else:
            P4 = _15AndOverG(name1,gender1,age1,number1,email1,event1str,event1float)
            p4.append(P4)
            
    elif (p.gender == 'Boy'):
        if (p.age <= 10):
            P5 = _10AndUnderB(name1,gender1,age1,number1,email1,event1str,event1float)
            p5.append(P5)

        elif ((p.age >= 11) and p.age <=12):
            P6 = _11To12B(name1,gender1,age1,number1,email1,event1str,event1float)
            p6.append(P6)

        elif ((p.age >= 13) and p.age <=14):
            P7 = _13To14B(name1,gender1,age1,number1,email1,event1str,event1float)
            p7.append(P7)

        else:
            P8 = _15AndOverB(name1,gender1,age1,number1,email1,event1str,event1float)
            p8.append(P8)

    else:
        print("Error")

f.close()


def DisplayRoster():
    global labelsR
    labelsR=[]
    label=tk.Label(roster,text='10 & Under Girls',font='Helvetica 10 underline')
    labelsR.append(label)
    y=0.03
    label.place(relx=0.2,rely=y)
    for j in range (0,len(p1)):
        y+=0.03
        label=tk.Label(roster,text=p1[j].name)
        label.place(relx=0.2,rely=y)
        labelsR.append(label)

    label=tk.Label(roster,text='11-12 Girls',font='Helvetica 10 underline')
    labelsR.append(label)
    y+=0.06
    label.place(relx=0.2,rely=y)
    for j in range (0,len(p2)):
        y+=0.03
        label=tk.Label(roster,text=p2[j].name) 
        label.place(relx=0.2,rely=y)
        labelsR.append(label)

    label=tk.Label(roster,text='13-14 Girls',font='Helvetica 10 underline')
    labelsR.append(label)
    y+=0.06
    label.place(relx=0.2,rely=y)
    for j in range (0,len(p3)):
        y+=0.03
        label=tk.Label(roster,text=p3[j].name) 
        label.place(relx=0.2,rely=y)
        labelsR.append(label)

    label=tk.Label(roster,text='15 & Over Girls',font='Helvetica 10 underline')
    labelsR.append(label)
    y+=0.06
    label.place(relx=0.2,rely=y)
    for j in range (0,len(p4)):
        y+=0.03
        label=tk.Label(roster,text=p4[j].name)
        label.place(relx=0.2,rely=y)
        labelsR.append(label)

    label=tk.Label(roster,text='10 & Under Boys',font='Helvetica 10 underline')
    labelsR.append(label)
    y=0.03
    label.place(relx=0.6,rely=y)
    for j in range (0,len(p5)):
        y+=0.03
        label=tk.Label(roster,text=p5[j].name)
        label.place(relx=0.6,rely=y)
        labelsR.append(label)

    label=tk.Label(roster,text='11-12 Boys',font='Helvetica 10 underline')
    labelsR.append(label)
    y+=0.06
    label.place(relx=0.6,rely=y)
    for j in range (0,len(p6)):
        y+=0.03
        label=tk.Label(roster,text=p6[j].name) 
        label.place(relx=0.6,rely=y)
        labelsR.append(label)

    label=tk.Label(roster,text='13-14 Boys',font='Helvetica 10 underline')
    labelsR.append(label)
    y+=0.06
    label.place(relx=0.6,rely=y)
    for j in range (0,len(p7)):
        y+=0.03
        label=tk.Label(roster,text=p7[j].name) 
        label.place(relx=0.6,rely=y)
        labelsR.append(label)

    label=tk.Label(roster,text='15 & Over Boys',font='Helvetica 10 underline')
    labelsR.append(label)
    y+=0.06
    label.place(relx=0.6,rely=y)
    for j in range (0,len(p8)):
        y+=0.03
        label=tk.Label(roster,text=p8[j].name)
        label.place(relx=0.6,rely=y)
        labelsR.append(label)

def SaveSwimmer():
    _Name = newname.get()
    _Gender = newgender.get()
    _Age = int(newage.get())
    _Number = int(newnum.get())
    _Email = newemail.get()
    e1 = newevents.get()
    t1 = newtimes.get()
    x=0
    y=2
    a=0 
    b=1
    ch=':'
    _Eventstr={}
    _Eventfloat={}
    num = t1.count(' ') + 1         #Uses spaces to determine the number of elements in t1
    for i in range(num):
        events1 = e1.split()[x:y]
        events1 = ' '.join(events1) #Joins list values into a string
        t2 = t1.split()[a:b]
        t2 = ' '.join(t2)
        if ch in t2:
            times1=t2.split(':')
            tmin=int(times1[0])*60
            ts=float(times1[1])
            times1=tmin+ts 
        else:
            t2.strip()
            times1 = float(t2)
        _Eventstr[events1]=t2
        _Eventfloat[events1]=times1
        x+=2
        y+=2
        a+=1
        b+=1


    p = Roster(_Name,_Gender,_Age,_Number,_Email,_Eventstr,_Eventfloat)
    if (p.gender == 'Girl'):
        if (p.age <= 10):
            P1 = _10AndUnderG(_Name,_Gender,_Age,_Number,_Email,_Eventstr,_Eventfloat)
            p1.append(P1)
            
        elif ((p.age >= 11) and p.age <=12):
            P2 = _11To12G(_Name,_Gender,_Age,_Number,_Email,_Eventstr,_Eventfloat)
            p2.append(P2)
            
        elif ((p.age >= 13) and p.age <=14):
            P3 = _13To14G(_Name,_Gender,_Age,_Number,_Email,_Eventstr,_Eventfloat)
            p3.append(P3)
            
        else:
            P4 = _15AndOverG(_Name,_Gender,_Age,_Number,_Email,_Eventstr,_Eventfloat)
            p4.append(P4)
            
    elif (p.gender == 'Boy'):
        if (p.age <= 10):
            P5 = _10AndUnderB(_Name,_Gender,_Age,_Number,_Email,_Eventstr,_Eventfloat)
            p5.append(P5)

        elif ((p.age >= 11) and p.age <=12):
            P6 = _11To12B(_Name,_Gender,_Age,_Number,_Email,_Eventstr,_Eventfloat)
            p6.append(P6)

        elif ((p.age >= 13) and p.age <=14):
            P7 = _13To14B(_Name,_Gender,_Age,_Number,_Email,_Eventstr,_Eventfloat)
            p7.append(P7)

        else:
            P8 = _15AndOverB(_Name,_Gender,_Age,_Number,_Email,_Eventstr,_Eventfloat)
            p8.append(P8)
    else:
        print("Error")
    
    add.destroy()
    for label in labelsR:
        label.destroy()
    DisplayRoster()

def AddSwimmer():
    global add,newname,newgender,newage,newnum,newemail,newevents,newtimes
    add = tk.Toplevel()
    add.geometry("400x250")
    add.title('Add a New Swimmer')
    btn1 = tk.Button(add,text='BACK',command=add.destroy)
    btn1.grid(row=0,column=0)

    tk.Label(add,text='Please enter swimmer name:').grid(row=2,column=1)
    tk.Label(add,text="Please enter 'Girl' or 'Boy':").grid(row=3,column=1)
    tk.Label(add,text='Please enter age:').grid(row=4,column=1)
    tk.Label(add,text='Please enter phone number:').grid(row=5,column=1)
    tk.Label(add,text='Please enter email address:').grid(row=6,column=1)
    tk.Label(add,text='Please enter events:').grid(row=7,column=1)
    tk.Label(add,text='Please enter times for events:').grid(row=8,column=1)
    
    newname = tk.Entry(add)
    newname.grid(row=2,column=2)
        
    newgender = tk.Entry(add)
    newgender.grid(row=3,column=2)

    newage = tk.Entry(add)
    newage.grid(row=4,column=2)
    
    newnum = tk.Entry(add)
    newnum.grid(row=5,column=2)

    newemail = tk.Entry(add)
    newemail.grid(row=6,column=2)

    newevents = tk.Entry(add)
    newevents.grid(row=7,column=2)

    newtimes = tk.Entry(add)
    newtimes.grid(row=8,column=2)

    enter = tk.Button(add,text='ENTER',command=SaveSwimmer)
    enter.grid(row=9,column=2)


def ROSTER():
    global roster
    roster = tk.Toplevel()
    roster.geometry("720x600")
    roster.title('Roster')
    btn1 = tk.Button(roster,text='HOME',command=roster.destroy)
    btn1.grid(row=0,column=0)
    btn2 = tk.Button(roster,text='ADD SWIMMER',command=AddSwimmer)
    btn2.grid(row=0,column=1)
    Rlabel=tk.Label(roster,text='ROSTER',font='Helvetica 12')
    Rlabel.place(relx=0.45,rely=0)
    DisplayRoster()



def Free50():
    event = tk.Toplevel()
    event.geometry("720x600") 
    event.title('50 Free Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='50 FREE TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '50 Free' in b:
            d=b['50 Free']
            e=c['50 Free']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '50 Free' in b:
            d=b['50 Free']
            e=c['50 Free']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '50 Free' in b:
            d=b['50 Free']
            e=c['50 Free']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '50 Free' in b:
            d=b['50 Free']
            e=c['50 Free']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '50 Free' in b:
            d=b['50 Free']
            e=c['50 Free']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '50 Free' in b:
            d=b['50 Free']
            e=c['50 Free']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '50 Free' in b:
            d=b['50 Free']
            e=c['50 Free']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '50 Free' in b:
            d=b['50 Free']
            e=c['50 Free']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)  

def Free100():
    event = tk.Toplevel()
    event.geometry("720x600")
    event.title('100 Free Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='100 FREE TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '100 Free' in b:
            d=b['100 Free']
            e=c['100 Free']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '100 Free' in b:
            d=b['100 Free']
            e=c['100 Free']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '100 Free' in b:
            d=b['100 Free']
            e=c['100 Free']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '100 Free' in b:
            d=b['100 Free']
            e=c['100 Free']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '100 Free' in b:
            d=b['100 Free']
            e=c['100 Free']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '100 Free' in b:
            d=b['100 Free']
            e=c['100 Free']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '100 Free' in b:
            d=b['100 Free']
            e=c['100 Free']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '100 Free' in b:
            d=b['100 Free']
            e=c['100 Free']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)  

def Free200():
    event = tk.Toplevel()
    event.geometry("720x600")
    event.title('200 Free Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='200 FREE TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '200 Free' in b:
            d=b['200 Free']
            e=c['200 Free']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '200 Free' in b:
            d=b['200 Free']
            e=c['200 Free']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '200 Free' in b:
            d=b['200 Free']
            e=c['200 Free']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '200 Free' in b:
            d=b['200 Free']
            e=c['200 Free']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '200 Free' in b:
            d=b['200 Free']
            e=c['200 Free']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '200 Free' in b:
            d=b['200 Free']
            e=c['200 Free']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '200 Free' in b:
            d=b['200 Free']
            e=c['200 Free']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '200 Free' in b:
            d=b['200 Free']
            e=c['200 Free']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

def Free400():
    event = tk.Toplevel()
    event.geometry("720x600") 
    event.title('400 Free Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='400 FREE TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '400 Free' in b:
            d=b['400 Free']
            e=c['400 Free']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '400 Free' in b:
            d=b['400 Free']
            e=c['400 Free']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '400 Free' in b:
            d=b['400 Free']
            e=c['400 Free']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '400 Free' in b:
            d=b['400 Free']
            e=c['400 Free']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '400 Free' in b:
            d=b['400 Free']
            e=c['400 Free']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '400 Free' in b:
            d=b['400 Free']
            e=c['400 Free']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '400 Free' in b:
            d=b['400 Free']
            e=c['400 Free']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '400 Free' in b:
            d=b['400 Free']
            e=c['400 Free']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

def Free800():
    event = tk.Toplevel()
    event.geometry("720x600")
    event.title('800 Free Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='800 FREE TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '800 Free' in b:
            d=b['800 Free']
            e=c['800 Free']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '800 Free' in b:
            d=b['800 Free']
            e=c['800 Free']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '800 Free' in b:
            d=b['800 Free']
            e=c['800 Free']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '800 Free' in b:
            d=b['800 Free']
            e=c['800 Free']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '800 Free' in b:
            d=b['800 Free']
            e=c['800 Free']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '800 Free' in b:
            d=b['800 Free']
            e=c['800 Free']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)  

def Free1500():
    event = tk.Toplevel()
    event.geometry("720x600")
    event.title('1500 Free Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='1500 FREE TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '1500 Free' in b:
            d=b['1500 Free']
            e=c['1500 Free']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '1500 Free' in b:
            d=b['1500 Free']
            e=c['1500 Free']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '1500 Free' in b:
            d=b['1500 Free']
            e=c['1500 Free']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '1500 Free' in b:
            d=b['1500 Free']
            e=c['1500 Free']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '1500 Free' in b:
            d=b['1500 Free']
            e=c['1500 Free']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '1500 Free' in b:
            d=b['1500 Free']
            e=c['1500 Free']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

def Fly50():
    event = tk.Toplevel()
    event.geometry("720x600") 
    event.title('50 Fly Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='50 FLY TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '50 Fly' in b:
            d=b['50 Fly']
            e=c['50 Fly']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '50 Fly' in b:
            d=b['50 Fly']
            e=c['50 Fly']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '50 Fly' in b:
            d=b['50 Fly']
            e=c['50 Fly']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '50 Fly' in b:
            d=b['50 Fly']
            e=c['50 Fly']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '50 Fly' in b:
            d=b['50 Fly']
            e=c['50 Fly']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '50 Fly' in b:
            d=b['50 Fly']
            e=c['50 Fly']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '50 Fly' in b:
            d=b['50 Fly']
            e=c['50 Fly']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '50 Fly' in b:
            d=b['50 Fly']
            e=c['50 Fly']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

def Fly100():
    event = tk.Toplevel()
    event.geometry("720x600")
    event.title('100 Fly Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='100 FLY TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '100 Fly' in b:
            d=b['100 Fly']
            e=c['100 Fly']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '100 Fly' in b:
            d=b['100 Fly']
            e=c['100 Fly']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '100 Fly' in b:
            d=b['100 Fly']
            e=c['100 Fly']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '100 Fly' in b:
            d=b['100 Fly']
            e=c['100 Fly']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '100 Fly' in b:
            d=b['100 Fly']
            e=c['100 Fly']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '100 Fly' in b:
            d=b['100 Fly']
            e=c['100 Fly']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '100 Fly' in b:
            d=b['100 Fly']
            e=c['100 Fly']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '100 Fly' in b:
            d=b['100 Fly']
            e=c['100 Fly']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)  

def Fly200():
    event = tk.Toplevel()
    event.geometry("720x600")
    event.title('200 Fly Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='200 FLY TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '200 Fly' in b:
            d=b['200 Fly']
            e=c['200 Fly']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '200 Fly' in b:
            d=b['200 Fly']
            e=c['200 Fly']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '200 Fly' in b:
            d=b['200 Fly']
            e=c['200 Fly']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '200 Fly' in b:
            d=b['200 Fly']
            e=c['200 Fly']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '200 Fly' in b:
            d=b['200 Fly']
            e=c['200 Fly']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '200 Fly' in b:
            d=b['200 Fly']
            e=c['200 Fly']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '200 Fly' in b:
            d=b['200 Fly']
            e=c['200 Fly']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '200 Fly' in b:
            d=b['200 Fly']
            e=c['200 Fly']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)  

def Back50():
    event = tk.Toplevel()
    event.geometry("720x600") 
    event.title('50 Back Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='50 BACK TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '50 Back' in b:
            d=b['50 Back']
            e=c['50 Back']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '50 Back' in b:
            d=b['50 Back']
            e=c['50 Back']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '50 Back' in b:
            d=b['50 Back']
            e=c['50 Back']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '50 Back' in b:
            d=b['50 Back']
            e=c['50 Back']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '50 Back' in b:
            d=b['50 Back']
            e=c['50 Back']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '50 Back' in b:
            d=b['50 Back']
            e=c['50 Back']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '50 Back' in b:
            d=b['50 Back']
            e=c['50 Back']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '50 Back' in b:
            d=b['50 Back']
            e=c['50 Back']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

def Back100():
    event = tk.Toplevel()
    event.geometry("720x600")
    event.title('100 Back Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='100 BACK TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '100 Back' in b:
            d=b['100 Back']
            e=c['100 Back']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '100 Back' in b:
            d=b['100 Back']
            e=c['100 Back']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '100 Back' in b:
            d=b['100 Back']
            e=c['100 Back']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '100 Back' in b:
            d=b['100 Back']
            e=c['100 Back']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '100 Back' in b:
            d=b['100 Back']
            e=c['100 Back']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '100 Back' in b:
            d=b['100 Back']
            e=c['100 Back']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '100 Back' in b:
            d=b['100 Back']
            e=c['100 Back']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '100 Back' in b:
            d=b['100 Back']
            e=c['100 Back']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)  

def Back200():
    event = tk.Toplevel()
    event.geometry("720x600")
    event.title('200 Back Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='200 BACK TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '200 Back' in b:
            d=b['200 Back']
            e=c['200 Back']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '200 Back' in b:
            d=b['200 Back']
            e=c['200 Back']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '200 Back' in b:
            d=b['200 Back']
            e=c['200 Back']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '200 Back' in b:
            d=b['200 Back']
            e=c['200 Back']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '200 Back' in b:
            d=b['200 Back']
            e=c['200 Back']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '200 Back' in b:
            d=b['200 Back']
            e=c['200 Back']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '200 Back' in b:
            d=b['200 Back']
            e=c['200 Back']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '200 Back' in b:
            d=b['200 Back']
            e=c['200 Back']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

def Breast50():
    event = tk.Toplevel()
    event.geometry("720x600") 
    event.title('50 Breast Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='50 BREAST TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '50 Breast' in b:
            d=b['50 Breast']
            e=c['50 Breast']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '50 Breast' in b:
            d=b['50 Breast']
            e=c['50 Breast']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '50 Breast' in b:
            d=b['50 Breast']
            e=c['50 Breast']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '50 Breast' in b:
            d=b['50 Breast']
            e=c['50 Breast']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '50 Breast' in b:
            d=b['50 Breast']
            e=c['50 Breast']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '50 Breast' in b:
            d=b['50 Breast']
            e=c['50 Breast']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '50 Breast' in b:
            d=b['50 Breast']
            e=c['50 Breast']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '50 Breast' in b:
            d=b['50 Breast']
            e=c['50 Breast']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)  

def Breast100():
    event = tk.Toplevel()
    event.geometry("720x600")
    event.title('100 Breast Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='100 BREAST TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '100 Breast' in b:
            d=b['100 Breast']
            e=c['100 Breast']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '100 Breast' in b:
            d=b['100 Breast']
            e=c['100 Breast']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '100 Breast' in b:
            d=b['100 Breast']
            e=c['100 Breast']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '100 Breast' in b:
            d=b['100 Breast']
            e=c['100 Breast']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '100 Breast' in b:
            d=b['100 Breast']
            e=c['100 Breast']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '100 Breast' in b:
            d=b['100 Breast']
            e=c['100 Breast']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '100 Breast' in b:
            d=b['100 Breast']
            e=c['100 Breast']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '100 Breast' in b:
            d=b['100 Breast']
            e=c['100 Breast']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)  

def Breast200():
    event = tk.Toplevel()
    event.geometry("720x600")
    event.title('200 Breast Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='200 BREAST TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '200 Breast' in b:
            d=b['200 Breast']
            e=c['200 Breast']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '200 Breast' in b:
            d=b['200 Breast']
            e=c['200 Breast']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '200 Breast' in b:
            d=b['200 Breast']
            e=c['200 Breast']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '200 Breast' in b:
            d=b['200 Breast']
            e=c['200 Breast']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '200 Breast' in b:
            d=b['200 Breast']
            e=c['200 Breast']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '200 Breast' in b:
            d=b['200 Breast']
            e=c['200 Breast']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '200 Breast' in b:
            d=b['200 Breast']
            e=c['200 Breast']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '200 Breast' in b:
            d=b['200 Breast']
            e=c['200 Breast']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)  

def IM100():
    event = tk.Toplevel()
    event.geometry("720x600")
    event.title('100 IM Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='100 IM TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '100 IM' in b:
            d=b['100 IM']
            e=c['100 IM']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '100 IM' in b:
            d=b['100 IM']
            e=c['100 IM']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '100 IM' in b:
            d=b['100 IM']
            e=c['100 IM']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '100 IM' in b:
            d=b['100 IM']
            e=c['100 IM']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '100 IM' in b:
            d=b['100 IM']
            e=c['100 IM']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '100 IM' in b:
            d=b['100 IM']
            e=c['100 IM']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '100 IM' in b:
            d=b['100 IM']
            e=c['100 IM']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '100 IM' in b:
            d=b['100 IM']
            e=c['100 IM']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)  

def IM200():
    event = tk.Toplevel()
    event.geometry("720x600")
    event.title('200 IM Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='200 IM TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '200 IM' in b:
            d=b['200 IM']
            e=c['200 IM']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '200 IM' in b:
            d=b['200 IM']
            e=c['200 IM']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '200 IM' in b:
            d=b['200 IM']
            e=c['200 IM']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '200 IM' in b:
            d=b['200 IM']
            e=c['200 IM']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '200 IM' in b:
            d=b['200 IM']
            e=c['200 IM']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '200 IM' in b:
            d=b['200 IM']
            e=c['200 IM']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '200 IM' in b:
            d=b['200 IM']
            e=c['200 IM']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '200 IM' in b:
            d=b['200 IM']
            e=c['200 IM']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)  

def IM400():
    event = tk.Toplevel()
    event.geometry("720x600") 
    event.title('400 IM Top Times')
    btn2 = tk.Button(event,text='BACK',command=event.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(event,text='400 IM TOP TIMES',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)

    dict10={}
    for j in range (0,len(p1)):
        a=p1[j].name
        b=p1[j].eventfloat
        c=p1[j].eventstr
        
        if '400 IM' in b:
            d=b['400 IM']
            e=c['400 IM']
            dict10[a]=[d,e]
    SortDict10=sorted(dict10.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Girls',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict10)):
        y+=0.03
        label=tk.Label(event,text=SortDict10[i][0])
        label1=tk.Label(event,text=SortDict10[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)

    
    dict11={}
    for j in range (0,len(p2)):
        a=p2[j].name
        b=p2[j].eventfloat
        c=p2[j].eventstr
        
        if '400 IM' in b:
            d=b['400 IM']
            e=c['400 IM']
            dict11[a]=[d,e]
    SortDict11=sorted(dict11.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict11)):
        y+=0.03
        label=tk.Label(event,text=SortDict11[i][0])
        label1=tk.Label(event,text=SortDict11[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict13={}
    for j in range (0,len(p3)):
        a=p3[j].name
        b=p3[j].eventfloat
        c=p3[j].eventstr
        
        if '400 IM' in b:
            d=b['400 IM']
            e=c['400 IM']
            dict13[a]=[d,e]
    SortDict13=sorted(dict13.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict13)):
        y+=0.03
        label=tk.Label(event,text=SortDict13[i][0])
        label1=tk.Label(event,text=SortDict13[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)
    
    
    dict15={}
    for j in range (0,len(p4)):
        a=p4[j].name
        b=p4[j].eventfloat
        c=p4[j].eventstr
        
        if '400 IM' in b:
            d=b['400 IM']
            e=c['400 IM']
            dict15[a]=[d,e]
    SortDict15=sorted(dict15.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Girls',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.2,rely=y)
    for i in range (0,len(SortDict15)):
        y+=0.03
        label=tk.Label(event,text=SortDict15[i][0])
        label1=tk.Label(event,text=SortDict15[i][1][1])
        label.place(relx=0.2,rely=y)
        label1.place(relx=0.4,rely=y)


    dict10B={}
    for j in range (0,len(p5)):
        a=p5[j].name
        b=p5[j].eventfloat
        c=p5[j].eventstr
        
        if '400 IM' in b:
            d=b['400 IM']
            e=c['400 IM']
            dict10B[a]=[d,e]
    SortDict10B=sorted(dict10B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='10 & Under Boys',font='Helvetica 10 underline')
    y=0.03
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict10B)):
        y+=0.03
        label=tk.Label(event,text=SortDict10B[i][0])
        label1=tk.Label(event,text=SortDict10B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)

    
    dict11B={}
    for j in range (0,len(p6)):
        a=p6[j].name
        b=p6[j].eventfloat
        c=p6[j].eventstr
        
        if '400 IM' in b:
            d=b['400 IM']
            e=c['400 IM']
            dict11B[a]=[d,e]
    SortDict11B=sorted(dict11B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='11-12 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict11B)):
        y+=0.03
        label=tk.Label(event,text=SortDict11B[i][0])
        label1=tk.Label(event,text=SortDict11B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


    dict13B={}
    for j in range (0,len(p7)):
        a=p7[j].name
        b=p7[j].eventfloat
        c=p7[j].eventstr
        
        if '400 IM' in b:
            d=b['400 IM']
            e=c['400 IM']
            dict13B[a]=[d,e]
    SortDict13B=sorted(dict13B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='13-14 Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict13B)):
        y+=0.03
        label=tk.Label(event,text=SortDict13B[i][0])
        label1=tk.Label(event,text=SortDict13B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)
    
    
    dict15B={}
    for j in range (0,len(p8)):
        a=p8[j].name
        b=p8[j].eventfloat
        c=p8[j].eventstr
        
        if '400 IM' in b:
            d=b['400 IM']
            e=c['400 IM']
            dict15B[a]=[d,e]
    SortDict15B=sorted(dict15B.items(),key=lambda x:x[1],reverse=False)
    label=tk.Label(event,text='15 & Over Boys',font='Helvetica 10 underline')
    y+=0.06
    label.place(relx=0.6,rely=y)
    for i in range (0,len(SortDict15B)):
        y+=0.03
        label=tk.Label(event,text=SortDict15B[i][0])
        label1=tk.Label(event,text=SortDict15B[i][1][1])
        label.place(relx=0.6,rely=y)
        label1.place(relx=0.8,rely=y)


def TopTimes():
    toptimes = tk.Toplevel()
    toptimes.geometry("1000x520") 
    toptimes.title('Top Times By Event')
    btn2 = tk.Button(toptimes,text='HOME',command=toptimes.destroy)
    btn2.grid(row=0,column=0)
    Tlabel=tk.Label(toptimes,text='TOP TIMES BY EVENT',font='Helvetica 12')
    Tlabel.place(relx=0.45,rely=0)
    Fr50 = tk.Button(toptimes,text='50 Free',width=20,height=10,command=Free50)
    Fr50.grid(row=2,column=1)
    Fr100 = tk.Button(toptimes,text='100 Free',width=20,height=10,command=Free100)
    Fr100.grid(row=3,column=1)
    Fr200 = tk.Button(toptimes,text='200 Free',width=20,height=10,command=Free200)
    Fr200.grid(row=4,column=1)
    Fr400 = tk.Button(toptimes,text='400 Free',width=20,height=10,command=Free400)
    Fr400.grid(row=2,column=2)
    Fr800 = tk.Button(toptimes,text='800 Free',width=20,height=10,command=Free800)
    Fr800.grid(row=3,column=2)
    Fr1500 = tk.Button(toptimes,text='1500 Free',width=20,height=10,command=Free1500)
    Fr1500.grid(row=4,column=2)
    Fl50 = tk.Button(toptimes,text='50 Fly',width=20,height=10,command=Fly50)
    Fl50.grid(row=2,column=3)
    Fl100 = tk.Button(toptimes,text='100 Fly',width=20,height=10,command=Fly100)
    Fl100.grid(row=3,column=3)
    Fl200 = tk.Button(toptimes,text='200 Fly',width=20,height=10,command=Fly200)
    Fl200.grid(row=4,column=3)
    Ba50 = tk.Button(toptimes,text='50 Back',width=20,height=10,command=Back50)
    Ba50.grid(row=2,column=4)
    Ba100 = tk.Button(toptimes,text='100 Back',width=20,height=10,command=Back100)
    Ba100.grid(row=3,column=4)
    Ba200 = tk.Button(toptimes,text='200 Back',width=20,height=10,command=Back200)
    Ba200.grid(row=4,column=4)
    Br50 = tk.Button(toptimes,text='50 Breast',width=20,height=10,command=Breast50)
    Br50.grid(row=2,column=5)
    Br100 = tk.Button(toptimes,text='100 Breast',width=20,height=10,command=Breast100)
    Br100.grid(row=3,column=5)
    Br200 = tk.Button(toptimes,text='200 Breast',width=20,height=10,command=Breast200)
    Br200.grid(row=4,column=5)
    Im100 = tk.Button(toptimes,text='100 IM',width=20,height=10,command=IM100)
    Im100.grid(row=2,column=6)
    Im200 = tk.Button(toptimes,text='200 IM',width=20,height=10,command=IM200)
    Im200.grid(row=3,column=6)
    Im400 = tk.Button(toptimes,text='400 IM',width=20,height=10,command=IM400)
    Im400.grid(row=4,column=6)
    

bt1=tk.Button(root,text='ROSTER',width=50,height=20,command=ROSTER)
bt1.grid(row=0,column=0)
bt2=tk.Button(root,text='TOP TIMES BY EVENT',width=50,height=20,command=TopTimes)
bt2.grid(row=0,column=1)


root.mainloop()
