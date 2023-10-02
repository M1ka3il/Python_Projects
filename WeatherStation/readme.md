Welcome to the Weather Data Viewer! With this tool, you can visualize and sort weather data from this specific CSV file.

The code reads a CSV file and displays its contents in a Treeview widget. The user can sort the table by clicking on the column headers. Additionally, there is a button that allows sorting the table by the sum of precipitation for each year.
At the beginning, the Pandas library is imported to read and process the CSV file, and the Tkinter library is imported to create the GUI window and widgets. 
The CSV file is read using the pd.read_csv() function and stored in a Pandas DataFrame. The file path is specified, the delimiter and decimal point type are defined, and duplicates in the "Stations_id" column are removed.

The GUI window is created using the Tk() function from Tkinter, and its size is set to 1400x500 pixels. The Treeview widget is created using the ttk.Treeview() function from Tkinter. Column headers are inserted into the widget and sorted using the SortColumn() function when clicked.

The SortColumn() function takes the column header as an argument for sorting and optionally the sorting order. 
The function first clears the current view in the Treeview widget and sorts the data in the DataFrame by the selected column. Then, the sorted table is inserted into the Treeview widget.

The SortByNiederschlagsmenge() function is called when the "Sort by Annual Precipitation" button is clicked. 
The function calculates the sum of precipitation for each year in the DataFrame, sorts the table by the calculated sum, and removes the additional column with the sums. Then, the sorted table is inserted into the Treeview widget.

Finally, the Treeview widget is filled with the data and column headers and added to the GUI window. 
The "Sort by Annual Precipitation" button is created, and the window is opened with mainloop() to wait for user input.

If you want to change the sorting order, simply click on the corresponding sorting button again. The sorting order will be reversed.

Notes:
- Changing the sorting order will reset the filtering by annual precipitation.
- Atm it just works with this specific csv file.
- The column width is set to 80 pixels and can be manually adjusted.
- You can use the scroll function to navigate through the table.
