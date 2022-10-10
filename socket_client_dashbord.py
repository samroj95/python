import threading
import socket
from matplotlib.pyplot import text
from numpy import rec
import pyautogui
from tkinter import *
import tkinter
import tkinter as tk
import time
import os
import sys
import glenn01_support
import random
def resource_path(relative_path):   
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
root = tk.Tk()
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.5, height*0.5, width*0.2, height*0.2))

image_file = resource_path("one.gif")
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*0.5, width=width*0.5, bg="black")
canvas.create_image(width*0.5/2, height*0.5/2, image=image)
canvas.pack()
root.after(5000, root.destroy)
root.mainloop()
def vp_start_gui():
    
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    glenn01_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    glenn01_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
g = 0
ran=0
class Toplevel1:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self, top=None):
        '''while True:
            self.server_ip=socket.gethostname()
            self.server_port=5000
            if len(self.server_ip.split('.'))<4:
                print("samroj")
                break
        print("finding connection")'''

        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec' 
        fname =file=resource_path("1225.png")
        bg_image = tk.PhotoImage(file=fname)
        self.Canvas1 = tk.Canvas(top)
        startframe = tk.Frame(root)
        tk.Canvas(startframe, width=1280, height=800)
        startframe.pack()
        self.Canvas1.pack()
        root.bg_image = bg_image  
        self.Canvas1.create_image((0, 0), image=bg_image, anchor='nw') 
        w = bg_image.width()
        h = bg_image.height()
        top.geometry('%dx%d+0+10' % (w,h))        
        top.overrideredirect(True)
        top.title("Electray dashboard")
        top.configure(background="#000000")
        self.Canvas1.place(relx=-0.004, rely=-0.006, relheight=1.016, relwidth=1.003)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=1203)
        self.Canvas1.create_text(540, 215, fill="#42f5d7", text=" °C", font=("Arial", 9))
        self.Canvas1.create_text(530, 335, fill="#42f5d7", text="GEAR", font=("Arial", 9))
        self.Canvas1.create_text(480, 375, fill="#42f5d7", text="Coolant", font=("Arial", 9))
        self.Canvas1.create_text(580, 375, fill="#42f5d7", text="Oil", font=("Arial", 9))
        self.Canvas1.create_text(290, 320, fill="#42f5d7", text="MPH", font=("Arial", 12))
        self.Canvas1.create_text(750, 320, fill="#42f5d7", text="RPM", font=("Arial", 12))
        @property
        def  make_connection(self):
            '''Sending connection request to the server node'''
            while True:
                try:
                    server=(self.server_ip,self.server_port)
                    self.client_socket.connect(server)
                    print("Connection successful  made to the server")
                    return True
                except:
                    print("Connection not found")

        def server_send(self,msg):
           '''sending the data to the Connected server'''
           self.client_socket.send(msg.encode())
           print("Send data",msg)
        def recieve_sms(self):
            '''Recieving message from the node server'''
            while True:
                data=''
                data=self.client_socket.recv(1024).decode()
                time.sleep(0.001)
                print("Recieve data from client",data)

        def coolant(coolant_: int = 0):
            coolant_ = int(coolant_) 
            self.Canvas1.delete("tag1")      
            self.Canvas1.create_text (465, 345, text=coolant_, fill="#42f5d7", anchor='nw', font=("Arial", 16),tag="tag1")
            self.Canvas1.create_text(1090, 120, fill="#42f5d7", text="Coolant mode is on", font=("Arial", 10),tag="tag1")     
            self.Canvas1.create_text(1074, 127, fill="white", anchor='s', font=("Arial Bold", 10), tag="tag1")

        self.Scale1 = tk.Scale(top,command=coolant, from_=0.0, to=99.0)
        self.Scale1.place(relx=0.008, rely=0.861, relwidth=0.08, relheight=0.0, height=41, bordermode='ignore')
        self.Scale1.configure(activebackground="#39ede1")
        self.Scale1.configure(background="#000000")
        self.Scale1.configure(borderwidth="0")

        self.Scale1.configure(font="TkTextFont")
        self.Scale1.configure(foreground="#ffffff")
        self.Scale1.configure(highlightbackground="#000000")
        self.Scale1.configure(highlightcolor="black")
        self.Scale1.configure(highlightthickness="0")
        self.Scale1.configure(orient="horizontal")
        self.Scale1.configure(troughcolor="#200fbc")
        self.Scale1.configure(width=8)
        coolant_:object = self.Scale1.get()

        def oil(oil_: int = 0):
            oil_ = int(oil_) 
            self.Canvas1.delete("tag2")
            self.Canvas1.create_text (570, 345, text=oil_, fill="#42f5d7", anchor='nw', font=("Arial", 16),tag="tag2")
            self.Canvas1.create_text(1090, 150, fill="#42f5d7", text="Oil meter on", font=("Arial", 10),tag="tag2")
            self.Canvas1.create_text(1074, 157, fill="white",  anchor='s', font=("Arial Bold", 10), tag="tag2")
        
        self.Scale2 = tk.Scale(top,command=oil, from_=0.0, to=99.0)
        self.Scale2.place(relx=0.008, rely=0.917, relwidth=0.08, relheight=0.0
                , height=41, bordermode='ignore')
        self.Scale2.configure(activebackground="#39ede1")
        self.Scale2.configure(background="#000000")
        self.Scale2.configure(borderwidth="0")
        self.Scale2.configure(font="TkTextFont")
        self.Scale2.configure(foreground="#ffffff")
        self.Scale2.configure(highlightbackground="#d9d9d9")
        self.Scale2.configure(highlightcolor="black")
        self.Scale2.configure(highlightthickness="0")
        self.Scale2.configure(orient="horizontal")
        self.Scale2.configure(troughcolor="#200fbc")
        self.Scale2.configure(width=8)
        oil_:object = self.Scale2.get()

        def rpm(rpm_: int = 0):
            rpm_ = int(rpm_) 
            self.Canvas1.delete("tag3")
            self.Canvas1.create_text (710, 260, text=rpm_, fill="#42f5d7", anchor='nw', font=("Arial", 40),tag="tag3")
            self.Canvas1.create_text(1095, 180, fill="#42f5d7", text="rpm meter on", font=("Arial", 10),tag="tag3")
            self.Canvas1.create_text(1076, 187, fill="white", anchor='s', font=("Arial Bold", 10), tag="tag3")
                
        self.Scale3 = tk.Scale(top,command=rpm, from_=0.0, to=300.0)
        self.Scale3.place(relx=0.008, rely=0.813, relwidth=0.078, relheight=0.0
                , height=37, bordermode='ignore')
        self.Scale3.configure(activebackground="#39ede1")
        self.Scale3.configure(background="#000000")
        self.Scale3.configure(borderwidth="0")
        self.Scale3.configure(font="TkTextFont")
        self.Scale3.configure(foreground="#ffffff")
        self.Scale3.configure(highlightbackground="#000000")
        self.Scale3.configure(highlightcolor="black")
        self.Scale3.configure(highlightthickness="0")
        self.Scale3.configure(orient="horizontal")
        self.Scale3.configure(troughcolor="#200fbc")
        self.Scale3.configure(width=8)
        rpm_:object = self.Scale3.get()

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.09, rely=0.826, height=31, width=119)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''CRANK SPEED''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.09, rely=0.882, height=31, width=136)
        self.Label2.configure(background="#000000")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''COOLANT TEMP''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.098, rely=0.931, height=31, width=82)
        self.Label3.configure(background="#000000")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''OIL TEMP''')

        def mph(mph_: int = 0):
            mph_ = int(mph_) 
            self.Canvas1.delete("tag4")
            self.Canvas1.create_text (260, 260, text=mph_, fill="#42f5d7", anchor='nw', font=("Arial", 40),tag="tag4")
            self.Canvas1.create_text(1092, 210, fill="#42f5d7", text="Speed meter on", font=("Arial", 10),tag="tag4")
            self.Canvas1.create_text(1076, 217, fill="white", anchor='s', font=("Arial Bold", 10), tag="tag4")
            
        self.Scale3_1 = tk.Scale(top,command=mph, from_=0.0, to=180.0)
        self.Scale3_1.place(relx=0.273, rely=0.813, relwidth=0.078, relheight=0.0, height=37, bordermode='ignore')
        self.Scale3_1.configure(activebackground="#39ede1")
        self.Scale3_1.configure(background="#000000")
        self.Scale3_1.configure(borderwidth="0")
        self.Scale3_1.configure(font="TkTextFont")
        self.Scale3_1.configure(foreground="#ffffff")
        self.Scale3_1.configure(highlightbackground="#000000")
        self.Scale3_1.configure(highlightcolor="black")
        self.Scale3_1.configure(highlightthickness="0")
        self.Scale3_1.configure(orient="horizontal")
        self.Scale3_1.configure(troughcolor="#200fbc")
        self.Scale3_1.configure(width=8)
        mph_:object = self.Scale3_1.get()

        def amb(amb_: int = 0):
            amb_ = int(amb_) 
            self.Canvas1.delete("amb")
            self.Canvas1.create_text (515, 205, text=amb_, fill="#42f5d7", anchor='nw', font=("Arial", 12),tag="amb")
            self.Canvas1.create_text(1092, 360, fill="#42f5d7", text="Ambient mode on", font=("Arial", 10),tag="amb")
            self.Canvas1.create_text(1076, 337, fill="white", anchor='s', font=("Arial Bold", 10), tag="amb")
        
        self.Scale3_2 = tk.Scale(top,command=amb, from_=0.0, to=50.0)
        self.Scale3_2.place(relx=0.523, rely=0.813, relwidth=0.078, relheight=0.0, height=37, bordermode='ignore')
        self.Scale3_2.configure(activebackground="#39ede1")
        self.Scale3_2.configure(background="#000000")
        self.Scale3_2.configure(borderwidth="0")
        self.Scale3_2.configure(font="TkTextFont")
        self.Scale3_2.configure(foreground="#ffffff")
        self.Scale3_2.configure(highlightbackground="#000000")
        self.Scale3_2.configure(highlightcolor="black")
        self.Scale3_2.configure(highlightthickness="0")
        self.Scale3_2.configure(orient="horizontal")
        self.Scale3_2.configure(troughcolor="#200fbc")
        self.Scale3_2.configure(width=8)
        amb_:object = self.Scale3_2.get()

        self.Label1_3 = tk.Label(top)
        self.Label1_3.place(relx=0.355, rely=0.833, height=31, width=139)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#000000")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(foreground="#ffffff")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''VEHICLE SPEED''')
        self.Label1_3.configure(width=139)
        def gearUp():
            global g
            if g<6:
                g=g+1    
                '''host = socket.gethostname()   # as both code is running on same pc
                port = 5000  # socket server port number
                client_socket = socket.socket()  # instantiate
                client_socket.connect((host, port))  # connect to the server
                message ="Current Gear level-" +f'{g}'''
                self.Canvas1.delete("gearUp")
                self.Canvas1.create_text(530, 337, fill="#42f5d7", text=g, anchor='s', font=("Arial", 45),tag="gearUp")
                self.Canvas1.create_text(1092, 340, fill="#42f5d7", text="Car is in gear mode", font=("Arial", 10),tag="gearUp")
                self.Canvas1.create_text(1076, 280, fill="white", anchor='s', font=("Arial Bold", 10), tag="gearUp")
                '''while message.lower().strip() != 'quit':
                    client_socket.send(message.encode())  # send message
                    thread1=threading.Thread(target=current_session)
                    thread1.start()
                    data = client_socket.recv(1024).decode("utf-8", "ignore")  # receive response
                    print('Received from server: ' + data)  # show in terminal
                client_socket.close()   close the connection'''
        #Button1= tk.Button(top, command=threading.Thread(target=gearUp).start())               
        self.Button1 = tk.Button(top,command=gearUp)
        self.Button1.place(relx=0.273, rely=0.882, height=32, width=38)
        self.Button1.configure(activebackground="#39ede1")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#092bd8")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''+''')
        self.Button1.configure(width=38)
        def gearDn():
            global  g
            if g>0:
                g=g-1
                #def client_program():
                '''host = socket.gethostname()   # as both code is running on same pc
                port = 5000  # socket server port number
                client_socket = socket.socket()  # instantiate
                client_socket.connect((host, port))  # connect to the server
                message = "Current gear level-"+f'{g}' # take input'''
                self.Canvas1.delete("gearUp")
                self.Canvas1.create_text(530, 337, fill="#42f5d7", text=g, anchor='s', font=("Arial", 45),tag="gearUp")
                self.Canvas1.create_text(1092, 340, fill="#42f5d7", text="Gear decreament by 1", font=("Arial", 10),tag="gearUp")
                self.Canvas1.create_text(1076, 280, fill="white",anchor='s', font=("Arial Bold", 10), tag="gearUp")
                '''while message.lower().strip() != 'quit':
                    #message = "Current gear level-"+f'{g}' #take input
                    client_socket.send(message.encode())  # send message
                    thread1=threading.Thread(target=current_session)
                    thread1.start()
                    data = client_socket.recv(1024).decode()  # receive response
                    print('Received from server: ' + data)  # show in terminal
                    message = data # again take input
                client_socket.close()'''
        #my_button1_5= tk.Button(top, command=threading.Thread(target=gearDn).start())
        self.Button1_5 = tk.Button(top,command=gearDn)
        self.Button1_5.place(relx=0.316, rely=0.882, height=32, width=38)
        self.Button1_5.configure(activebackground="#39ede1")
        self.Button1_5.configure(activeforeground="#000000")
        self.Button1_5.configure(background="#092bd8")
        self.Button1_5.configure(disabledforeground="#a3a3a3")
        self.Button1_5.configure(foreground="#ffffff")
        self.Button1_5.configure(highlightbackground="#d9d9d9")
        self.Button1_5.configure(highlightcolor="black")
        self.Button1_5.configure(pady="0")
        self.Button1_5.configure(text='''-''')

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.355, rely=0.889, height=31, width=139)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#000000")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#ffffff")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''GEAR SELECTOR''')
        self.Label1_4.configure(width=139)
        def parkOn():
            self.Canvas1.delete("parkOff")
            #if keyboard.is_pressed("b"):
            '''host = socket.gethostname()   # as both code is running on same pc
            port = 5000  # socket server port number
            client_socket = socket.socket()  # instantiate
            client_socket.connect((host, port))  # connect to the server
            message = 'Park on             '  # message pass'''
            self.Canvas1.create_text(1092, 270, fill="#42f5d7", text="Parking mode on.", font=("Arial", 10),tag="parkOn")
            self.Canvas1.create_text(1076, 277, fill="white", anchor='s', font=("Arial Bold", 10), tag="parkOn")
            '''while message.lower().strip() != 'quit':
                client_socket.send(message.encode())  # send message
                thread1=threading.Thread(target=current_session)
                thread1.start()
                data = client_socket.recv(1024).decode("utf-8", "ignore")  # receive response
                print('Received from server: ' + data)  # show in terminal
            client_socket.close()'''
        self.Button1_6 = tk.Button(top,command=parkOn)
        #self.Button1_6.bind("<KeyPress>",parkOn)
        self.Button1_6.place(relx=0.523, rely=0.882, height=32, width=38)
        self.Button1_6.configure(activebackground="#39ede1")
        self.Button1_6.configure(activeforeground="#000000")        
        self.Button1_6.configure(background="#092bd8")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''ON''')
        self.Button1_6.configure(width=98)

        def parkOff():
            self.Canvas1.delete("parkOn")
            #if keyboard.is_pressed("a"):
            ''''host = socket.gethostname()   #as both code is running on same pc
            port = 5000  #socket server port number
            client_socket = socket.socket()  #instantiate
            client_socket.connect((host, port))  #connect to the server
            message = 'Park off             '  #message pass'''
            self.Canvas1.create_rectangle(510, 410, 555, 435, fill='black',tag="parkOff")
            self.Canvas1.create_text(1092, 270, fill="#42f5d7", text="Parking mode off", font=("Arial", 10),tag="parkOff")
            self.Canvas1.create_text(1076, 277, fill="white", anchor='s', font=("Arial Bold", 10), tag="parkOff")
            '''while message.lower().strip() != 'quit':
                client_socket.send(message.encode())  #send message
                thread1=threading.Thread(target=current_session)
                thread1.start()
                data = client_socket.recv(1024).decode("utf-8", "ignore")  #receive response
                print('Received from server: ' + data)  #show in terminal
            client_socket.close()  '''
        self.Button1_6 = tk.Button(top,command=parkOff)
        #self.Button1_6.bind("<KeyPress>",parkOff)
        self.Button1_6.place(relx=0.57, rely=0.882, height=32, width=38)
        self.Button1_6.configure(activebackground="#39ede1")
        self.Button1_6.configure(activeforeground="#000000")
        self.Button1_6.configure(background="#092bd8")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''OFF''')
        self.Button1_6.configure(width=98)

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.609, rely=0.833, height=31, width=139)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#000000")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#ffffff")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''AMBIENT TEMP''')

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.609, rely=0.889, height=31, width=139)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#000000")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#ffffff")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''PARKING BRAKE''')

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.605, rely=0.938, height=31, width=139)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#000000")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#ffffff")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''DOOR LOCKS''')

        doorOpen = ('Doors Unlocked')
        def DoorOpen(do_: int = 50):
            rpm_ = int(do_) 
            self.Canvas1.delete("tagclosed","tagopen")
            '''host = socket.gethostname()   # as both code is running on same pc
            port = 5000  # socket server port number
            client_socket = socket.socket()  # instantiate
            client_socket.connect((host, port))  # connect to the server
            message = 'Door open            '  # message pass'''
            self.Canvas1.create_text(530, 250, fill="#42f5d7", text=doorOpen, font=("Arial", 12),tag="tagopen")
            self.Canvas1.create_text(1092, 240, fill="#42f5d7", text="Door unlocked", font=("Arial", 10),tag="tagopen")
            self.Canvas1.create_text(1076, 247, fill="white", anchor='s', font=("Arial Bold", 10), tag="tagopen")
            '''while message.lower().strip() != 'quit':
                client_socket.send(message.encode())  # send message
                thread1=threading.Thread(target=current_session)
                thread1.start()
                data = client_socket.recv(1024).decode("utf-8", "ignore")  # receive response
                print('Received from server: ' + data)  # show in terminal
            client_socket.close()'''
    
        self.Button1_6 = tk.Button(top,command=DoorOpen)
        self.Button1_6.place(relx=0.523, rely=0.938, height=32, width=38)
        self.Button1_6.configure(activebackground="#39ede1")
        self.Button1_6.configure(activeforeground="#000000")
        self.Button1_6.configure(background="#092bd8")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''O''')
        doorClosed = ('Doors Locked')

        def DoorClosed(dc_: int = 12):
            rpm_ = int(dc_) 
            self.Canvas1.delete("tagopen","tagclosed")
            '''host = socket.gethostname()   # as both code is running on same pc
            port = 5000  # socket server port number
            client_socket = socket.socket()  # instantiate
            client_socket.connect((host, port))  # connect to the server
            message = 'Door locked         '  # message pass'''
            self.Canvas1.create_text(530, 250, fill="#42f5d7", text=doorClosed, font=("Arial", 12),tag="tagclosed")
            self.Canvas1.create_text(1092, 240, fill="#42f5d7", text="Door closed", font=("Arial", 10),tag="tagclosed")
            self.Canvas1.create_text(1076, 247, fill="white", anchor='s', font=("Arial Bold", 10), tag="tagclosed")
            '''while message.lower().strip() != 'quit':
                client_socket.send(message.encode())  # send message
                thread1=threading.Thread(target=current_session)
                thread1.start()
                data = client_socket.recv(1024).decode("utf-8", "ignore")  # receive response
                print('Received from server: ' + data)  # show in terminal
            client_socket.close()'''
        self.Button1_6 = tk.Button(top,command=DoorClosed)
        self.Button1_6.place(relx=0.57, rely=0.938, height=32, width=38)
        self.Button1_6.configure(activebackground="#39ede1")
        self.Button1_6.configure(activeforeground="#000000")
        self.Button1_6.configure(background="#092bd8")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(foreground="#ffffff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''C''')

        def ignitionOn():
            self.Canvas1.delete("ignitionOff")
            '''host = socket.gethostname()  # as both code is running on same pc
            port = 5000  # socket server port number
            client_socket = socket.socket()  # instantiate
            client_socket.connect((host, port))  # connect to the server
            message = 'key Onn             '  # message pass'''
            self.Canvas1.create_text(1092, 300, fill="#42f5d7", text="Ignition mode on.", font=("Arial", 10),tag="igntionOn")
            self.Canvas1.create_text(1120, 300, fill="white", anchor='s', font=("Arial Bold", 10), tag="ignitionOn")
            '''while message.lower().strip() != 'quit':
                client_socket.send(message.encode())  # send message
                thread1=threading.Thread(target=current_session)
                thread1.start()
                data = client_socket.recv(1024).decode("utf-8", "ignore")  # receive response
                print('Received from server: ' + data)  # show in terminal
            client_socket.close()'''
        self.Button1_7 = tk.Button(top,command = ignitionOn)
        self.Button1_7.place(relx=0.750, rely=0.860, height=39, width=48)
        self.Button1_7.configure(activebackground="#39ede1")
        self.Button1_7.configure(activeforeground="#000000")
        self.Button1_7.configure(background="#092bd8")
        self.Button1_7.configure(disabledforeground="#a3a3a3")
        self.Button1_7.configure(foreground="#ffffff")
        self.Button1_7.configure(highlightbackground="#d9d9d9")
        self.Button1_7.configure(highlightcolor="black")
        self.Button1_7.configure(pady="0")
        self.Button1_7.configure(text='''Onn key''')
        self.Button1_7.configure(width=98)

        def ignitionOff():
            self.Canvas1.delete("ignitionOn")
            host = socket.gethostname()  # as both code is running on same pc
            port = 5000  # socket server port number'
            client_socket = socket.socket()  # instantiate
            client_socket.connect((host, port))  # connect to the server
            self.Canvas1.create_text(1092, 320, fill="#42f5d7", text="Ignition mode off", font=("Arial", 10),tag="ignitionOff")
            self.Canvas1.create_text(1120, 300, fill="white", anchor='s', font=("Arial Bold", 10), tag="ignitionOff")
            message = 'key off'
            while True:	
                message = "\nclient:{}\n".format(message)
                #self.send_sms(message)#Client replying 
                client_socket.send(message.encode())  
                '''data = client_socket.recv(1024).decode("utf-8", "ignore")  # receive response
                print('Received from server: ' + data)'''  # show in terminal
        self.my_button1_7= tk.Button(top, command=threading.Thread(target=gearDn).start())
        self.Button1_7 = tk.Button(top,command = ignitionOff)
        self.Button1_7.place(relx=0.75, rely=0.925, height=39, width=48)
        self.Button1_7.configure(activebackground="#39ede1")
        self.Button1_7.configure(activeforeground="#000000")
        self.Button1_7.configure(background="#092bd8")
        self.Button1_7.configure(disabledforeground="#a3a3a3")
        self.Button1_7.configure(foreground="#ffffff")
        self.Button1_7.configure(highlightbackground="#d9d9d9")
        self.Button1_7.configure(highlightcolor="black")
        self.Button1_7.configure(pady="0")
        self.Button1_7.configure(text='''Off key''')
        self.Button1_7.configure(width=98)  

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.605, rely=0.938, height=31, width=139)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#000000")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#ffffff")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''DOOR LOCKS''')

        def current_session():
            host = socket.gethostname()
            # as both code is running on same pc
            port = 5000  # socket server port number
            client_socket = socket.socket()  # instantiate
            client_socket.connect((host, port))# connect to the server'''
            mainframe=Frame(root,bg="cadetblue")
            dataframe=Frame(mainframe,bd=1,relief=SUNKEN,bg="cadetblue").place(relx=0.85,rely=0.860,width=75,height=25)
            mylabel=Label(root,font=("Arial Bold", 10),text="Current session",activebackground="#f9f9f9",
                activeforeground="black",background="#000000",
                disabledforeground="#a3a3a3",foreground="#ffffff",
                highlightbackground="#d9d9d9").place(relx=0.85, rely=0.710,width=100,height=25)
            while True:    
                data=client_socket.recv(1024).decode()
                ax1=IntVar()
                #x1=(int(data))
                ax1.set(data)
                textlabel=Entry(dataframe,bg='ghostwhite',borderwidth=10,width=10,bd=8,textvariable=ax1).place(relx=0.86, rely=0.750)
        thread1=threading.Thread(target=current_session)
        thread1.daemon=True
        thread1.start()
thread2=threading.Thread(target=vp_start_gui)
thread2.start()