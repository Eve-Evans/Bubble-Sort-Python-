#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sorting Numbers with Bubble Sort
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import csv #For reading and writing CSV files 
import os #For interacting with the operating system. 
import time #Imports system clock
import tracemalloc #For tracking memory usage.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Bubble sort function
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def bubble_sort(data):
    """
    Performs Bubble Sort on a list of numbers.
    Includes code for an early‑exit, if no swaps occur in a pass then
    the algorithm stops early because the list is already sorted.
    
    """
    n = len(data)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j] #If the values are in the wrong order they swap position
                swapped = True
                
        if not swapped: #If no swaps occur in a pass, the algorithm stops early for optimisation.
            break
                
    return data

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# File paths for input and output CSV files
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

folder_path = r'C:/25007820_COMP1421_Assignment02/CSV Files/Numbers'
input_filename = 'number_dataset.csv'
output_filename = 'sorted_numbers_bubble.csv'

input_path = os.path.join(folder_path, input_filename)
output_path = os.path.join(folder_path, output_filename)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Runs bubble sort
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def run_lab():
    
    if not os.path.exists(input_path): #Checks if the file exist
        print(f"Error: {input_path} not found.")
        return

    # 1. Load Data
    numbers = []
    with open(input_path, mode='r', encoding='utf-8-sig') as file: #Opens CSV file
        reader = csv.reader(file) #Reads CSV file
        for row in reader:
            if row:
                numbers.append(int(row[0].strip())) #Adds each number from CSV file to list of numbers

    print(f"Sorting {len(numbers)} numbers...")

    # 2. Start Performance Tracking
    tracemalloc.start()           # Start memory tracking
    start_time = time.perf_counter() # Start time tracking

    # Execute Sort
    sorted_numbers = bubble_sort(numbers)

    # 3. Stop Performance Tracking
    end_time = time.perf_counter()   # Stop time tracking
    current, peak = tracemalloc.get_traced_memory() # The highest amount of data used during tracking
    tracemalloc.stop()            # Stop memory tracking

    # 4. Saves the sorted output to CSV file. 
    with open(output_path, mode='w', newline='') as f:
        writer = csv.writer(f)
        for num in sorted_numbers:
            writer.writerow([num])

    # Prints Performance Results
    duration = end_time - start_time
    print("-" * 30)
    print("Algorithm: Bubble Sort")
    print(f"Execution Time: {duration:.6f} seconds")
    print(f"Peak Memory Usage: {peak / 1024:.2f} KB")
    print()
    print(f"Output saved to: {output_path}")
    print("-" * 30)

if __name__ == "__main__": # Prevents run_lab() from executing automatically if this file is imported somewhere else.
    run_lab()
