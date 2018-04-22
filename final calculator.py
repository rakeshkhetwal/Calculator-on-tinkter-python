#Rakesh kumar khetwal
#On button not in use sorry
import tkinter as tk #creating alias of tkinter
from tkinter import font
x=[]
class MyUI(tk.Frame):  #tk.frame is predefined class and acting as a base class
    def __init__(self,master=None): # here master and self are not the the argumentt taken from the base class tk.Frame 
        super().__init__(master) # here the __init__() is a function inside the tk.Frame base class
        self.pack() # render or create the frame , where pack is in-built function
        self.create_widgets()
        
    def nik(self,tex,tv,his):
       
        return lambda : self.calc(tex,tv,his)

    def calc(self,tex,tv,his):
      tex.insert(tk.END, tv)
      if tv.find('DEL')!=-1:
           his.insert(tk.END,'\n')
      elif tv.find('AC')!=-1:
           his.insert(tk.END,'\n')
      else:
           his.insert(tk.END,tv)
      
     
      x.append(tv)      
      y=''.join(x)   # for concatenating the list into single string
      try:  
        if y.find('=')!=-1:
            tex.delete('1.0', tk.END)
            y=y.replace('=','')
            y=y.replace('Ans','')
            if y.find("/")!=-1:           
                s=y.split('/')
                z=len(s)
                print(z)
                if float(s[1])!=0.0:
                    suma=float(s[0])/float(s[1])
                    tex.insert(tk.END, suma)
                    suma=float(suma)
                    his.insert(tk.END,suma)
                    his.insert(tk.END,'\n')
                    suma=str(suma)
                    print("Division of nos",suma)
                    x[:]=[]
                    x.append(suma)
                else:
                    his.insert(tk.END,'Math error')
                    tex.insert(tk.END,'Math error')
            
            elif y.find("X")!=-1:  # for multiplication
                suma=1
               
                s=y.split('X')
                
                z=len(s)
                print(z)
                for i in range(0,z):
                    suma=suma*float(s[i])
                tex.insert(tk.END, suma)
                print("multiplication of nos",suma)
                suma=float(suma)
                his.insert(tk.END,suma)
                his.insert(tk.END,'\n')
                suma=str(suma)
                x[:]=[]
                x.append(suma)

            elif y.find("+")!=-1:   # for addition
                suma=0
               
                s=y.split('+')
               
                z=len(s)
                print(z)
                for i in range(0,z):
                    suma=suma+float(s[i])
                tex.insert(tk.END, suma)
                print("sum of nos",suma)
                suma=float(suma)
                his.insert(tk.END,suma)
                his.insert(tk.END,'\n')
                suma=str(suma)
                x[:]=[]
                x.append(suma)

            elif y.find("-")!=-1:
                s=y.split('-')
                z=len(s)
                print(z)
                suma=float(s[0])-float(s[1])
                tex.insert(tk.END, suma)
                print("subtraction of nos",suma)
                suma=float(suma)
                his.insert(tk.END,suma)
                his.insert(tk.END,'\n')
                suma=str(suma)
                x[:]=[]
                x.append(suma)
          
        elif y.find("DEL")!=-1:  # for deletion
            x[:]=[]
            tex.delete('1.0', tk.END)
            return
        
        elif y.find("AC")!=-1:  # for deletion
            x[:]=[]
            tex.delete('1.0', tk.END)
            return
        
      except:
          None
          
    def create_widgets(self): # for creating wizards
        # can't use grid and pack in same function
        h =font.Font(family='Helvetica', size=36, weight=font.BOLD)# here Font is a function inbuilt inside the from tkinter import font and font is a function inside tinkter
        #making of text box
        cc=font.Font(family='Helvetica', size=20, weight=font.BOLD)
        xx=font.Font(family='Helvetica', size=25, weight=font.BOLD)
        self.shows=tk.Text(self,width=21,font=xx,height=1,fg='black',bg='light blue')
        self.shows.insert(tk.END,'Rakesh Kumar Khetwal')
        self.shows.grid(row=0,column=5)
        #Output Box
        self.show = tk.Text(self,width=25,height=1.5,bg='brown',fg='white',font=cc)        
        self.show.grid(row=3, column=5,rowspan=5,columnspan=5)
        # Histroy box
        self.his=tk.Text(self,width=15,height=7,bg='brown',fg='white',font=cc)
        self.his.grid(row=0,column=5,rowspan=5,columnspan=7)
        self.his.insert(tk.END,"-------Histroy-------")
        
        #For creating the buttons
        self.a = tk.Button(self,text="7",fg="white",bg="black",font=h,height=0,width=0)
        tv=self.a["text"]
        self.a["command"] = self.nik(self.show,tv,self.his)
        self.a.grid(column=0, row=0,padx=(2,2),pady=(2,2))

        #Unsuccessful attempts  for inputing the value inside the text inside gui frame
        #self.a["command"]=self.extract(tv)
        # xx=self.show.insert(tk.END,self.a['text'])
        # self.a["command"] = print(self.a['text'])
        #self.a.bind('<Button-1>', y.insert(tk.END,gg))
        #self.show['text']="7";
        #self.show.insert('1.0','vv')
        
        self.b = tk.Button(self,text="8",fg="white",bg="black",font=h)
        tv=self.b["text"]
        self.b["command"] = self.nik(self.show,tv,self.his)
        self.b.grid(column=1, row=0,padx=(2,2),pady=(2,2))
        
        self.c = tk.Button(self,text="9",fg="white",bg="black",font=h)
        tv=self.c["text"]
        self.c["command"] = self.nik(self.show,tv,self.his)
        self.c.grid(column=2, row=0,padx=(2,2),pady=(2,2))

        self.k = tk.Button(self,text="DEL",fg="white",bg="red",font=h,width=4)
        tv=self.k["text"]
        self.k["command"] = self.nik(self.show,tv,self.his)
        self.k.grid(column=3, row=0,padx=(2,2),pady=(2,2))

        self.l = tk.Button(self,text="AC",fg="white",bg="red",font=h,width=4)        
        tv=self.l["text"]
        self.l["command"] = self.nik(self.show,tv,self.his)
        self.l.grid(column=4, row=0,padx=(2,2),pady=(2,2))

        self.d = tk.Button(self,text="4",fg="white",bg="black",font=h)
        tv=self.d["text"]
        self.d["command"] = self.nik(self.show,tv,self.his)
        self.d.grid(column=0, row=1,padx=(2,2),pady=(2,2))
        
        self.e = tk.Button(self,text="5",fg="white",bg="black",font=h)
        tv=self.e["text"]
        self.e["command"] = self.nik(self.show,tv,self.his)
        self.e.grid(column=1, row=1,padx=(2,2),pady=(2,2))   

        self.f = tk.Button(self,text="6",fg="white",bg="black",font=h)
        tv=self.f["text"]
        self.f["command"] = self.nik(self.show,tv,self.his)
        self.f.grid(column=2, row=1,padx=(2,2),pady=(2,2))

        self.m = tk.Button(self,text="X",fg="white",bg="light green",font=h,width=4)       
        tv=self.m["text"]
        self.m["command"] = self.nik(self.show,tv,self.his)
        self.m.grid(column=3, row=1,padx=(2,2),pady=(2,2))

        self.n = tk.Button(self,text="/",fg="white",bg="light green",font=h,width=4)    
        tv=self.n["text"]
        self.n["command"] = self.nik(self.show,tv,self.his)
        self.n.grid(column=4, row=1,padx=(2,2),pady=(2,2))

        self.g = tk.Button(self,text="1",fg="white",bg="black",font=h)        
        tv=self.g["text"]
        self.g["command"] = self.nik(self.show,tv,self.his)
        self.g.grid(column=0, row=2,padx=(2,2),pady=(2,2))
       
        self.h = tk.Button(self,text="2",fg="white",bg="black",font=h)
        tv=self.h["text"]
        self.h["command"] = self.nik(self.show,tv,self.his)
        self.h.grid(column=1, row=2,padx=(2,2),pady=(2,2))

        self.i = tk.Button(self,text="3",fg="white",bg="black",font=h)   
        tv=self.i["text"]
        self.i["command"] = self.nik(self.show,tv,self.his)
        self.i.grid(column=2, row=2,padx=(2,2),pady=(2,2))

        self.o = tk.Button(self,text="+",fg="white",bg="light green",font=h,width=4)  
        tv=self.o["text"]
        self.o["command"] = self.nik(self.show,tv,self.his)
        self.o.grid(column=3, row=2,padx=(2,2),pady=(2,2))

        self.p = tk.Button(self,text="-",fg="white",bg="light green",font=h,width=4) 
        tv=self.p["text"]
        self.p["command"] = self.nik(self.show,tv,self.his)
        self.p.grid(column=4, row=2,padx=(2,2),pady=(2,2))

        self.q = tk.Button(self,text="0",fg="white",bg="black",font=h)    
        tv=self.q["text"]
        self.q["command"] = self.nik(self.show,tv,self.his)
        self.q.grid(column=0, row=3,padx=(2,2),pady=(2,2))

        z =font.Font(family='Helvetica', size=36, weight=font.BOLD)
        self.r = tk.Button(self,text=".",fg="white",bg="black",font=z,width=2)
        tv=self.r["text"]
        self.r["command"] = self.nik(self.show,tv,self.his)
        self.r.grid(column=1, row=3,padx=(2,2),pady=(2,2))    

        self.t = tk.Button(self,text="=",fg="white",bg="orange",font=h)   
        self.t.grid(column=2, row=3,padx=(2,2),pady=(2,2))
        tv=self.t["text"]
        self.t["command"] = self.nik(self.show,tv,self.his)
        
        self.u = tk.Button(self,text="Ans",fg="white",bg="orange",font=h,width=4)  
        tv=self.u["text"]
        self.u["command"] = self.nik(self.show,tv,self.his)
        self.u.grid(column=3, row=3,padx=(2,2),pady=(2,2))

        self.w = tk.Button(self,text="ON",fg="white",bg="brown",font=h,width=4)  
        tv=self.w["text"]
        self.w["command"] = self.nik(self.show,tv,self.his)
        self.w.grid(column=4, row=3,padx=(2,2),pady=(2,2))

root = tk.Tk() # create frame
app = MyUI(master=root)  #master here is used to for storing the layouts after each function basically 
app.mainloop()
