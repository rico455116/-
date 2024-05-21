import tkinter as tk

def add_counter():
    global counter
    counter += 1
    counter_label.config(text = "times：{}".format(counter))
    
def zero_counter():
    global counter
    counter = 0
    counter_label.config(text = "times：{}".format(counter)) 
    
counter = 0
root = tk.Tk()
root.geometry("400x200+200+200")
root.title("窗口程式")
root.config(background = "pink")
label = tk.Label(root, text = "計數器")
label.pack()
counter_label = tk.Label(root, text = "目前計數:0")
counter_label.pack()
slider = tk.Scale(root, from_=0, to = 100, orient = "horizontal")
slider.pack()
button = tk.Button(root, text = "增加", command = add_counter)
button.pack()
button = tk.Button(root, text = "清零", command = zero_counter)
button.pack()
button = tk.Button(root, text = "退出", command = root.quit)
button.pack()

root.mainloop()
