# Importaciones
import threading
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from classes.b import master
import time
import sqlite3

##LOCALES##
timer = 60
test1On = False
test2On = False

# Colores
black = '#343434'
darkGrey = '#464646'
lightGrey = '#b7b7b7'
orange = '#fb8500'

##VENTANA##
root = Tk()
root.title("Cubicaje")
root.geometry("1090x750")
root.resizable(width=False, height=False)
imgBackground = PhotoImage(file="problemas\imgs\mainBackground.png")
mainBackground = Label(root, image=imgBackground).place(x=-100, y=-100)

# Footer
footer = Frame(root, bg=black)
footer.pack(side=BOTTOM, fill=X)

# Funcion test 1


def showTest1():
    clean()
    global test1On, test1, mainFrame1
    test1On = True

    test1.config(state=DISABLED, disabledforeground='white',
                 background=darkGrey)

    # Frame principal
    mainFrame1 = Frame(root, height=100, width=100)
    mainFrame1.pack(padx=100, pady=50)
    mainOn = True

    # Header frame
    header = Frame(mainFrame1, height=40, bg=darkGrey)
    header.pack(side=TOP, fill=X)

    # Actualizar Temporizador y datos de la tabla
    def updateTimer():
        global timer
        timerLabel.config(text='T I M E  T O  R E S E T :   %ss' % timer)
        timer -= 1
        if timer == 0:
            timer = 60
            setTableValues()
        timerLabel.after(1000, updateTimer)

    # Label de tiempo
    timerLabel = Label(header, text="T I M E: %ss" %
                       timer, bg=darkGrey, fg='white', font=('Segoe UI', 15))
    timerLabel.pack(pady=5, side=TOP)

    # Llamada de funcion
    updateTimer()

    # Foooter
    footer = Frame(mainFrame1, height=40, bg=darkGrey)
    footer.pack(side=BOTTOM, fill=X)

    # Variables del footer
    maxLabelVar = StringVar()
    maxLabel = Label(footer, textvariable=maxLabelVar, bg=darkGrey, fg='white', font=(
        'Segoe UI', 13)).pack(side=LEFT, padx=17, pady=10)
    minLabelVar = StringVar()
    minLabel = Label(footer, textvariable=minLabelVar, bg=darkGrey, fg='white', font=(
        'Segoe UI', 13)).pack(side=LEFT, padx=17, pady=10)
    firstLabelVar = StringVar()
    firstLabel = Label(footer, textvariable=firstLabelVar, bg=darkGrey, fg='white', font=(
        'Segoe UI', 13)).pack(side=LEFT, padx=17, pady=10)
    lastLabelVar = StringVar()
    lastLabel = Label(footer, textvariable=lastLabelVar, bg=darkGrey, fg='white', font=(
        'Segoe UI', 13)).pack(side=LEFT, padx=17, pady=10)
    primeLabelVar = StringVar()
    primeLabel = Label(footer, textvariable=primeLabelVar, bg=darkGrey, fg='white', font=(
        'Segoe UI', 13)).pack(side=LEFT, padx=17, pady=10)
    evenLabelVar = StringVar()
    evenLabel = Label(footer, textvariable=evenLabelVar, bg=darkGrey, fg='white', font=(
        'Segoe UI', 13)).pack(side=LEFT, padx=17, pady=10)
    oddLabelVar = StringVar()
    oddLabel = Label(footer, textvariable=oddLabelVar, bg=darkGrey, fg='white', font=(
        'Segoe UI', 13)).pack(side=LEFT, padx=17, pady=10)

    ##TABLA##

    # Estilos
    style = ttk.Style()
    style.theme_use('clam')

    style.configure('Treeview',
                    background=lightGrey,
                    foreground=darkGrey,
                    rowheight=45)

    style.configure('Treeview.Heading',
                    background=darkGrey,
                    foreground='white',
                    font=('Segoe UI', 10),
                    troughcolor=black,
                    bordercolor=black,
                    arrowcolor=black,
                    darkcolor=black,
                    lightcolor=black)

    style.map('Treeview.Heading',
              background=[('pressed', '!disabled', lightGrey), ('active', 'grey')])

    style.map('Treeview',
              background=[('selected', darkGrey)],
              troughcolor=black,
              bordercolor=black,
              arrowcolor=black,
              darkcolor=black,
              lightcolor=black)

    # Scrollbar y
    scrollBary = ttk.Scrollbar(mainFrame1, orient=VERTICAL)
    scrollBary.pack(side=RIGHT, fill=Y)

    style.configure('Vertical.TScrollbar',
                    background=darkGrey,
                    troughcolor=black,
                    bordercolor=darkGrey,
                    arrowcolor=lightGrey,
                    darkcolor=darkGrey,
                    lightcolor=darkGrey)

    style.map('Vertical.TScrollbar',
              background=[('pressed', '!disabled', lightGrey), ('active', 'grey')])

    # Tabla
    table = ttk.Treeview(
        mainFrame1, yscrollcommand=scrollBary.set, selectmode='browse')
    table.pack(pady=0)
    scrollBary.config(command=table.yview)

    table['columns'] = ('B', 'M A X', 'M I N', 'F I R S T',
                        'L A S T', 'P R I M E', 'E V E N', 'O D D')

    table.column('#0',
                 width=0,
                 stretch=NO)
    table.column('B',
                 width=100,
                 anchor='center')
    table.column('M A X',
                 width=100,
                 anchor='center')
    table.column('M I N',
                 width=100,
                 anchor='center')
    table.column('F I R S T',
                 width=100,
                 anchor='center')
    table.column('L A S T',
                 width=100,
                 anchor='center')
    table.column('P R I M E',
                 width=100,
                 anchor='center')
    table.column('E V E N',
                 width=100,
                 anchor='center')
    table.column('O D D',
                 width=100,
                 anchor='center')

    table.heading('#0',
                  text='')
    table.heading('#1',
                  text='B')
    table.heading('#2',
                  text='M A X')
    table.heading('#3',
                  text='M I N')
    table.heading('#4',
                  text='F I R S T')
    table.heading('#5',
                  text='L A S T')
    table.heading('#6',
                  text='P R I M E')
    table.heading('#7',
                  text='E V E N')
    table.heading('#8',
                  text='O D D')

    def setTableValues():
        # Limpiar la tabla
        table.delete(*table.get_children())
        # Generar numeros
        master.generate()
        # Asignar valores a las variables
        firstLabelVar.set('First:   %s' % str(master.first))
        lastLabelVar.set('Last:   %s' % str(master.last))
        primeLabelVar.set('Prime:   %s' % str(master.prime))
        evenLabelVar.set('Even:   %s' % str(master.even))
        oddLabelVar.set('Odd:   %s' % str(master.odd))
        # Recorrer la lista
        for i in range(len(master.b)):
            # inicializar variables
            isMax = 'N o'
            isMin = 'N o'
            isFirst = 'N o'
            isLast = 'N o'
            isPrime = 'N o'
            isEven = 'N o'
            isOdd = 'N o'

            # Verificar si es max
            if max(master.b) == master.b[i]:
                isMax = 'Y e s'
                maxLabelVar.set('Max:   %s' % str(master.b[i]))
            # Verificar si es min
            if min(master.b) == master.b[i]:
                isMin = 'Y e s'
                minLabelVar.set('Min:   %s' % str(master.b[i]))
            # Verificar si fue el primero
            if master.first == master.b[i] and master.firstPosition == i:
                isFirst = 'Y e s'
            # Verificar si fue el ultimo
            if master.last == master.b[i] and master.lastPosition == i:
                isLast = 'Y e s'
            # Verificar si es primo
            if master.isPrime(master.b[i]):
                isPrime = 'Y e s'
            # Verificar si es par
            if master.isEven(master.b[i]):
                isEven = 'Y e s'
            # Verificar si es impar
            if master.isOdd(master.b[i]):
                isOdd = 'Y e s'
            # Insertar los valores en la tabla
            table.insert(parent='', index='end', text='', values=(
                master.b[i], isMax, isMin, isFirst, isLast, isPrime, isEven, isOdd))

    # Llamada de inicializacion
    setTableValues()


