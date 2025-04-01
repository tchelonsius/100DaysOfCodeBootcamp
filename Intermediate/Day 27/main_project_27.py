import tkinter as tk

def convert(event=None):
    result = float(entry.get())*1.609
    result_label["text"]=str(result)

    
window = tk.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=300,height=200)
window.config(padx=30,pady=30)


entry = tk.Entry(width=10)
entry.grid(column=1, row=0)

miles_label = tk.Label(text="Miles", font=("Arial", 20))
miles_label.grid(column=2, row=0)

equals_label = tk.Label(text="is equal to", font=("Arial", 20))
equals_label.grid(column=0, row=1)

result_label = tk.Label(text="0", font=("Arial",20))
result_label.grid(column=1, row=1)

km_label = tk.Label(text="Km", font=("Arial", 20))
km_label.grid(column=2, row=1)

calculate_button = tk.Button(text="Calculate",command=convert)
calculate_button.grid(column=1, row=2)
window.bind("<Return>", convert)

window.mainloop()