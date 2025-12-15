import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename


def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[('Text Files', '*.txt')])

    if not filepath:
        return 
    
    text_edit.delete(1.0,tk.END) #1.0 means line 1, character 0, END represents the end of the text box
    with open(filepath, "r") as f: #r means read mode
        content = f.read()
        text_edit.insert(tk.END, content) #END is now the begining since we deleted everything earlier
    window.title(f"Open File: {filepath}")
        

def save_file(window, text_edit):
    filepath = asksaveasfilename(defaultextension='.txt',
                                 filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    if not filepath.lower().endswith('.txt'):
        filepath = filepath + '.txt'

    with open(filepath, "w", encoding="utf-8") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Saved File: {filepath}")

def main(): #Created a main function, set the window, set the title, the loop ensures it stays running and then called the main function
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=1) #Tkinker uses a grid system, with 0,0 being the top left corner 

    #This frame will hold the buttons
    frame = tk.Frame(window, relief=tk.RAISED, bd=2) #Relief is the 3d appeareance of the element, bd is border width
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit)) #Command is a function we want to call whenever we press the button
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit)) #lambda is a way to call a function is one line 

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky='ew') #Padx and pady add padding around the button
    open_button.grid(row=1, column=0, padx=5, sticky='ew') #Sticky 'ew' makes the button expand east to west
    frame.grid(row=0, column=0, sticky='ns') #Sticky allows us to stick the frame to a certain side of the screen, it's in the north and the south side of whatever it is in

    window.bind("<Control-s>", lambda x: save_file(window, text_edit)) #Binds ctrl+s to the save function
    window.bind("<Control-o>", lambda x: open_file(window, text_edit)) #Binds ctrl+o to the open function

    window.mainloop()

main()