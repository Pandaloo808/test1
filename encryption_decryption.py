from tkinter import *
from simplecrypt import encrypt, decrypt
from tkinter import filedialog
import os

root = Tk()
root.geometry("400x250")
root.configure("orange")

file_name_entry=""
encryption_text_data=""

def saveData():
    global file_name_entry
    global encryption_text_data
    file_name=file_name_entry.get()
    file_name=file_name.open("note.txt",write)
    data=encryption_text_data.get(start_index,end_index)
    ciphercode=data.encrypt("riya",encryption_text_data)
    hexBite=ciphercode.hexDigest()
    print(hexBite)
    file_name_entry.delete(0,END)
    encryption_text_data.delete(0,END)
    messagebox.showinfo("Congrats!","data has been successfuly updated")
    

def startDecryption():
    global file_name_entry
    global decryption_text_data
    root.destroy()
 
    decryption_window = Tk()
    decryption_window.geometry("600x500")
    
    decryption_text_data = Text(decryption_window, height=20, width=72)
    decryption_text_data.place(relx=0.5,rely=0.35, anchor=CENTER)
    
    btn_open_file = Button(decryption_window, text="Choose File..", font = 'arial 13')
    btn_open_file.place(relx=0.5,rely=0.8, anchor=CENTER)
    
    decryption_window.mainloop()
    
    
def startEncryption():
    global file_name_entry
    global encryption_text_data
    root.destroy()
 
    encryption_window = Tk()
    encryption_window.geometry("600x500")
    
    file_name_label = Label(encryption_window, text="File Name: ", bg="orange" , font = 'arial 13')
    file_name_label.place(relx=0.1,rely=0.15, anchor=CENTER)
    
    file_name_entry = Entry(encryption_window, font = 'arial 15')
    file_name_entry.place(relx=0.38,rely=0.15, anchor=CENTER)
    
    btn_create = Button(encryption_window, text="Create", font = 'arial 13')
    btn_create.place(relx=0.75,rely=0.15, anchor=CENTER)
    
    encryption_text_data = Text(encryption_window, height=20, width=72)
    encryption_text_data.place(relx=0.5,rely=0.55, anchor=CENTER)
    
    encryption_window.mainloop()
    
    
heading_label = Label(root, text="Encryption & Decryption" , bg="orange", font = 'arial 18 italic')
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

btn_start_encryption = Button(root, text="Start Encryption", bg="crimson" ,command=saveData , font =('arial', 13) , command=startEncryption, relief=FLAT)
btn_start_encryption.place(relx=0.3,rely=0.6, anchor=CENTER)

btn_start_decryption = Button(root, text="Start Decryption" , bg="crimson", font = 'arial 13' ,  command=startDecryption,releif=FLAT)
btn_start_decryption.place(relx=0.7,rely=0.6, anchor=CENTER)

root.mainloop()

