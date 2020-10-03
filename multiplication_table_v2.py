## Daniel Ham
## Multiplication Table v2

## **************************** INSTRUCTIONS ****************************
## Print out a multiplication table (10 x 10).
## Print your table with a label row and column
## **********************************************************************


for i in range(11):
    if i == 0:
        print("*", end = "\t")
    else:
        print(i, end = "\t")
        
    for j in range(1, 11):
        if i == 0:
            print(1 * j, end = "\t")
        else:
            print(i * j, end = "\t")
    print()
