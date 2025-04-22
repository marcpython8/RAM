from tkinter import ttk
import customtkinter as ct
from PIL import Image
from tkinter import Toplevel

class vetana_principal:

    def __init__(self,app):
        self.app = app
        self.app.minsize(800, 600)
        self.app.resizable(False, False)
        self.app.config(bg="#054c2e")
        self.app.title("Login")
        self.app.iconbitmap("RAM Logo_i.ico")

        self.image = ct.CTkImage(light_image=Image.open("RAM_Logo.png"),
                                 size=(300, 300))

        self.image_label = ct.CTkLabel(app, image=self.image, text="",bg_color="#054c2e")
        self.image_label.place(x=25, y=20)

        self.Bienvenido = ct.CTkLabel(app,text="Bienvenido",font=("Gill Sans",30,"bold"),bg_color="#054c2e",text_color="#fcfce9")
        self.Bienvenido.place(x=95,y=280)

        self.Farm_confi = ct.CTkLabel(app, text="Tu farmacia de confianza", font=("Gill Sans", 20), bg_color="#054c2e",
                                 text_color="#fcfce9")
        self.Farm_confi.place(x=65, y=320)

        self.frame = ct.CTkFrame(app,width=450,height=820)
        self.frame.place(x=350,y=0)

        self.inicar_sesion = ct.CTkLabel(self.frame,text="Iniciar Sesión",font=("Gill Sans", 30,"bold"))
        self.inicar_sesion.place(x=130,y=50)

        self.Email = ct.CTkLabel(self.frame, text="Email", font=("Gill Sans", 15, "bold"))
        self.Email.place(x=80, y=120)

        self.Email_Entrada = ct.CTkEntry(self.frame,width=300,font=("Gill Sans", 15))
        self.Email_Entrada.place(x=80, y=150)

        self.Password = ct.CTkLabel(self.frame, text="Password", font=("Gill Sans", 15, "bold"))
        self.Password.place(x=80, y=200)

        self.Password_Entrada = ct.CTkEntry(self.frame, width=300, font=("Gill Sans", 15),show="*")
        self.Password_Entrada.place(x=80, y=230)

        self.entrar = ct.CTkButton(self.frame,text="Entrar",font=("Gill Sans", 15,"bold"),text_color="white",corner_radius=30,
                                   fg_color="#054c2e",hover_color="#022e03")
        self.entrar.place(x=150,y=280)

        self.tienes_cuenta = ct.CTkLabel(self.frame,text="¿No tienes cuenta?",font=("Gill Sans", 20, "bold"))
        self.tienes_cuenta.place(x=130,y=350)

        self.Botton_CC = ct.CTkButton(self.frame,text="Crear Cuenta",text_color="white",font=("Gill Sans", 15,"bold"),
                                      fg_color="#f01009",corner_radius=30,hover_color="#ab0a05",command=self.crear_cuenta)
        self.Botton_CC.place(x=150,y=390)

    def crear_cuenta(self):
        self.segunda_ventana = Toplevel(self.app)
        self.segunda_ventana.minsize(990, 750)
        self.segunda_ventana.resizable(False, False)
        self.segunda_ventana.title("Crear Cuenta")
        self.segunda_ventana.iconbitmap("RAM Logo_i.ico")

        self.frame_superior = ct.CTkFrame(self.segunda_ventana,width=10,fg_color="#054c2e")
        self.frame_superior.place(relx=0, rely=0, relwidth=1)

        self.image = ct.CTkImage(light_image=Image.open("RAM_Logo.png"),
                                 size=(180, 180))

        self.image_label = ct.CTkLabel(self.frame_superior, image=self.image, text="", bg_color="#054c2e")
        self.image_label.grid(row=0, column=0, padx=1, pady=1)

        self.comencemos = ct.CTkLabel(self.frame_superior,text="¡Comencemos!",font=("Gill Sans",70,"bold"),text_color="white")
        self.comencemos.place(x=200,y=50)

        self.nombre = ct.CTkLabel(self.segunda_ventana,text="Nombre(s):",font=("Gill Sans",20,"bold"))
        self.nombre.place(x=28,y=229)

        self.nombre_entrada = ct.CTkEntry(self.segunda_ventana,width=200,font=("Gill Sans",20))
        self.nombre_entrada.place(x=140,y=229)

        self.apellidoPa = ct.CTkLabel(self.segunda_ventana,text="Apellido (Pat/Mat):",font=("Gill Sans",20,"bold"))
        self.apellidoPa.place(x=360,y=229)

        self.apellidoPa_entrada = ct.CTkEntry(self.segunda_ventana, width=200, font=("Gill Sans", 20))
        self.apellidoPa_entrada.place(x=540, y=229)

        self.genero = ct.CTkLabel(self.segunda_ventana,text="Genero:",font=("Gill Sans",20,"bold"))
        self.genero.place(x=28,y=300)

        self.generoEn = ct.CTkComboBox(self.segunda_ventana,values=["Hombre", "Mujer", "Prefiero no decirlo"])
        self.generoEn.set("")
        self.generoEn.place(x=110,y=300)

        self.MayorDeEdad = ct.CTkLabel(self.segunda_ventana,text="¿Eres mayor de edad?",font=("Gill Sans",20,"bold"))
        self.MayorDeEdad.place(x=290,y=300)

        self.checkSi = ct.CTkCheckBox(self.segunda_ventana,text="Si",font=("Gill Sans",20),hover_color="#157c0c")
        self.checkSi.place(x=520,y=302)

        self.checkNo = ct.CTkCheckBox(self.segunda_ventana, text="No",font=("Gill Sans",20),hover_color="#157c0c")
        self.checkNo.place(x=580, y=302)

        self.fecha = ct.CTkLabel(self.segunda_ventana,text="Fecha de Nacimiento:",font=("Gill Sans",20,"bold"))
        self.fecha.place(x=28,y=370)

        self.dia = ct.CTkComboBox(self.segunda_ventana, values=["1","2","3","4","5","6","7","8","9","10",
                                                                "11","12","13","14","15","16","17","18","19","20",
                                                                "21","22","23","23","24","25","26","27","28","27","28","29","30",
                                                                "31"])
        self.dia.set("")
        self.dia.place(x=240, y=370)

        self.mes = ct.CTkComboBox(self.segunda_ventana, values=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
                                                                "Agosto","Septiembre","Octubre","Noviembre","Diciembre"])
        self.mes.set("")
        self.mes.place(x=390, y=370)

        self.año = ct.CTkComboBox(self.segunda_ventana, values=["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000",
                                                                "2001","2002","2003","2004","2005","2006","2007","2008","2009","2010",
                                                                "2011","2012","2013","2014","2015","2016","2017","2018","2019","2020",
                                                                "2021","2022","2023","2024","2025"])
        self.año.set("")
        self.año.place(x=540, y=370)

        self.correo = ct.CTkLabel(self.segunda_ventana,text="Correo:",font=("Gill Sans",20,"bold"))
        self.correo.place(x=28,y=430)

        self.correo_entrada = ct.CTkEntry(self.segunda_ventana,width=180)
        self.correo_entrada.place(x=110,y=430)

        self.contraseña = ct.CTkLabel(self.segunda_ventana, text="Contraseña:", font=("Gill Sans", 20, "bold"))
        self.contraseña.place(x=320, y=430)

        self.contraseña_entrada = ct.CTkEntry(self.segunda_ventana, width=180)
        self.contraseña_entrada.place(x=450, y=430)

        self.crear = ct.CTkButton(self.segunda_ventana,text="Crear Cuenta",font=("Gill Sans",20,"bold"),text_color="white",
                                  corner_radius=20,fg_color="#13c104",hover_color="#0f7307",command=self.regresar_login)
        self.crear.place(x=320,y=490)

    def regresar_login(self):
        self.segunda_ventana.destroy()


app = ct.CTk()
ventana = vetana_principal(app)
app.mainloop()