# Boton test 1
test1 = Button(footer,
               text="P R O B L E M 1",
               font=('Segoe UI', 10),
               foreground='white',
               activeforeground='white',
               width=77,
               height=6,
               relief='flat',
               borderwidth=0,
               background=black,
               activebackground=darkGrey,
               command=showTest1)
test1.pack(side=LEFT)

# Funcion test 2


def showTest2():
    ##DATABASE##
    conn = sqlite3.connect('problema2.db')
    c = conn.cursor()
    # Crear tabla

    def createTable():
        c.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            userName TEXT(25), 
            lastname TEXT(25), 
            age INTEGER(3),
            email TEXT(25) UNIQUE)''')
        conn.commit()
        
    createTable()

    # Eliminar Tabla

    def dropTable():
        c.execute('''DROP TABLE users''')
        conn.commit()
    # Clase Usuario

    class USER():
        # Usuarios creados
        users = c.execute("SELECT * FROM users")
        users = c.fetchall()

        # Constructor
        def __init__(self):
            pass
        
        # Crear usuario
        def createUser(self, user):
            for i in range(len(user)):
                c.execute(
                    "INSERT INTO users(userName, lastName, age, email) VALUES (?, ?, ?, ?)", (user[i]))
        # Editar usuario

        def editUser(self, user):
            for i in range(len(user)):
                c.execute(
                    "UPDATE users SET userName=?, lastName=?, age=?, email=? WHERE id=?", (user[i]))
        # Eliminar usuario

        def deleteUser(self, id):
            c.execute("DELETE FROM users WHERE id=?", (id,))
        # Buscar usuario

        def searchUserById(self, id):
            quest = c.execute("SELECT * FROM users WHERE id=?", (id,))
            return quest.fetchone()
          
     
    # User manager
    um = USER()
    # Variables globales
    global test2On, test1, mainFrame2
    # Limpiar pantalla
    clean()
    test2On = True
    # Deshabilitar boton
    test2.config(state=DISABLED, bg=darkGrey,
                 disabledforeground='white')

    # Frame
    mainFrame2 = Frame(root,
                       width=1000,
                       height=1000)
    mainFrame2.pack(padx=100, pady=100)

    # Header
    header = Frame(mainFrame2,
                   height=35,
                   background=black)
    header.pack(side=TOP, fill=X)

    ##BOTONES##

    # Frame de botones
    buttonsFrame = Frame(mainFrame2,
                         height=50)
    buttonsFrame.pack(side=BOTTOM, fill=X)

    def filterActionButton():
        #Limpiar pantalla
        clean()
        #Deshabilitar boton
        test2.config(state=DISABLED, bg=darkGrey,
                 disabledforeground='white')
        test1.config(state=DISABLED, bg=black,
                 disabledforeground='white')
        #Filter frame
        filterFrame = Frame(root,
                            height=50,
                            width=50,
                            background=darkGrey)
        filterFrame.pack(pady=157)
        # Header
        headerEditUser = Frame(filterFrame,
                                    height=35,
                                    width=700,
                                    background=black)
        headerEditUser.grid(row=0, column=0, columnspan=2, sticky=W+E)
        headerText = Label(headerEditUser,
                           text='F I L T E R  U S E R',
                           bg=black,
                           fg='white',
                           font=('Segoe UI', 10)).pack(side=TOP, pady=7)

        # footer
        footerEditUser = Frame(filterFrame,
                                    height=45,
                                    width=700,
                                    background=black)
        footerEditUser.grid(row=6, column=0, columnspan=2, sticky=W+E)

        # Texto
        idLabel = Label(filterFrame,
                          text="I D",
                          font=('Segoe UI', 10),
                          foreground='white',
                          background=darkGrey).grid(row=1, column=0, pady=10, padx=40)
        
        nameLabel = Label(filterFrame,
                          text='N A M E',
                          font=('Segoe UI', 10),
                          foreground='white',
                          background=darkGrey).grid(row=2, column=0, pady=10, padx=40)
        
        userNameVar = StringVar()
        userNameLabel = Label(filterFrame,
                          textvariable=userNameVar,
                          font=('Segoe UI', 10),
                          foreground='white',
                          background=darkGrey).grid(row=2, column=1, pady=10, padx=40)
        
        lastNameLabel = Label(filterFrame,
                              text='L A S T  N A M E',
                              font=('Segoe UI', 10),
                              foreground='white',
                              background=darkGrey).grid(row=3, column=0, pady=10, padx=40)
        
        userLastNameVar= StringVar() 
        userLastNameLabel = Label(filterFrame,
                              textvariable=userLastNameVar,
                              font=('Segoe UI', 10),
                              foreground='white',
                              background=darkGrey).grid(row=3, column=1, pady=10, padx=40)
        
        ageLabel = Label(filterFrame,
                         text="A G E",
                         font=('Segoe UI', 10),
                         foreground='white',
                         background=darkGrey).grid(row=4, column=0, pady=10, padx=40)
        
        userAgeVar = StringVar()
        userAageLabel = Label(filterFrame,
                         textvariable=userAgeVar,
                         font=('Segoe UI', 10),
                         foreground='white',
                         background=darkGrey).grid(row=4, column=1, pady=10, padx=40)
        
        emailLabel = Label(filterFrame,
                           text='E M A I L',
                           font=('Segoe UI', 10),
                           foreground='white',
                           background=darkGrey).grid(row=5, column=0, pady=10, padx=40)
        
        userEmailVar = StringVar()
        userEmailLabel = Label(filterFrame,
                           textvariable=userEmailVar,
                           font=('Segoe UI', 10),
                           foreground='white',
                           background=darkGrey).grid(row=5, column=1, pady=10, padx=40)
        
        # Entrada
        idVar = IntVar()
        idVar.set(0)
        idEntry = Entry(filterFrame,
                          textvariable=idVar,
                          borderwidth=0,
                          background=lightGrey,
                          relief='flat',
                          foreground=black,
                          font=('Segoe UI', 10),
                          justify=CENTER).grid(row=1, column=1, pady=10, padx=40)

        # Funcion de volver
        def filterUserBack():
            global containersActionButton
            filterFrame.pack_forget()
            showTest2()
            test1.config(state=NORMAL, bg=black)
        # Función de agregar

        def filterUser():
            user = um.searchUserById(idVar.get())
            userNameVar.set(user[1])
            userLastNameVar.set(user[2])
            userAgeVar.set(user[3])
            userEmailVar.set(user[4])
                
        # Boton de restroceder
        backAddUserButton = Button(footerEditUser,
                                   text="B A C K",
                                   height=2,
                                   width=20,
                                   command=filterUserBack,
                                   bg=black,
                                   activebackground=darkGrey,
                                   fg='white',
                                   activeforeground='white',
                                   font=('Segoe UI', 10),
                                   relief='flat',
                                   borderwidth=0).pack(side=LEFT)
        # Boton de añadir usuario
        addUserButton = Button(footerEditUser,
                               text='F I L T E R',
                               height=2,
                               width=25,
                               command=filterUser,
                               bg=black,
                               activebackground=darkGrey,
                               fg='white',
                               activeforeground='white',
                               font=('Segoe UI', 10),
                               relief='flat',
                               borderwidth=0).pack(side=RIGHT)

        # Boton de agregar
        addUserButton = Button(buttonsFrame,
                            text="A  G  R  E  G  A  R",
                            font=('Segoe UI', 10),
                            foreground='white',
                            activeforeground='white',
                            width=32,
                            height=2,
                            relief='flat',
                            borderwidth=0,
                            background=black,
                            activebackground=darkGrey,
                            command=addActionButton).pack(side=LEFT)

        
        
    
    # Boton de filtrar
    filterButton = Button(buttonsFrame,
                          text="F I L T R A R",
                          font=('Segoe UI', 10),
                          foreground='white',
                          activeforeground='white',
                          width=32,
                          height=2,
                          relief='flat',
                          borderwidth=0,
                          background=black,
                          activebackground=darkGrey,
                          command=filterActionButton).pack(side=LEFT)

    # funcion de agregar

    def addActionButton():
        # Limpiar pantalla
        clean()
        # Deshabilitar boton
        test2.config(
            state=DISABLED, bg=darkGrey, disabledforeground='white')
        test1.config(
            state=DISABLED, bg=black, disabledforeground='white')

        # Frame de agregar
        addUserFrame = Frame(root,
                             width=1000,
                             height=1000,
                             background=darkGrey)
        addUserFrame.pack(padx=100, pady=157)

        # Header
        headerAddUser = Frame(addUserFrame,
                                    height=35,
                                    width=700,
                                    background=black)
        headerAddUser.grid(row=0, column=0, columnspan=6, sticky=W+E)
        headerText = Label(headerAddUser,
                           text='A D D  U S E R',
                           bg=black,
                           fg='white',
                           font=('Segoe UI', 10)).pack(side=TOP, pady=7)

        # footer
        footerAddUser = Frame(addUserFrame,
                                    height=45,
                                    width=700,
                                    background=black)
        footerAddUser.grid(row=14, column=0, columnspan=6, sticky=W+E)

        # Texto
        nameLabel = Label(addUserFrame,
                          text="N A M E",
                          font=('Segoe UI', 10),
                          foreground='white',
                          background=darkGrey).grid(row=1, column=0, pady=10, padx=40)
        lastNameLabel = Label(addUserFrame,
                              text="L A S T  N A M E",
                              font=('Segoe UI', 10),
                              foreground='white',
                              background=darkGrey).grid(row=2, column=0, pady=10, padx=40)
        ageLabel = Label(addUserFrame,
                         text="A G E",
                         font=('Segoe UI', 10),
                         foreground='white',
                         background=darkGrey).grid(row=3, column=0, pady=10, padx=40)
        emailLabel = Label(addUserFrame,
                           text="E M A I L",
                           font=('Segoe UI', 10),
                           foreground='white',
                           background=darkGrey).grid(row=4, column=0, pady=10, padx=40)

        # Entrada
        nameVar = StringVar()
        nameVar.set('NULL')
        nameEntry = Entry(addUserFrame,
                          textvariable=nameVar,
                          borderwidth=0,
                          background=lightGrey,
                          relief='flat',
                          foreground=black,
                          font=('Segoe UI', 10),
                          justify=CENTER).grid(row=1, column=1, pady=10, padx=40)
        lastNameVar = StringVar()
        lastNameVar.set('NULL')
        lastNameEntry = Entry(addUserFrame,
                              textvariable=lastNameVar,
                              borderwidth=0,
                              background=lightGrey,
                              relief='flat',
                              foreground=black,
                              font=('Segoe UI', 10),
                              justify=CENTER).grid(row=2, column=1, pady=10, padx=40)
        ageVar = IntVar()
        ageVar.set(0)
        ageEntry = Entry(addUserFrame,
                         textvariable=ageVar,
                         borderwidth=0,
                         background=lightGrey,
                         relief='flat',
                         foreground=black,
                         font=('Segoe UI', 10),
                         justify=CENTER).grid(row=3, column=1, pady=10, padx=40)
        emailVar = StringVar()
        emailVar.set('NULL')
        emailEntry = Entry(addUserFrame,
                           textvariable=emailVar,
                           borderwidth=0,
                           background=lightGrey,
                           relief='flat',
                           foreground=black,
                           font=('Segoe UI', 10),
                           justify=CENTER).grid(row=4, column=1, pady=10, padx=40)

        # Funcion de volver
        def addUserBack():
            global containersActionButton
            addUserFrame.pack_forget()
            showTest2()
            test1.config(state=NORMAL, bg=black)
        # Función de agregar

        def addUser():
            quest = tk.messagebox.askyesno(
                'A G R E G A R', 'Seguro que quieres añadir un nuevo usuario?')
            print(quest)
            if quest:
                # Almacenamiento de usuario
                newUser = [(nameVar.get(), lastNameVar.get(),
                            ageVar.get(), emailVar.get())]
                # Creacion de usuario
                um.createUser(newUser)
                conn.commit()
                # Volver a la pantalla principal
                addUserBack()
            else:
                ...
        # Boton de restroceder
        backAddUserButton = Button(footerAddUser,
                                   text="B A C K",
                                   height=2,
                                   width=20,
                                   command=addUserBack,
                                   bg=black,
                                   activebackground=darkGrey,
                                   fg='white',
                                   activeforeground='white',
                                   font=('Segoe UI', 10),
                                   relief='flat',
                                   borderwidth=0).pack(side=LEFT)
        # Boton de añadir usuario
        addUserButton = Button(footerAddUser,
                               text='A D D',
                               height=2,
                               width=25,
                               command=addUser,
                               bg=black,
                               activebackground=darkGrey,
                               fg='white',
                               activeforeground='white',
                               font=('Segoe UI', 10),
                               relief='flat',
                               borderwidth=0).pack(side=RIGHT)

    # Boton de agregar
    addUserButton = Button(buttonsFrame,
                           text="A  G  R  E  G  A  R",
                           font=('Segoe UI', 10),
                           foreground='white',
                           activeforeground='white',
                           width=32,
                           height=2,
                           relief='flat',
                           borderwidth=0,
                           background=black,
                           activebackground=darkGrey,
                           command=addActionButton).pack(side=LEFT)

    # Funcion de eliminar

    def deleteActionButton():
        # Verificar si se selecciono un usuario
        if len(table.selection()) == 0:
            tk.messagebox.showinfo(
                "A T E N C I O N", "Debes seleccionar un usuario")
        else:
            # Preguntar si se quiere eliminar
            selected = table.item(table.focus())["values"][0]
            quest = tk.messagebox.askyesno(
                "E L I M I N A R", "Seguro que quieres eliminar el usuario %s?" % selected)
            if quest == True:
                # Eliminar usuario
                selection = table.selection()[0]
                um.deleteUser(int(selected))
                table.delete(selection)
                conn.commit()
            else:
                ...

    # Boton de eliminar
    deleteButton = Button(buttonsFrame,
                          text="E L I M I N A R",
                          font=('Segoe UI', 10),
                          foreground='white',
                          activeforeground='white',
                          width=32,
                          height=2,
                          relief='flat',
                          borderwidth=0,
                          background=black,
                          activebackground=darkGrey,
                          command=deleteActionButton).pack(side=LEFT)

    # Funcion de modificar

    def editActionButton():
        # Verificar si se selecciono un usuario
        if len(table.selection()) == 0:
            tk.messagebox.showinfo(
                "A T E N C I O N", "Debes seleccionar un usuario")
        else:
            # Limpiar pantalla
            clean()
            # Deshabilñitar botones
            test2.config(
                state=DISABLED, bg=darkGrey, disabledforeground='white')
            test1.config(
                state=DISABLED, bg=black, disabledforeground='white')

            # Frame de agregar
            editUserFrame = Frame(root,
                                  width=1000,
                                  height=1000,
                                  background=darkGrey)
            editUserFrame.pack(padx=100, pady=157)

            # Header
            headerEditContainers = Frame(editUserFrame,
                                         height=35,
                                         width=700,
                                         background=black)
            headerEditContainers.grid(
                row=0, column=0, columnspan=6, sticky=W+E)
            headerText = Label(headerEditContainers,
                               text='U S U A R I O  %s' % table.item(table.focus())[
                                   "values"][0],
                               bg=black,
                               fg='white',
                               font=('Segoe UI', 10)).pack(side=TOP, pady=7)

            # footer
            footerEditContainers = Frame(editUserFrame,
                                         height=45,
                                         width=700,
                                         background=black)
            footerEditContainers.grid(
                row=14, column=0, columnspan=6, sticky=W+E)

            # Texto
            nameLabel = Label(editUserFrame,
                              text="N O M B R E",
                              font=('Segoe UI', 10),
                              foreground='white',
                              background=darkGrey).grid(row=1, column=0, pady=10, padx=40)
            lastNameLabel = Label(editUserFrame,
                                  text="L A S T  N A M E",
                                  font=('Segoe UI', 10),
                                  foreground='white',
                                  background=darkGrey).grid(row=2, column=0, pady=10, padx=40)
            ageLabel = Label(editUserFrame,
                             text="A G E",
                             font=('Segoe UI', 10),
                             foreground='white',
                             background=darkGrey).grid(row=3, column=0, pady=10, padx=40)
            emailLabel = Label(editUserFrame,
                               text="E M A I L",
                               font=('Segoe UI', 10),
                               foreground='white',
                               background=darkGrey).grid(row=4, column=0, pady=10, padx=40)
            # Entrada
            nameVar = StringVar()
            nameVar.set(table.item(table.focus())["values"][1])
            nameEntry = Entry(editUserFrame,
                              textvariable=nameVar,
                              borderwidth=0,
                              background=lightGrey,
                              relief='flat',
                              foreground=black,
                              font=('Segoe UI', 10),
                              justify=CENTER).grid(row=1, column=1, pady=10, padx=40)
            lastNameVar = StringVar()
            lastNameVar.set(table.item(table.focus())["values"][2])
            lastNameEntry = Entry(editUserFrame,
                                  textvariable=lastNameVar,
                                  borderwidth=0,
                                  background=lightGrey,
                                  relief='flat',
                                  foreground=black,
                                  font=('Segoe UI', 10),
                                  justify=CENTER).grid(row=2, column=1, pady=10, padx=40)
            ageVar = IntVar()
            ageVar.set(table.item(table.focus())["values"][3])
            ageEntry = Entry(editUserFrame,
                             textvariable=ageVar,
                             borderwidth=0,
                             background=lightGrey,
                             relief='flat',
                             foreground=black,
                             font=('Segoe UI', 10),
                             justify=CENTER).grid(row=3, column=1, pady=10, padx=40)
            emailVar = StringVar()
            emailVar.set(table.item(table.focus())["values"][4])
            emailEntry = Entry(editUserFrame,
                               textvariable=emailVar,
                               borderwidth=0,
                               background=lightGrey,
                               relief='flat',
                               foreground=black,
                               font=('Segoe UI', 10),
                               justify=CENTER).grid(row=4, column=1, pady=10, padx=40)
            # Funcion de regresar

            def editContainerBack():
                global showTest2
                editUserFrame.pack_forget()
                test1.config(state=NORMAL, bg=black)
                showTest2()
            # Boton de editar

            def edit():
                tk.messagebox.showinfo(
                    "A T E N C I O N", "Seguro que quieres modificar el usuario %s" % table.item(table.focus())["values"][0])
                updatedUser = [(nameVar.get(), lastNameVar.get(), ageVar.get(
                ), emailVar.get(), table.item(table.focus())["values"][0])]
                um.editUser(updatedUser)
                conn.commit()
                editContainerBack()

            # Boton de regresar
            backEditUserButton = Button(footerEditContainers,
                                        text="A  T  R  A  S",
                                        height=2,
                                        width=20,
                                        command=editContainerBack,
                                        bg=black,
                                        activebackground=darkGrey,
                                        fg='white',
                                        activeforeground='white',
                                        font=('Segoe UI', 10),
                                        relief='flat',
                                        borderwidth=0).pack(side=LEFT)
            editUserButton = Button(footerEditContainers,
                                    text='E D I T A R',
                                    height=2,
                                    width=25,
                                    command=edit,
                                    bg=black,
                                    activebackground=darkGrey,
                                    fg='white',
                                    activeforeground='white',
                                    font=('Segoe UI', 10),
                                    relief='flat',
                                    borderwidth=0).pack(side=RIGHT)

    # Boton de editar
    editButton = Button(buttonsFrame,
                        text="E D I T A R",
                        font=('Segoe UI', 10),
                        foreground='white',
                        activeforeground='white',
                        width=32,
                        height=2,
                        relief='flat',
                        borderwidth=0,
                        background=black,
                        activebackground=darkGrey,
                        command=editActionButton).pack(side=LEFT)

    ##TABLA##
    style = ttk.Style()
    style.theme_use('clam')

    style.configure('Treeview',
                    background=lightGrey,
                    foreground=black,
                    rowheight=45)

    style.configure('Treeview.Heading',
                    background=darkGrey,
                    foreground='white',
                    font=('Segoe UI', 10),
                    troughcolor=black,
                    bordercolor=black,
                    arrowcolor=black,
                    darkcolor=black,
                    lightcolor=black)

    style.map('Treeview.Heading',
              background=[('pressed', '!disabled', lightGrey), ('active', 'grey')])

    style.map('Treeview',
              background=[('selected', darkGrey)],
              troughcolor=black,
              bordercolor=black,
              arrowcolor=black,
              darkcolor=black,
              lightcolor=black)

    # Scrollbar y
    scrollBary = ttk.Scrollbar(mainFrame2, orient=VERTICAL)
    scrollBary.pack(side=RIGHT, fill=Y)

    style.configure('Vertical.TScrollbar',
                    background=darkGrey,
                    troughcolor=black,
                    bordercolor=black,
                    arrowcolor=black,
                    darkcolor=black,
                    lightcolor=black)

    style.map('Vertical.TScrollbar',
              background=[('pressed', '!disabled', lightGrey), ('active', 'grey')])

    # Scrollbar x
    scrollBarx = ttk.Scrollbar(mainFrame2, orient=HORIZONTAL)
    scrollBarx.pack(side=TOP, fill=X)

    style.configure('Horizontal.TScrollbar',
                    background=darkGrey,
                    troughcolor=black,
                    bordercolor=black,
                    arrowcolor=black,
                    darkcolor=black,
                    lightcolor=black)

    style.map('Horizontal.TScrollbar',
              background=[('pressed', '!disabled', lightGrey), ('active', 'grey')])

    # Tabla
    table = ttk.Treeview(mainFrame2, xscrollcommand=scrollBarx.set,
                         yscrollcommand=scrollBary.set, selectmode='browse')
    table.pack(pady=0)
    scrollBary.config(command=table.yview)
    scrollBarx.config(command=table.xview)

    table['columns'] = (
        'I D', 'N A M E', 'L A S T  N A M E', 'A G E', 'E M A I L')

    table.column('#0',
                 width=0,
                 stretch=NO)
    table.column('I D',
                 width=150,
                 anchor='center')
    table.column('N A M E',
                 width=250,
                 anchor='center')
    table.column('L A S T  N A M E',
                 width=250,
                 anchor='center')
    table.column('A G E',
                 width=150,
                 anchor='center')
    table.column('E M A I L',
                 width=250,
                 anchor='center')

    table.heading('#0',
                  text='')
    table.heading('#1',
                  text='I D')
    table.heading('#2',
                  text='N A M E')
    table.heading('#3',
                  text='L A S T  N A M E')
    table.heading('#4',
                  text='A G E')
    table.heading('#5',
                  text='E M A I L')

    # Insertar datos
    for i in range(len(um.users)):
        table.insert(parent='', index='end', text='', values=(
            um.users[i][0], um.users[i][1], um.users[i][2], um.users[i][3], um.users[i][4]))

    if test2On == False:
        conn.close()


# Boton test 2
test2 = Button(footer,
               text="P R O B L E M 2",
               font=('Segoe UI', 10),
               foreground='white',
               activeforeground='white',
               width=77,
               height=6,
               relief='flat',
               borderwidth=0,
               background=black,
               activebackground=darkGrey,
               command=showTest2)
test2.pack(side=RIGHT)


def clean():
    global test1On, mainFrame1, test1, test2, test2On
    if test1On:
        test1.configure(state=NORMAL, background=black)
        mainFrame1.pack_forget()
        test1On = False
    if test2On:
        test2.configure(state=NORMAL, background=black)
        mainFrame2.pack_forget()
        test2On = False


root.mainloop()
