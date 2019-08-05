def group_equal(items):
    listy = []
    listOfNONequal = []

    dicky = {}
    for cu, value in enumerate(items, 1):
        dicky[cu] = value

    print dicky

    c = 0
    for i in dicky.items():
        if i[1] == dicky.items():
            print i , "yes"
            c += 1






















group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) # [[1,1],[4,4,4],["hello","hello"],[4]]


# contain the consecutive runs of equal elements of the original list