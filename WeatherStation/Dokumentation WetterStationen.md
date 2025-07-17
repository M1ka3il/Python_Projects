# Dokumentation: Wetterdaten-Viewer

Willkommen beim Wetterdaten-Viewer! Mit diesem Tool können Sie Wetterdaten aus einer CSV-Datei visualisieren und sortieren.

# Funktionalität 
Der Code liest eine CSV-Datei ein und zeigt deren Inhalte in einem Treeview-Widget an. 
Der Nutzer kann die Tabelle durch Klicken auf die Spaltenüberschriften sortieren lassen. 
Zusätzlich gibt es einen Button, mit dem die Tabelle nach der Summe der Niederschlagsmenge jedes Jahres sortiert werden kann.

## Systemanforderungen

Um den Wetterdaten-Viewer nutzen zu können, benötigen Sie Folgendes:

- Python 3.x
- Die Python-Module pandas und tkinter

## Installation

1. Laden Sie den Code von GitHub herunter und entpacken Sie das ZIP-Archiv.
2. Öffnen Sie die Datei `WetterdatenViewer.py` in einem Python-Editor oder einer Python-IDE.
3. Speichern Sie die Datei ab.
4. Öffnen Sie eine Konsole oder ein Terminal und wechseln Sie in das Verzeichnis, in dem die Datei `WetterdatenViewer.py` gespeichert ist.
5. Geben Sie den Befehl `python WetterdatenViewer.py` ein, um das Tool zu starten.

## Verwendung

### Schritt 1: CSV-Datei laden

Nach dem Start des Tools wird automatisch die Datei `Niederschlag_Daten_ungefiltert.csv` aus dem entsprechenden Ordner geladen. Wenn Sie eine andere CSV-Datei verwenden möchten, ändern Sie den Dateipfad in Zeile 6 des Codes entsprechend ab.

### Schritt 2: Daten anzeigen

Nachdem die Daten geladen wurden, werden sie in einer Tabelle angezeigt. Die Spaltenüberschriften dienen als Sortierbuttons. Klicken Sie auf eine Spaltenüberschrift, um die Daten nach dieser Spalte zu sortieren.

### Schritt 3: Daten filtern

Um die Daten nach Jahresniederschlagsmenge zu filtern, klicken Sie auf den Button "Nach Jahresniederschlagsmenge sortieren". Die Daten werden dann nach der Summe der Niederschlagsmengen für jedes Jahr sortiert.

### Schritt 4: Sortierreihenfolge ändern

Wenn Sie die Sortierreihenfolge ändern möchten, klicken Sie einfach erneut auf den entsprechenden Sortierbutton. Die Sortierreihenfolge wird dann umgekehrt.

## Hinweise

- Wenn Sie die Sortierreihenfolge ändern, wird die Filterung nach Jahresniederschlagsmenge zurückgesetzt.
- Wenn Sie eine andere CSV-Datei laden möchten, muss diese die gleiche Struktur wie `Niederschlag_Daten_ungefiltert.csv` haben.
- Die Spaltenbreite ist auf 80 Pixel festgelegt und kann manuell geändert werden.
- Wenn es mehr Daten als Platz in der Tabelle gibt, können Sie die Scrollfunktion benutzen, um durch die Tabelle zu navigieren.

<hr>
