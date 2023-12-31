# Parcial 2 fisica 3
# descripcion: Realice una interfaz grafica para obtener propiedades físicas de tres tipos de capacitores de placas paralelas (placas paralelas, capacitor esferico, capacitor de cilintros)
# autores:  Francis Aguilar #222432
#           Angela García   #22869
# recursos: python 3.10
# fecha de entrega: 30/10/2023
# sin modificaciones

# librerias:
from tkinter import * 
from tkinter import messagebox
from math import sin, cos, tan 
from math import pi
from math import log
from tkinter.ttk import Combobox 
from PIL import Image, ImageTk
import requests
from io import BytesIO
"""
ATENCION: antes de correr el programa asegurese de tener instaladas las librerias: 
-  PIL 
-  requests

"""

Electrodomesticos={
    #llave, valor:link imagen
    "microondas":"https://th.bing.com/th/id/OIP.fqUI18B-s9vlRY5p8Zs4SgHaEi?pid=ImgDet&rs=1",
    "refrigerador":"https://th.bing.com/th/id/R.2ccb7bd5e5eeb40eb0950630508b94a7?rik=1jrtsNckPHUM%2fw&pid=ImgRaw&r=0",
    "television":"https://th.bing.com/th/id/R.0d7a0df3fc3ed1d85494bd2713439749?rik=Xc9%2fpl%2brKqqI5g&riu=http%3a%2f%2fimage.made-in-china.com%2f2f0j00AjiEFlwGLVbp%2f-Televisi-n-barata-de-la-pulgada-LED-de-la-.jpg&ehk=Lm4CZyNY70guM4ImBEOMmf2IczCeWTPkVbPYyRdQ8K4%3d&risl=&pid=ImgRaw&r=0",
    "computadora":"https://th.bing.com/th/id/R.c9d717f747f9154f668484dfb1d4d8c8?rik=O8ncJ4VtTb%2bBqQ&riu=http%3a%2f%2fwww.solutekcolombia.com%2fimages%2fcomputadores_escritorio_hp.jpeg&ehk=UVNk23buwNZ4Sv6kcbOHjuowbZFQjjskUyutGWycY4c%3d&risl=&pid=ImgRaw&r=0",
    "plancha":"https://images-na.ssl-images-amazon.com/images/I/41M7o%2B5wMFL.__AC_SY300_QL70_ML2_.jpg",
    "licuadora":"https://th.bing.com/th/id/R.cfc3f9be1bd380baa81cdff134477580?rik=p30RKe2Gf%2fAQQA&pid=ImgRaw&r=0",
    "horno":"https://th.bing.com/th/id/R.1f3acd3e602e4509c20068b11f9b0a6c?rik=%2fDbe9jJcwLu9oQ&pid=ImgRaw&r=0",
    "lavadora":"https://th.bing.com/th/id/OIP._9pbFZ835-fD8lUIbd0IlgHaHa?pid=ImgDet&rs=1",
    "secadora":"https://th.bing.com/th/id/OIP.lQB-mm9cUTH3Bz3NEgpAIAHaHa?pid=ImgDet&rs=1",
    "lavavajillas":"https://th.bing.com/th/id/OIP.LfSxYqmTDND2YPbCHiT2wQHaHa?pid=ImgDet&rs=1",
    "freidora":"https://freidoraelectrica.com/wp-content/uploads/2021/03/freidora-de-aire-caliente.jpg",
    "wafflera":"https://th.bing.com/th/id/R.738d8df1afc0d58fa5ccfca04f710938?rik=deFNKQ8fMVUZQw&pid=ImgRaw&r=0",
    "ventilador":"https://th.bing.com/th/id/OIP.nQ6zkOoHGNc-eR-vRNAw5gHaHa?pid=ImgDet&rs=1",
    "consola de videojuegos":"https://th.bing.com/th/id/R.cc10af6236fc6614b6b53b2382638a1b?rik=Yx6qyxqUR%2fnbhg&riu=http%3a%2f%2fupload.wikimedia.org%2fwikipedia%2fcommons%2f8%2f83%2fWii_console.png&ehk=OduJYQa3O8BYVDptaLGwtyoWDwsd0Y6jJATbQHCgAa0%3d&risl=1&pid=ImgRaw&r=0",
    "radio":"https://th.bing.com/th/id/R.572cc6dd12c5f9223b2682665c5032c6?rik=9wmdtFM%2bEIyfeg&riu=http%3a%2f%2fpds.exblog.jp%2fpds%2f1%2f200905%2f13%2f69%2fe0136669_21463089.jpg&ehk=rm6Buvntngc28QNxdYCQZ5rsiCQX3t3lON8jLfuzjvE%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1",
    "estufa":"https://images-na.ssl-images-amazon.com/images/I/8166LaMpUOL._AC_SL1500_.jpg",
    "congelador":"https://th.bing.com/th/id/OIP.Aru-wNBym3XH_-POnxAgvAHaHa?pid=ImgDet&rs=1",
    "camara":"https://eldiariony.com/wp-content/uploads/sites/2/2020/03/alan-j-hendry-knt4zd8hpb0-unsplash.jpg?quality=80&strip=all",
    "aspiradora":"https://th.bing.com/th/id/R.17cfcae4d8e6add93cdaab6c78260d14?rik=Q%2b3vQ3cSP%2fMM7w&pid=ImgRaw&r=0",
    "cafetera":"https://th.bing.com/th/id/OIP.OX9HyLxM8Av1gfxqebpnOwHaHa?pid=ImgDet&rs=1"

}

