import tkinter as tk
from tkinter import filedialog
import os

def select_file():
    filepath = filedialog.askopenfilename()
    file_label.config(text=filepath)

def delete_file():
    filepath = file_label.cget('text')
    os.remove(filepath)
    status_label.config(text='File deleted.')

def delete_file_securely():
    filepath = file_label.cget("text")
    with open(filepath, 'rb+') as file:
        file.write(b'0' * os.path.getsize(filepath))
        file.flush()
        os.fsync(file.fileno())
    os.remove(filepath)
    status_label.config(text='File securely deleted.')

root = tk.Tk()
root.title('Secure File Deletion')

file_label = tk.Label(root, text='No file selected')
file_label.pack()

select_button = tk.Button(root, text='Select File', command=select_file)
select_button.pack()

delete_button = tk.Button(root, text='Delete File', command=delete_file)
delete_button.pack()

secure_delete_button = tk.Button(root, text='Securely Delete File', command=delete_file_securely)
secure_delete_button.pack()

status_label = tk.Label(root, text='')
status_label.pack()

root.mainloop()
