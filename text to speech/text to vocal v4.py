import gtts
from playsound import playsound
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
import os






main = Tk()
main.title('TEXT TO SPEECH')
main.geometry("1000x650")
main.configure(bg="#231e1e")
main.iconbitmap("text-to-speech.ico")


img = ImageTk.PhotoImage(Image.open("text_speech.png"))
Label(main,image=img,bg="#231e1e").pack()




label = Label(main,text="Entrer le Text",bg="#231e1e",fg="white")
label.config(font=("Fixedsys",17))
label.pack()

textEnter = Entry(main,width=50,border=3,bg="#201f1f",fg="white")
textEnter.pack()



#Open TXT File Fucntion

def file_menu ():
    global v
    main.filename = filedialog.askopenfilename(initialdir="C:/Users/Administrator/Desktop",title="choose a txt file",filetypes=(("txt files","*.txt"),("csv files","*.csv")))
    t = open(main.filename,"r")
    v = t.read()
    textEnter.insert(END,v)



#Language Fucntions Text to Speech

def english ():
    global english
    try :
        english = gtts.gTTS(text=textEnter.get(),lang="en")
        english.save("en.mp3")
        playsound("en.mp3")
        os.remove("en.mp3")
    except :
        messagebox.showinfo("Error","Enter a Text First")


def french ():
    global french
    try :
        french = gtts.gTTS(text=textEnter.get(),lang="fr")
        french.save("fr.mp3")
        playsound("fr.mp3")
        os.remove("fr.mp3")
    except :
        messagebox.showinfo("Error","Enter a Text First")
    
     
def arabic ():
    global arabic
    try :
        arabic = gtts.gTTS(text=textEnter.get(),lang="ar")
        arabic.save("ar.mp3")
        playsound("ar.mp3")
        os.remove("ar.mp3")
    except :
        messagebox.showinfo("Error","Enter a Text First")


def japanese ():
    global japanese
    try :
        japanese = gtts.gTTS(text=textEnter.get(),lang="ja")
        japanese.save("ja.mp3")
        playsound("ja.mp3")
        os.remove("ja.mp3")
    except :
        messagebox.showinfo("Error","Enter a Text First")




l = Label(main,text="OU" , bg="#231e1e",fg="white")
l.config(font=("Fixedsys",17))
l.pack(pady=5)


import_ = Button(main,text="Import a TEXT File" , bg="#201f1f" , fg = "white", border=3 , padx=40 , pady=4 , command=file_menu)
import_.config(font=("Fixedsys"))
import_.pack(pady=5)




# Frame For Language Choice

frame = LabelFrame(main,text="Choisir Une Langue",bg="#231e1e",fg="white",padx=10,pady=10)
frame.config(font=("Fixedsys"))
frame.pack(pady=30)


#Language Buttons With Images 

uk = ImageTk.PhotoImage(Image.open("Country images/uk0.png"))
uk_button = Button(frame,image=uk,bg="#231e1e",command=english)
uk_button.grid(row=0,column=0,padx=15)


fr=ImageTk.PhotoImage(Image.open("Country images/fr0.png"))
fr_button = Button(frame,image=fr,bg="#231e1e",command=french)
fr_button.grid(row=0,column=1,padx=15)


ar = ImageTk.PhotoImage(Image.open("Country images/ar0.jpg"))
ar_button = Button(frame,image=ar,bg="#231e1e",command=arabic)
ar_button.grid(row=0,column=2,padx=15)


jp = ImageTk.PhotoImage(Image.open("Country images/japan0.jpg"))
jp_button = Button(frame,image=jp,bg="#231e1e",command=japanese)
jp_button.grid(row=0,column=3,padx=15)



frame_2 = LabelFrame(main,text="Volume",bg="#231e1e" , fg="white")
frame_2.config(font=("Fixedsys"))
frame_2.pack(side=LEFT)


#images for sound volume
sound_0_img = ImageTk.PhotoImage(Image.open("Volume images/volume_0_.png"))
sound_30_img = ImageTk.PhotoImage(Image.open("Volume images/volume_30_.png"))
sound_70_img = ImageTk.PhotoImage(Image.open("Volume images/volume_70_.png"))
sound_100_img = ImageTk.PhotoImage(Image.open("Volume images/volume_100_.png"))





sound_0_label = Label(frame_2 , image=sound_0_img , bg ="#231e1e")
sound_0_label.grid(row=0,column=0)


#volume controll function
def sound(x):
    global sound_0_label
    

    

    if sound_scale.get() == 0 :
        sound_0_label.config(image=sound_0_img)
        sound_0_label.grid(row=0 , column=0)

    elif sound_scale.get() > 0 and sound_scale.get() < 35:
        sound_0_label.config(image=sound_30_img)
        sound_0_label.grid(row=0 , column=0)

    elif sound_scale.get() >= 35 and sound_scale.get() < 70 :
        sound_0_label.config(image=sound_70_img)
        sound_0_label.grid(row=0 , column=0)

    elif sound_scale.get() >= 70 :
        sound_0_label.config(image=sound_100_img)
        sound_0_label.grid(row=0 ,column=0)



        



#volume scale
sound_scale = Scale(frame_2 , bg="#231e1e" , fg="white" , width=10 , length=140 , orient=HORIZONTAL , command=sound)
sound_scale.grid(row=0 , column=1)















mainloop()