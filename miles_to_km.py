from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
M_TO_KM = 1.609


#functionality
def miles_to_km():
    miles = miles_entry.get()
    to_km = round(int(miles) * M_TO_KM,2)
    km_result_label.config(text=str(to_km))


#Label
label_1 = Label(text="is equal to", font=("Arial", 17, "normal"))
miles = Label(text="Miles", font=("Arial", 17, "normal"))
km = Label(text="Km", font=("Arial", 17, "normal"))

#positioning with grid
label_1.grid(column=0, row=1)
miles.grid(column=2, row=0)
km.grid(column=2, row=1)

km_result_label = Label(text="0", font= ("Arial", 12, "italic"))
km_result_label.grid(column=1, row=1)

#Button
button = Button(text="calculate", command=miles_to_km)
button.grid(column=1, row=2)

#Entry
miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

miles.config(padx=20, pady=0)
window.mainloop()
