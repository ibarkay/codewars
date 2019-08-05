def longestWord(sen):
    longys = sen.split()
    lonngtrue = ''
    for i in longys:
        if len(i) > len(lonngtrue):
            lonngtrue = str(i)

    return lonngtrue


longestWord("Argument goes here")

