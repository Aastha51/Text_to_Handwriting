from tkinter import *
import pywhatkit as pw
# Function to clear both the text areas
def clearAll() :
    text1_field.delete(1.0, END)
    text2_field.delete(1.0, END)
 
# Function to convert into handwriting
def convert() :
    input_text = text1_field.get("1.0", "end")[:-1]
    output_text = pw.text_to_handwriting(input_text,save_to="th.png")
    global imag
    imag=PhotoImage(file="C:/Users/Asus/Documents/th.png")
    text2_field.image_create("current",image=imag)

 
# Driver code
if __name__ == "__main__" :
 
    # Create a GUI window
    root = Tk()
    root.configure(background = 'light green') 
    root.geometry("900x850") 
    root.title("Converter")
     

    headlabel = Label(root, text = '..Welcome to text to handwriting converter..',fg = 'black', bg = "pink")
    label1 = Label(root, text = " Text: ",fg = 'black', bg = 'light blue') 
    label2 = Label(root, text = " Handwriting: ",fg = 'black', bg = 'light blue') 
    headlabel.grid(row = 0, column = 1) 
    label1.grid(row = 1, column = 0) 
    label2.grid(row = 3, column = 0)
 

    text1_field = Text(root, height = 5, width = 30, font = "lucida 13")
    text2_field = Text(root, height = 9, width = 40, font = "lucida 13")
    text1_field.grid(row = 1, column = 1, padx = 10, pady = 10) 
    text2_field.grid(row = 3, column = 1, padx = 10, pady = 10)
 
       
    
    button1 = Button(root, text = "Convert into handwriting", bg = "light yellow", fg = "black",command = convert)       
    button1.grid(row = 2, column = 1)
    button2 = Button(root, text = "Clear", bg = "light yellow",fg = "black", command = clearAll)
    button2.grid(row = 4, column = 1)
     
    # Start the GUI 
    root.mainloop() 