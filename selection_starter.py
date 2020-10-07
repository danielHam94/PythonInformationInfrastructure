# Daniel Ham
# Selection Sort


from tools import *

def selection_sort(items):
    # make a copy of the list so we don't destroy the original data
    # because lists (like items) pass by reference
    ordered = items.copy()

    # sort the copy using the Selection Sort algorithm
    # YOUR CODE GOES HERE
    for i in range(len(ordered)):
        next_smallest = -1

        for j in range(i, len(ordered)):

            if ordered[j] < ordered[next_smallest]:
                next_smallest = j

        swap(ordered, next_smallest, i)

        

    return ordered



#main
print(selection_sort([3,1,7,2,6,5,0,4]))

# NOTE TO STUDENTS
# If you're having a trouble understanding the algorithm, check out this link:
# https://www.tutorialspoint.com/data_structures_algorithms/selection_sort_algorithm.htm
# You need to implement the solution yourself, however.
