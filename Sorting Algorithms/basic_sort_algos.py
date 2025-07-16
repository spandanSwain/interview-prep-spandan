# selection sort
arr = [5,3,4,1,2]
for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)

"""
output:
[1, 3, 4, 5, 2]
[1, 2, 4, 5, 3]
[1, 2, 3, 5, 4]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
"""


# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]                      # Current element to be inserted
        j = i - 1

        # Shift elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Insert the key at correct location

        # Print array after each pass (optional for dry run)
        print(f"After pass {i}: {arr}")

# Example usage:
arr = [5, 3, 4, 1, 2]
print("Original:", arr)
insertion_sort(arr)
print("Sorted:  ", arr)
"""
output:
Original: [5, 3, 4, 1, 2]
After pass 1: [3, 5, 4, 1, 2]
After pass 2: [3, 4, 5, 1, 2]
After pass 3: [1, 3, 4, 5, 2]
After pass 4: [1, 2, 3, 4, 5]
Sorted:   [1, 2, 3, 4, 5]
"""


# bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        print(f"\n✅ Pass {i + 1}:")
        for j in range(n - i - 1):
            # why n-i-1?
            # after every i passes, i items are already sorted in ascending
            print(f"  🔍 Compare arr[{j}] = {arr[j]} and arr[{j+1}] = {arr[j+1]}")
            if arr[j] > arr[j + 1]:
                print(f"  👉 Swap {arr[j]} and {arr[j+1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True # so that we don't do n-1 passes each time, even if no swapping is required
            else:
                print(f"  ❌ No swap needed")
        
        print(f"🔁 After Pass {i + 1}: {arr}")
        
        if not swapped:
            print("✅ Array is already sorted. Exiting early.")
            break

# Example usage
arr = [5, 3, 4, 1, 2]
print("🔷 Original Array:", arr)
bubble_sort(arr)
print("\n✅ Sorted Array:", arr)
"""
output:
🔷 Original Array: [5, 3, 4, 1, 2]

✅ Pass 1:
  🔍 Compare arr[0] = 5 and arr[1] = 3
  👉 Swap 5 and 3
  🔍 Compare arr[1] = 5 and arr[2] = 4
  👉 Swap 5 and 4
  🔍 Compare arr[2] = 5 and arr[3] = 1
  👉 Swap 5 and 1
  🔍 Compare arr[3] = 5 and arr[4] = 2
  👉 Swap 5 and 2
🔁 After Pass 1: [3, 4, 1, 2, 5]

✅ Pass 2:
  🔍 Compare arr[0] = 3 and arr[1] = 4
  ❌ No swap needed
  🔍 Compare arr[1] = 4 and arr[2] = 1
  👉 Swap 4 and 1
  🔍 Compare arr[2] = 4 and arr[3] = 2
  👉 Swap 4 and 2
🔁 After Pass 2: [3, 1, 2, 4, 5]

✅ Pass 3:
  🔍 Compare arr[0] = 3 and arr[1] = 1
  👉 Swap 3 and 1
  🔍 Compare arr[1] = 3 and arr[2] = 2
  👉 Swap 3 and 2
🔁 After Pass 3: [1, 2, 3, 4, 5]

✅ Pass 4:
  🔍 Compare arr[0] = 1 and arr[1] = 2
  ❌ No swap needed
🔁 After Pass 4: [1, 2, 3, 4, 5]
✅ Array is already sorted. Exiting early.

✅ Sorted Array: [1, 2, 3, 4, 5]
"""

