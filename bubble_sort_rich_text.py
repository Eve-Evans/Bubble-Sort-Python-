#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sorting Rich Text with Bubble Sort
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import csv #For reading and writing CSV files 
import os #For interacting with the operating system. 
import time #Imports system clock
import tracemalloc #For tracking memory usage.
import re #Used to recognise end of sentences in the data.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Bubble sort function
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def bubble_sort(data, sort_index=0):
    """
    Performs Bubble Sort on a list of rich text.
    Sort_index tells it which element in each row to sort by.
    Includes code for an early‑exit, if no swaps occur in a pass then
    the algorithm stops early because the list is already sorted.
    
    """
    n = len(data)     # Warning: For a large number of sentences, this will be very slow
    
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

folder_path = r'C:/25007820_COMP1421_Assignment02/CSV Files/Rich Text'
input_filename = 'richtext_dataset.csv'
output_filename = 'sorted_richtext.csv'

input_path = os.path.join(folder_path, input_filename)
output_path = os.path.join(folder_path, output_filename)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Runs bubble sort
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

try:
    # 1. Load and Extract all sentences from the dataset
    if not os.path.exists(input_path): #Checks if the file exist 
        print(f"Error: File not found at {input_path}")
    else:
        all_sentences = []
        with open(input_path, mode='r', newline='', encoding='utf-8-sig') as file: #Opens CSV file
            reader = csv.reader(file)  
            for row in reader: #Reads CSV file line by line
                if row: #This is to avoid errors from empty lines
                    text_block = row[0]
                    # Split by common sentence endings: . ! ?
                    sentences = re.split(r'[.!?]', text_block)
                    # Clean up and add non-empty sentences
                    for s in sentences:
                        clean_s = s.strip() #Removes spaces before and after the sentences
                        if clean_s: #Skips epmpty sentences
                            all_sentences.append(clean_s + ".")

        sample_size = 2000 
        data_to_sort = all_sentences[:sample_size]


        print(f"Dataset contains {len(all_sentences)} sentences.")
        print(f"Starting Bubble Sort on a sample of {len(data_to_sort)} sentences...")

        # 2. Starts performance tracking (Time and Space) 'Now'
        tracemalloc.start()           # Start memory tracking
        start_time = time.perf_counter() # Start time tracking
        
        sorted_list = bubble_sort(data_to_sort) #Runs sorting algorithm
        
        end_time = time.perf_counter()   # Stop time tracking
        current, peak = tracemalloc.get_traced_memory() # The highest amount of data used during tracking
        tracemalloc.stop()            # Stop memory tracking        
        
        duration = end_time - start_time
        peak_memory_kb = peak / 1024    # Convert bytes to KB

        # 3. Saves the sorted output to CSV file. 
        with open(output_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for sentence in sorted_list:
                writer.writerow([sentence])

        # Prints Performance Results
        print("-" * 45)
        print(f"Algorithm: Bubble Sort (Rich Text Sentences)")
        print(f"Execution Time: {duration:.6f} seconds")
        print(f"Peak Space Usage: {peak_memory_kb:.2f} KB")
        print()
        print(f"Sorted file saved to: {output_path}")
        print("-" * 45)

except Exception as e: # Catches any unexpected runtime errors so the program doesn't crash
    print(f"An unexpected error occurred: {e}")