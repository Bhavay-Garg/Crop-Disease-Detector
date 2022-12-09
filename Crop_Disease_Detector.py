from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tensorflow as tf
import numpy as np
import os




def wheat_detect(path_to_file):
    try:
      img_height=200
      img_width=200
      rice_class_names=['.ipynb_checkpoints', 'Brown_Rust', 'Healthy', 'Yellow_Rust']
      img = tf.keras.utils.load_img(path_to_file, target_size=(img_height, img_width))
      img_array = tf.keras.utils.img_to_array(img)
      img_array = tf.expand_dims(img_array, 0) # Create a batch
      rice_model=tf.keras.models.load_model("wheat_model.h5")
      predictions = rice_model.predict(img_array)
      score = tf.nn.softmax(predictions[0])
      print("This image most likely belongs to {} with a {:.2f} percent confidence.".format(rice_class_names[np.argmax(score)], 100 * np.max(score)))
      messagebox.showinfo("Detected","This image most likely belongs to {} with a {:.2f} percent confidence.".format(rice_class_names[np.argmax(score)], 100 * np.max(score)))
    except:
      messagebox.showerror("Error", "Unable to detect. Please try again")


# Function for opening the file explorer window
def wheat_browseFiles():
    file = filedialog.askopenfile(initialdir = "D:\Code\AI_Bootcamp\Project", title = "Select a File", filetypes = (("Images","*.jpg*"),("All Files","*.*")))
    if file:
      filepath = os.path.abspath(file.name)
      print("The File is located at : " + str(filepath))
    # Change label contents
    #label_file_explorer.configure(text="File Opened: "+file)

    wheat_detect(filepath)




def rice_detect(path_to_file):
    try:
      img_height=200
      img_width=200
      rice_class_names=['.ipynb_checkpoints', 'Brown Spot', 'Healthy', 'Hispa', 'Leaf Blast']
      img = tf.keras.utils.load_img(path_to_file, target_size=(img_height, img_width))
      img_array = tf.keras.utils.img_to_array(img)
      img_array = tf.expand_dims(img_array, 0) # Create a batch
      rice_model=tf.keras.models.load_model("rice_model.h5")
      predictions = rice_model.predict(img_array)
      score = tf.nn.softmax(predictions[0])
      print("This image most likely belongs to {} with a {:.2f} percent confidence.".format(rice_class_names[np.argmax(score)], 100 * np.max(score)))
      messagebox.showinfo("Detected","This image most likely belongs to {} with a {:.2f} percent confidence.".format(rice_class_names[np.argmax(score)], 100 * np.max(score)))
    except:
      messagebox.showerror("Error", "Unable to detect. Please try again")


# Function for opening the file explorer window
def rice_browseFiles():
    file = filedialog.askopenfile(initialdir = "D:\Code\AI_Bootcamp\Project", title = "Select a File", filetypes = (("Images","*.jpg*"),("All Files","*.*")))
    if file:
      filepath = os.path.abspath(file.name)
      print("The File is located at : " + str(filepath))
    # Change label contents
    #label_file_explorer.configure(text="File Opened: "+file)

    rice_detect(filepath)



# Create the root window
window = Tk()
  
# Set window title
window.title('File Explorer')
  
window_height = 500
window_width = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
window.resizable(False, False)


canvas=Canvas(window,height=screen_height,width=screen_width)
canvas.pack()
background_image=PhotoImage(file=r"bg.png")
canvas.create_image(0,0,anchor=NW,image=background_image)
title_image=PhotoImage(file=r"Title.png")
canvas.create_image(((window_width-454)/2),20,anchor=NW,image=title_image)
menubar=Menu(window)
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label="Exit",command=window.destroy)
help=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help)
help.add_command(label="Information",command=None)
  
# Create a File Explorer label
wheat_label = Label(window,text = "Wheat",width=8,fg = "Purple",font=("Bold",20))
rice_label = Label(window,text = "Rice",width=8,fg = "Purple",font=("Bold",20))
wheat_button = Button(window,text = "Browse Files",command = wheat_browseFiles)
rice_button = Button(window,text = "Browse Files",command = rice_browseFiles)
button_exit = Button(window,text = "Exit",command = exit)

wheat_label.place(x=80,y=170)
wheat_button.place(x=350,y=175)
rice_label.place(x=80,y=270)
rice_button.place(x=350,y=275)
button_exit.place(x=425,y=425)

window.mainloop()
