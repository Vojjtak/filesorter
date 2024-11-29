import os
import tkinter as tk
from tkinter.filedialog import askdirectory

unsorted_file_types = [".exe", ".py", ".docx", ".xlsx", ".pdf", ".zip", ".gcode", ".stl", ".pptx", ".doc", ".jpg", ".ppt", ".txt", ".csv"]
file_types = sorted(unsorted_file_types)

# Create and open app
window = tk.Tk()
window.title("File sorter")
window.geometry("600x300")
window.resizable()

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

def file_extension(file_name):
    _, ext = os.path.splitext(file_name)
    return ext.lower()


def button_accept():
    sort()


def select():
    selected_types = []
    for i in listbox.curselection():
        selected_types.append(listbox.get(i))
    return selected_types


def select_folder():
    cwd = askdirectory(title='Select Folder')
    textbox.delete('1.0', tk.END)
    textbox.insert('1.0', cwd, tk.END)
    return cwd


def sort():
    dir = textbox.get('1.0', tk.END).strip()
    files = [f for f in os.listdir(textbox.get('1.0', tk.END).strip()) if
             os.path.isfile(os.path.join(textbox.get('1.0', tk.END).strip(), f))]
    for file in files:
        target_folder = file_extension(file)
        for type in select():
            if file_extension(file) == type:
                path = os.path.join(dir, target_folder)
                os.makedirs(path, exist_ok=True)
                os.replace(f'{dir}/{file}', f'{path}/{file}')
                msg = tk.Label(window, text='Sorted')
                msg.grid(row=4, columnspan=2,sticky=tk.S)


# List of types



listbox = tk.Listbox(window, selectmode=tk.MULTIPLE, width=50, height=20)
listbox.grid(column=0, row=0, padx=(10, 0), pady=10, sticky="nsew")

scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.grid(column=1, row=0, padx=(0, 10), pady=10, sticky="ns")

listbox.config(yscrollcommand=scrollbar.set)

for filetype in file_types:
    listbox.insert(tk.END, str(filetype))


# Textbox
textbox = tk.Text(window, height=1, width=50)
textbox.grid(column=0, row=1, padx=10, pady=11)

directory = textbox.get('1.0', tk.END).strip()


# Buttons
close_button = tk.Button(window, text="Close", command=window.destroy, width=10)
select_folder_button = tk.Button(window, text='Select folder', command=select_folder)
sort_button = tk.Button(window, text='Sort files', command=sort)

close_button.grid(column=2, row=3)
select_folder_button.grid(column=1, row=1)
sort_button.grid(column=2, row=1)


window.mainloop()

if __name__ == "__main__":
    app = window
    app.mainloop()
