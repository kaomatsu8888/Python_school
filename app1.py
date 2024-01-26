import tkinter as tk

root = tk.Tk()
root.geometry("200x100")  # 'x' を使用する

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH")

lbl.pack()
btn.pack()
tk.mainloop()
