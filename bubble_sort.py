# Bubble sort algorythm

def bubble_sort(arr):
  # Set a flag to True to start the loop
  swapped = True
  # Continue looping until the flag is set to False
  while swapped:
    # Set the flag to False at the start of each iteration
    swapped = False
    # Iterate through the list of elements
    for i in range(len(arr) - 1):
      # Compare the current element with the next element
      if arr[i] > arr[i + 1]:
        # Swap the elements if they are in the wrong order
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        # Set the flag to True to continue the loop
        swapped = True
  # Return the sorted list
  return arr
