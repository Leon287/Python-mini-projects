import qrcode
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('QR Code Generator')
root.geometry("350x350")

def qr_generator():
    link = e.get()
    qr = qrcode.QRCode(version=1,box_size=5,border=4)
    qr.add_data(link)
    qr.make()
    img = qr.make_image(fill_color = 'black',bg = 'white')

    qr_img = ImageTk.PhotoImage(img)

    img_label.config(image=qr_img)
    img_label.image = qr_img


e = Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,padx=10,pady=10)
gen_button = Button(root,text='Generate QR Code',padx=10,command=qr_generator)
gen_button.grid(row=1,column=0,pady=5)

img_label = Label(root)
img_label.grid(row=2,column=0,pady=10)

root.mainloop()