import csv
import os
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# liest die csv datei aus 
filepath=input("Bitte Pfad zur Niederschlag_Daten_ungefiltert.csv Datei eingeben")
data = pd.read_csv(filepath,  sep=r";", encoding="latin1" , decimal=",")

# entfernt Zeilen mit doppelt auftretenden Stations IDs
data.drop_duplicates(subset=["Stations_id"],inplace=True)

data["Jahr"] = data["Jahr"].astype(int)
data["Stations_id"] = data["Stations_id"].astype(int)

# erstellt ein Fenster
root = tk.Tk()
root.geometry("1400x500")

# erstellt die treeview
treeview = ttk.Treeview(root)

# globale Variable die die Sortierreihenfolge speichert
reverse = False

#  Sortiert nach der angeklickten Spalte
def SortColumn(column):
    global reverse
    
    # Berücksichtigt die Sortierreihenfolge
    reverse = not reverse
    
    # löscht die View
    treeview.delete(*treeview.get_children())

    # Sortiert die Daten nach der angeklickten Spalte unter berücksichtigung der reverse Variable
    sorted_data = data.sort_values(by=column, ascending=not reverse)

    # fügt die sortierten Daten in die view ein.
    for index, row in sorted_data.iterrows():
        values = list(row.values)
        treeview.insert("", tk.END, text=index, values=values)

# Funktion um nach der Jahres Niederschlagsmenge zu sortieren
def SortByNiederschlagsmenge():
    global reverse

    # Berücksichtigt die Sortierreihenfolge
    reverse = not reverse
    
    # Löscht die aktuelle View
    treeview.delete(*treeview.get_children())

    # Berechnet die Summe des Niederschlags pro Jahr
    data['Jahresumme'] = data.iloc[:, 2:14].sum(axis=1)

    # Sortiert die Daten nach der BErechneten Summe und berückschtigt die Sortierreihenfolge
    sorted_data = data.sort_values(by='Jahresumme', ascending=not reverse)

    # Löscht die Spalte "Jahresumme"
    sorted_data.drop(columns=['Jahresumme'], inplace=True)

    # Aktualisiert die Zeilen.
    for index, row in sorted_data.iterrows():
        values = list(row.values)
        treeview.insert("", tk.END, text=index, values=values)

button_font=("Arial", 10, "bold")

# Erstellt die Spalten in der view
treeview['columns'] = list(data.columns)
for column in data.columns:
    treeview.column("#0", width=80)
    treeview.column(column,width=80, anchor="center")
    treeview.heading(column, text=column, command=lambda c=column: SortColumn(c))
    

# Erstellt die Zeilen der view.
for index, row in data.iterrows():
    values = list(row.values)
    treeview.insert("", tk.END, text=index, values=values)

# Erstellt die Sortierbuttons
sort_frame = tk.Frame(root)
sort_frame.pack()

# Erstellt einen Knopf zur Filterung nach Jahresniederschlagsmengen
# Erstellt einen Knopf zur Filterung nach Jahresniederschlagsmengen
# sort_by_niederschlag_button = tk.Button
sort_by_niederschlag_button = tk.Button(sort_frame, text="Nach Jahresniederschlagsmenge sortieren", command=lambda: SortByNiederschlagsmenge())
sort_by_niederschlag_button.pack(side=tk.LEFT)


# Packt das Widget "treeview" in das parent widget root, also das Fenster. 
# Außerdem werden hier propertys gesetzt, die dafür sorgen, dass das widget das Fenster füllt.
treeview.pack(fill=tk.BOTH, expand=1)

def save_to_csv():
    # Öffnet einen Dialog zur Auswahl des Speicherorts und Dateinamens
    file_path = filedialog.asksaveasfilename(defaultextension=".csv")

    # Öffnet eine Datei und schreibt den Inhalt des Treeview in die Datei
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        # Schreibt die Spaltenüberschriften in die Datei
        writer.writerow([treeview.heading(column)['text'] for column in treeview['columns']])
        # Schreibt die Zeilendaten in die Datei
        for row in treeview.get_children():
            writer.writerow([treeview.item(row)['values'][column] for column in range(len(treeview['columns']))])

# Erstellt einen Knopf zum abspeichern 
save_button = tk.Button(root, text="Als CSV speichern", command=save_to_csv)
save_button.pack(side=tk.RIGHT, anchor=tk.SE)

Beschreibung = tk.Label(text="Zum Filtern einfach auf die entsprechede Spalte klicken. Bei erneutem Klick wird die Sortierreihenfolge geändert")
Beschreibung.pack(side=tk.LEFT, anchor=tk.SW)

# Lässt das Fenster offen und wartet auf User-Input
root.mainloop()