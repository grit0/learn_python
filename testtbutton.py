# create multiple Tkinter buttons using a dictionary:
import tkinter as tk
def text_update(animal):
    text.delete(0, tk.END)
    text.insert(0, animal*2) 

root = tk.Tk()
text = tk.Entry(root, width=35, bg='yellow')
text.grid(row=0, column=0, columnspan=5) 
btn_dict = {}
col = 0 
words = ["Dog", "Cat", "Pig", "Cow", "Rat"] 
for animal in words:
    # pass each button's text to a function

    # create the buttons and assign to animal:button-object dict pair
    btn_dict[animal] = tk.Button(root, text=animal, command=lambda x = animal: text_update(x)) 
    btn_dict[animal].grid(row=1, column=col, pady=5) 
    col += 1 
# run the GUI event loop
btn_dict["Dog"]['text']="ddd"
btn_dict["Cow"].bind("<Enter>", lambda e:  print("ffff"))
root.mainloop()