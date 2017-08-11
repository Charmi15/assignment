for x in range(2000, 3200):
    if (x % 7) == 0:
        y = x / 5.0
        if (y % 5) != 0:
            print str(x) + ",",  # coz u cant concatenate an int+a string, so convert int to str then contacate

