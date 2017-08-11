#. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line
for x in range(2000, 3200):
    if (x % 7) == 0:
        y = x / 5.0
        if (y % 5) != 0:
            print str(x) + ",",  # coz u cant concatenate an int+a string, so convert int to str then concatenate