listaDispositivos=[]
llaves=[]




class app(Tk):
    def __init__(self): 
        Tk.__init__(self)
        self._root = Frame() #crea el frame principal
        self.geometry("1400x1400")
        self.title("🤑 Parcial 3 🤑")
        self.config(bg="#ffafcc")
        self.l=Label(text=" Elija un dispositivo: ");self.l.place(x=20,y=20); self.l.config(bg="#ffc2d1")
        self.caja = Combobox(self, state="readonly",values=["microondas", "refrigerador", "television","computadora","plancha","licuadora","horno","lavadora","secadora","lavavajillas","freidora","wafflera","ventilador","consola de videojuegos","radio","estufa","congelador","camara","aspiradora","cafetera"], width=20)
        self.caja.place(x=20, y =50)

        self.dispexist = False
        #objetos

        self.l1=Label(self,text="Potencia del dispositivo(w):");self.l1.place(x=10,y=90); self.l1.config(bg="#ffc2d1")
        self.e1=Entry(self);self.e1.place(x=160,y=90)

        self.l2=Label(self,text="corriente (A):");self.l2.place(x=10,y=130); self.l2.config(bg="#ffddd2")
        self.e2=Entry(self);self.e2.place(x=160,y=130)

        self.l3=Label(self,text="voltaje (v):");self.l3.place(x=10,y=170); self.l3.config(bg="#ff8fab")
        self.e3=Entry(self);self.e3.place(x=160,y=170)

        self.l4=Label(self,text="horas de uso (h):");self.l4.place(x=10,y=210); self.l4.config(bg="#f08080")
        self.e4=Entry(self);self.e4.place(x=160,y=210)

        self.l5=Label(self,text="longitud del cable(mismo en todos):");self.l5.place(x=300,y=20); self.l5.config(bg="#f08080")
        self.e5=Entry(self);self.e5.place(x=300,y=50)
        
        self.btn1= Button(self, text="agregar dispositivo", width=35,command=self.AgregarDispositivo, bg="#ffc2d1");self.btn1.place(x=550,y=10)
        self.btn2= Button(self, text="diametro minimo y energia a pagar", width=35,command=self.calcular, bg="#ffb3c6");self.btn2.place(x=550,y=40)
        self.btn3= Button(self, text="graficar", width=35,command=self.graficar, bg="#ff8fab");self.btn3.place(x=550,y=70)       
        self.btn4= Button(self, text="limpiar canvas", width=35,command=self.limpiar, bg="#ff8fab");self.btn4.place(x=550,y=100)       
        
        #self.l5=Label(self, text="");self.l5.place(x=10,y=290); self.l5.config(bg="#ff8fab")
        self.l6=Label(self, text="energia total");self.l6.place(x=10,y=320); self.l6.config(bg="#ffc2d1")
        self.l7=Label(self, text="");self.l7.place(x=10,y=350); self.l7.config(bg="#ff8fab")
        self.l8=Label(self, text="");self.l8.place(x=10,y=390); self.l8.config(bg="#ffc2d1")
        self.l10=Label(self, text="");self.l10.place(x=10,y=430); self.l10.config(bg="#ff8fab")
        
        self.l11=Label(self, text="Lista de dispositivos");self.l11.place(x=280,y=320); self.l11.config(bg="#ff8fab")
        self.l12=Label(self, text="");self.l12.place(x=280,y=350); self.l12.config(bg="#ffc2d1")

        self.l13=Label(self, text="");self.l13.place(x=10,y=550); self.l13.config(bg="#ff8fab")
        self.l14=Label(self, text="");self.l14.place(x=10,y=590); self.l14.config(bg="#ffc2d1")
        self.l15=Label(self, text="");self.l15.place(x=10,y=630); self.l15.config(bg="#ff8fab")
        self.l16=Label(self, text="");self.l16.place(x=10,y=670); self.l16.config(bg="#ffc2d1")
        self.l17=Label(self, text="");self.l17.place(x=10,y=710); self.l17.config(bg="#ff8fab")

        self.energiaTotal=0
        self.Imax = 0 
        self.DispMasGaston = ""
        self.masV = 0 
        self.diametro = 0
        self.contador= 0

        # Crear una lista para guardar las imágenes
        self.imagenes = []

        #canvas
        self.c1 = Canvas(self, width=800, height=500, bg="white")
        self.c1.place(x=450, y=150)
        self.c1.config(bg="misty rose")

  


    def AgregarDispositivo(self):
        
        
       # try:
            #obtener los datos del dispositivo y del cable
            self.dispexist = True
            self.nombre= str(self.caja.get())
            self.potencia= float(self.e1.get())
            self.corriente= float(self.e2.get())
            self.voltaje= float(self.e3.get())
            self.horas= float(self.e4.get())
            
            if (self.horas > 0 ):
                
                #verificar que la lista no pase de 10 dispositivos
                if len(listaDispositivos)>9:
                    messagebox.showerror("error","Se ha superado el limite de dispositivos")

                #agregar a la lista
                else:
                    #calculos, para luego agregarlo al diccionario
                    
                    self.costoHora= 1.47 # por kw
                    self.tiempo= (30)*(self.horas) # tiempo por mes
                    self.energia=(self.potencia* self.tiempo)/1000

                    #creamos un diccionario con todos los valores 
                    dict={}
                    dict["nombre"]= self.nombre
                    dict["potencia"]=self.potencia
                    dict["corriente"]=self.corriente
                    dict["voltaje"]=self.voltaje
                    dict["horas"]=self.horas
                    dict["energia"]=self.energia
            
                    #sumar a la energia todal la energia agregada
                    self.energiaTotal += self.energia
                    self.l7.config(text=str(self.energiaTotal))
                    self.l8.config(text="Gasto total Baja tensión simple")
                    self.l10.config(text=str(self.energiaTotal/1000*self.tiempo*self.costoHora)+" Q")

                    # que disp gasta mas 
                    if self.corriente > self.Imax: 
                        self.Imax = self.corriente 
                        self.DispMasGaston = self.nombre
                        self.masV = self.voltaje

                    print(self.energiaTotal)
                    
                    messagebox.showinfo("atencion","se agrego dispositivo")

                    #borrar valores del entry
                    self.e1.insert(0,"")
                    self.e2.insert(0,"")
                    self.e3.insert(0,"")
                
                    #agregamos al final de la lista
                    listaDispositivos.append(dict)
                    llaves.append(self.nombre)
                    print(listaDispositivos)
                    print(llaves)
                   
                    
                    #mostrar en pantalla los dispositivos
                    for i in range(len(llaves)): 
                        self.lt = Label(self, text =llaves[i]); self.lt.place(x = 280 , y = 360+ i*30);self.lt.config(bg="#ff8fab")
                
                

            else: 
                messagebox.showerror("Error", "Ingrese valores validos para la distancia y longitud")
        #except Exception as msg: 
        #    messagebox.showerror("error", "asegurese de ingresar un número válido y todos los valores ")


                       
    def calcular(self):
        self.largo = float(self.e5.get())
           
        if(self.dispexist):
            if(self.largo>0):
                self.diametro = 2*(((self.Imax*1.72e-8*self.largo)/(pi*self.masV))**1/2)
                print(self.diametro )
                if self.diametro > 0.519: 
                    messagebox.showinfo("Info","El Calibre recomendado para evitar cualquier mal funcionamiento es de: 4")

                if self.diametro > 0.462 and self.diametro < 0.519:
                    messagebox.showinfo("Info","El calibre recomendado para evitar cualquier mal funcionamiento es de: 5")

                if self.diametro > 0.412 and self.diametro < 0.462:
                    messagebox.showinfo("Info","El calibre recomendado para evitar cualquier mal funcionamiento es de: 6")
            
                if self.diametro > 0.326 and self.diametro < 0.412:
                    messagebox.showinfo("Info","El calibre recomendado para evitar cualquier mal funcionamiento es de: 8")

                if self.diametro > 0.259 and self.diametro < 0.326:
                    messagebox.showinfo("Info","El calibre recomendado para evitar cualquier mal funcionamiento es de: 10")

                if self.diametro > 0.205 and self.diametro < 0.259:
                    messagebox.showinfo("Info","El calibre recomendado para evitar cualquier mal funcionamiento es de: 12")

                if self.diametro < 0.205:
                    messagebox.showinfo("Info","El calibre recomendado para evitar cualquier mal funcionamiento es de: 14")

            else:
                messagebox.showerror("error", "Debe de ingresar el largo del cable ")
        else:
            messagebox.showerror("error", "Debe de ingresar al menos un dispositivo ")

    
    

    def graficar(self):
        # obtener todas las llaves para ver que es lo que hay
        # graficar
          
        self.c1.create_rectangle((self.c1.winfo_width()/2)-250,  (self.c1.winfo_height()/2) +20, (self.c1.winfo_width())-100,  (self.c1.winfo_height()/2)-10, fill='gray')

        if len(listaDispositivos)>0:

            #
            self.width_canvas= (self.c1.winfo_width())-710
            self.altura_canvas= (self.c1.winfo_height()/2) - 100

            self.width_canvas2= (self.c1.winfo_width())-710
            self.altura_canvas2= (self.c1.winfo_height()/2) + 100
            
            for elemento in llaves:
                # Para cada clave en el diccionario
                for key in Electrodomesticos.keys():
                    # Si el elemento es igual a la clave
                    if elemento == key:
                        self.contador+= 1
                        print("\n contador"+str(self.contador))
                        valor_link_imagen = Electrodomesticos[key]
                        print(f'el elemento de la lista {elemento} s igual a la clave {key}')
                        print(valor_link_imagen)
                        # poner la imagen al canvas
                        response = requests.get(valor_link_imagen)
                        img_data= response.content
                        #Abrir la imagen con PIL 
                        img = Image.open(BytesIO(img_data))
                        #cambiar el tamaño 
                        nuevo_tamanio=(100,100)
                        img = img.resize(nuevo_tamanio)
                        #convertir la imagen a formato tkinter
                        tk_img = ImageTk.PhotoImage(img)
                        self.imagenes.append(tk_img)

                        if (self.contador <6 ):
                            #aumentar el valor del canvas
                            self.width_canvas= self.width_canvas+110
                            #Añadir la imagen al canvas
                            self.c1.create_image(self.width_canvas,self.altura_canvas, image=self.imagenes[-1])
                        else:
                            self.width_canvas2= self.width_canvas2+110
                            #Añadir la imagen al canvas
                            self.c1.create_image(self.width_canvas2,self.altura_canvas2, image=self.imagenes[-1])

                        


                        
                        



        else: 
            messagebox.showerror("error","primero debe de agregar algun dispositivo")



    def limpiar(self):
        self.c1.delete("all")
    

app().mainloop()