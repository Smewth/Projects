import tkinter as tk
import csv

def write_to_csv():
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([entry.get() for entry in entries])

root = tk.Tk()
entries = []

for i in range(3):
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

button = tk.Button(root, text="Write to CSV", command=write_to_csv)
button.pack()

root.mainloop()

