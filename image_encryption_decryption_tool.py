from tkinter import *
from tkinter import filedialog

# Initialize the main window
root = Tk()
root.geometry("700x500")

def encrypt_image():
    # Open file dialog to select the image file
    file_dialog = filedialog.askopenfile(mode='r', filetype=[('JPEG file', '*.jpg')])
    if file_dialog is not None:
        file_path = file_dialog.name
        encryption_key = key_entry.get(1.0, END).strip()  # Get the encryption key from the text entry
        
        with open(file_path, 'rb') as image_file:
            image_data = image_file.read()
        
        image_data = bytearray(image_data)
        for index, value in enumerate(image_data):
            image_data[index] = value ^ int(encryption_key)  # Encrypt the image data using XOR
        
        with open(file_path, 'wb') as encrypted_image_file:
            encrypted_image_file.write(image_data)

# Create an "Encrypt" button and place it on the window
encrypt_button = Button(root, text="Encrypt", command=encrypt_image)
encrypt_button.place(x=350, y=450)

# Create a text entry for the encryption key and place it on the window
key_entry = Text(root, height=4, width=20)
key_entry.place(x=290, y=350)

# Run the main event loop
root.mainloop()
