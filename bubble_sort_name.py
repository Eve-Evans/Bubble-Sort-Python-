#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sorting Names with Bubble Sort
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import csv #For reading and writing CSV files 
import os #For interacting with the operating system. 
import time #Imports system clock
import tracemalloc #For tracking memory usage.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Bubble sort function
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def bubble_sort(data, sort_index=0):
    """
    Performs Bubble Sort on a list of names.
    Sort_index tells it which element in each row to sort by.
    Includes code for an early‑exit, if no swaps occur in a pass then
    the algorithm stops early because the list is already sorted.
    
    """
    n = len(data)
    
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if data[j][sort_index].lower() > data[j + 1][sort_index].lower():  #Case insensitive
                data[j], data[j + 1] = data[j + 1], data[j]  #If the values are in the wrong order they swap position
                swapped = True
                
        if not swapped: #If no swaps occur in a pass, the algorithm stops early for optimisation.
            break

    return data

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# File paths for input and output CSV files
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

folder_path = r'C:/25007820_COMP1421_Assignment02/CSV Files/Names'
input_path = os.path.join(folder_path, 'name_dataset.csv')
output_path = os.path.join(folder_path, 'sorted_bubble_names.csv')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Runs bubble sort
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

try:
    # 1. Load the data 
    rows = []
    if not os.path.exists(input_path): #Checks if the file exist
        print(f"Error: File not found at {input_path}")
    else:
        with open(input_path, mode='r', newline='', encoding='utf-8') as file: #Opens CSV file
            reader = csv.reader(file) #Reads CSV file
            for row in reader:
                if row:
                    rows.append(row) #Adds each row from CSV file to list of rows

        print(f"File loaded. Starting Bubble Sort on {len(rows)} records...")

        # 2. Starts performance tracking (Time and Space) 'Now'
        tracemalloc.start()           # Start memory tracking
        start_time = time.perf_counter() # Start time tracking
        
        sorted_rows = bubble_sort(rows, sort_index=0) #Runs sorting algorithm
        
        end_time = time.perf_counter()   # Stop time tracking
        current, peak = tracemalloc.get_traced_memory() # The highest amount of data used during tracking
        tracemalloc.stop()            # Stop memory tracking
        
        duration = end_time - start_time
        peak_memory_kb = peak / 1024  # Convert bytes to KB

        # 3. Saves the sorted output to CSV file. 
        with open(output_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(sorted_rows)

        # Prints Performance Results
        print("-" * 45)
        print(f"Algorithm: Bubble Sort")
        print(f"Execution Time: {duration:.6f} seconds")
        print(f"Peak Space Usage: {peak_memory_kb:.2f} KB")
        print()
        print(f"Output saved to: {output_path}")
        print("-" * 45)

except Exception as e: # Catches any unexpected runtime errors so the program doesn't crash
    print(f"An unexpected error occurred: {e}")